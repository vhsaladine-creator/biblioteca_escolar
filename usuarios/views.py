from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Aluno, Professor


# =========================
# 1. PÁGINA INICIAL
# =========================

def home(request):
    return render(request, "home.html")


# =========================
# 2. ESCOLHA DE CADASTRO
# =========================

def escolha_cadastro(request):
    return render(request, "escolha_cadastro.html")


# =========================
# 3. JÁ TENHO CADASTRO
# =========================

def ja_tenho_cadastro(request):
    return render(request, "ja_tenho_cadastro.html")


# =========================
# 4. ESCOLHA LOGIN
# =========================

def login_escolha(request):
    return render(request, "login_escolha.html")



# =========================
# 5. CADASTRO DE ALUNO
# =========================

def cadastro_aluno(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        ra = request.POST.get("ra")
        turma = request.POST.get("turma")
        senha = request.POST.get("senha")


        # Verifica se o RA já existe
        if User.objects.filter(username=ra).exists():
            return render(request, "cadastro_aluno.html", {
                "erro": "Esse RA já está cadastrado"
            })


        # Verifica se o email já existe
        if Aluno.objects.filter(email=email).exists():
            return render(request, "cadastro_aluno.html", {
                "erro": "Esse email já está cadastrado"
            })


        user = User.objects.create_user(
            username=ra,
            email=email,
            password=senha
        )


        Aluno.objects.create(
            user=user,
            nome=nome,
            email=email,
            telefone=telefone,
            ra=ra,
            turma=turma
        )


        return redirect("/login/aluno/")


    return render(request, "cadastro_aluno.html")



# =========================
# 6. CADASTRO DE PROFESSOR
# =========================

def cadastro_professor(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        rg = request.POST.get("rg")
        senha = request.POST.get("senha")


        # RG será o login do professor
        user = User.objects.create_user(
            username=rg,
            email=email,
            password=senha
        )


        Professor.objects.create(
            user=user,
            nome=nome,
            email=email,
            telefone=telefone,
            rg=rg
        )


        return redirect("/login/")


    return render(request, "cadastro_professor.html")



# =========================
# 7. LOGIN ALUNO
# =========================

# LOGIN ALUNO

def login_aluno(request):

    if request.method == "POST":

        ra = request.POST.get("ra")
        senha = request.POST.get("senha")

        usuario = authenticate(
            request,
            username=ra,
            password=senha
        )

        if usuario:
            login(request, usuario)
            return redirect("/painel/")


        return render(request, "login_aluno.html", {
            "erro": "RA ou senha inválidos"
        })


    return render(request, "login_aluno.html")
# =========================
# 8. LOGIN PROFESSOR
# =========================

def login_professor(request):

    if request.method == "POST":

        rg = request.POST.get("rg")
        senha = request.POST.get("senha")


        usuario = authenticate(
            request,
            username=rg,
            password=senha
        )


        if usuario:

            # confirma se é professor
            try:
                Professor.objects.get(user=usuario)

                login(request, usuario)

                return redirect("/painel/")

            except Professor.DoesNotExist:
                pass


        return render(request, "login_professor.html", {
            "erro": "RG ou senha inválidos"
        })


    return render(request, "login_professor.html")



# =========================
# 9. PAINEL
# =========================

def painel(request):

    if request.user.is_authenticated:

        return render(request, "painel.html")


    return redirect("/login/")



# =========================
# 10. LOGOUT
# =========================

def logout_usuario(request):

    logout(request)

    return redirect("/")