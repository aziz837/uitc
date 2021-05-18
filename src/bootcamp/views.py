
from django.conf import settings
from django.shortcuts import render, redirect
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import datetime
from .models import Person, Courser
# from .forms import ImageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout, login




def index(request):
    print
    return render(request, 'main/index.html', {})

def contact(request):
    try:
        if request.method=='POST':
            first_name=request.POST['username']
            lastname=request.POST['lastname']
            email=request.POST['email']
            phone=request.POST['phone']
            message=request.POST['message']
            
            date = datetime.date.today()
            sms = str(first_name) + '\n' + str(lastname) + '\n' + str(email) + '\n' + str(phone)+'\n\n' + str(message)+'\n'+str(date)
            send_mail('CONTACT FORM',
                            sms,
                            settings.EMAIL_HOST_USER,
                            ['mubashirov2002@gmail.com'],
                            fail_silently=False)
        return render(request, 'main/contact.html')
    except :
        return redirect('/')

   
def reg(request):
    if request.method == 'POST':
        first_name = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            u=User.objects.filter(username=first_name)
            if u.exists():
                messages.warning(request,'Bunday foydalanuvchi mavjud!')
                return redirect('boot:register')
            else:
                user1=User(username=first_name,email=email,password=make_password(password1))
                user1.save()
                person=Person(user=user1,first_name=first_name,last_name=last_name,email=email,password=password1,phone=phone)
                person.save()
                return redirect('boot:login')
        else:
            messages.warning(request,"Parolni to'gri kiriting!")
    return render(request, 'main\singup.html')


    
            
def login_view(request):
    if request.method=='POST':
        username=request.POST['firstname']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('boot:index')
        else:
            messages.warning(request,"Bunday foydalanuvchi yo'q!")
    return render(request, 'main\login.html', {})




def logout_view(request, pk):
    user = User.objects.get(id=pk).delete()
    return redirect('boot:index')

def profile(request, pk):
    user = get_object_or_404(Person, user_id=pk)
    courser = Courser.objects.all()
    
    return render(request, 'main/prof.html', {'user':user})


def edit_profile(request, pk):
    user = get_object_or_404(Person, user_id=pk)
    if request.method == 'POST' and request.FILES['img']:\
        # try:
            photo = request.FILES['img']
        # except Exception:
        #     print('rasm yo')
            username=request.POST['username']
            lastname = request.POST['last_name']
            email=request.POST['email']
            phone = request.POST['phone']
            fullname = username+ ' ' + lastname
            user.photo = photo
            user.last_name = fullname
            user.phone = phone
            user.email = email
            user.save()
            return redirect('/')
    return render(request, 'main/edit-profile.html', {'user':user })