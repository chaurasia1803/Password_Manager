from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from .models import Password
from .utils import encrypt_password, decrypt_password


def hello(request):
    return render(request, 'vault/hello.html')

@login_required
def password_list(request):
    passwords = Password.objects.filter(user=request.user)

    for p in passwords:
        p.decrypted = decrypt_password(p.password)

    return render(request, 'vault/password_list.html',{
        'passwords' : passwords
    })

@login_required
def add_password(request):
    if request.method == "POST":
        Password.objects.create(
            user=request.user,
            website=request.POST['website'],
            username=request.POST['username'],
            password=encrypt_password(request.POST['password']),
            notes= request.POST.get('notes', '')
        )
        return redirect('vault:password_list')

    # 👇 fetch passwords to show in table
    passwords = Password.objects.filter(user=request.user)

    return render(request, 'vault/add_password.html', {
        'passwords': passwords
    })


def reveal_password(request, pk):
    pwd = Password.objects.get(id=pk, user= request.user)
    return JsonResponse({
        "password" : decrypt_password(pwd.password)
    })
