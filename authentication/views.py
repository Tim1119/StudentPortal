from django.core.mail import message
from django.shortcuts import render,redirect
from django.views.generic import CreateView,View
from .forms import LoginUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.contrib.auth import logout
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .utils import token_generator
from django.views.decorators.cache import cache_control
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate,login,logout
# Create your views here.


class RegisterUserView(CreateView):

    form_class=LoginForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('authentication:login') 

    def post(self,request):
        #print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            
            user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name)
            user.set_password(password)
            user.is_active = False 
            user.save()
                    
            #path to view 
            # get our current site and relative url 
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

            domain = get_current_site(request).domain
            link = reverse('authentication:activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})


            email_subject = 'Activate your account'

            activate_url = 'http://'+domain+link
            email_body = 'Hi' + first_name + last_name +' please use this link to verify your account\n' + activate_url
            send_email = EmailMessage(email_subject,email_body,'noreply@emicolon.com',[email])
            send_email.send()
            messages.success(request,'account succesfully created. check your email to activate account')
            return redirect('authentication:login')
        else:
           
            return render(request,'registration/register.html',{'form':form})

class LoginUser(LoginView):
    template_name = 'registration/login.html'
    form_class= LoginUserForm 
    
    def post(self,request):
        form = LoginUserForm()
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            print(user)

            if user:
                if user.is_active:
                    login(request,user)
                    messages.success(request,'Welcome, '+user.username+'you are now logged in')
                    return redirect('authentication:home')
                else:
                    messages.error(request,'sorry, your account is not active.please check your email')
                    return redirect('authentication:login')
            else:
                messages.error(request,'Invalid Credentials, try again')
                return redirect('authentication:login')
        else:
            messages.error(request,'please fill all fields')
            return redirect('authentication:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required
def HomeView(request):
    return render(request,'index.html')  




def UserLogoutView(request):
        
    logout(request)
    messages.success(request,'you have been logged out')
    return redirect('authentication:login')


class VerificationView(View):

    def get(self,request, uidb64, token):
        try:
            id=force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user,token):
                return redirect('authentication:login' + '?message='+'user already activated')


            if user.is_active:
                return redirect('authentication:login')
            else:
                user.is_active = True 
                user.save()
                
                messages.success(request,'Account activated successfully')
                return redirect('authenticatin:login')
        except Exception as e:
            pass
        return redirect('authentication:login')