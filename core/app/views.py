from django.shortcuts import render
from .models import User
import datetime

def home(request):
    if request.method == "GET":
        return render(request=request, template_name='home.html')
    
    if request.method == "POST":
        return render(request=request, template_name='home.html')
    
def register(request):
    if request.method == "GET":
        return render(request=request, template_name='reg.html')
    if request.method == "POST":
        User.objects.create(first_name = request.POST.get('first_name'), 
                                    last_name = request.POST.get('last_name'), 
                                    mail = request.POST.get('usermail'),
                                    phone = request.POST.get('phone'), 
                                    password = request.POST.get('password'),
                                    post = 'user')
        return render(request=request, template_name='auth.html')

def auth_user(request):
    if request.method == "POST":
        user_phone = request.POST.get('phone')
        user_password = request.POST.get('password')
        user = User.objects.filter(phone = user_phone, password = user_password).values()
        if user.filter(post = 'admin'):
            print(f'Admin Enter')
            return render(request=request, template_name='admin_journal.html')
        if user.filter(post = 'user'):
            user_name = f'{user[0]["first_name"] + " " + user[0]["last_name"]}'
            print(f'{user_name} Enter\nData {datetime.datetime.now()} ')
            user_id = user[0]["id"]
            data = {}
            data['user'] = user_name
            data['id'] = user_id
            return render(request=request, template_name='user_journal.html', context=data)
        else:
            return render(request=request, template_name='auth.html')

    if request.method == "GET":
        return render(request=request, template_name='auth.html')