from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render

from .models import Aluno, Professor


def home(request):
    return render(request, "home.html")


def escolha_cadastro(request):
    return render(request, "escolha_cadastro.html")


def ja_tenho_cadastro(request):
    return redirect("login")


def login_escolha(request):
    return render(request, "login_escolha.html")


def _identificador_aluno(ra, digito_ra, uf):
    return f"{ra.strip()}-{digito_ra.strip()}-{uf.strip().upper()}"


def cadastro_aluno(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        email = request.POST.get("email", "").strip().lower()
        telefone = request.POST.get("telefone", "").strip()
        ra = request.POST.get("ra", "").strip()
        digito_ra = request.POST.get("digito_ra", "").strip()
        uf = request.POST.get("uf", "SP").strip().upper()
        turma = request.POST.get("turma", "").strip()
        senha = request.POST.get("senha", "")

        if not all([nome, email, ra, digito_ra, uf, turma, senha]):
            return render(request, "cadastro_aluno.html", {
                "erro": "Preencha todos os campos obrigatórios."
            })

        if Aluno.objects.filter(ra=ra).exists():
            return render(request, "cadastro_aluno.html", {
                "erro": "Esse RA já está cadastrado."
            })

        if User.objects.filter(email=email).exists() or Aluno.objects.filter(email=email).exists():
            return render(request, "cadastro_aluno.html", {
                "erro": "Esse e-mail já está cadastrado."
            })

        username = _identificador_aluno(ra, digito_ra, uf)
        if User.objects.filter(username=username).exists():
            return render(request, "cadastro_aluno.html", {
                "erro": "Esses dados de acesso já estão cadastrados."
            })

        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                email=email,
                password=senha,
            )
            Aluno.objects.create(
                user=user,
                nome=nome,
                email=email,
                telefone=telefone,
                ra=ra,
                digito_ra=digito_ra,
                uf=uf,
                turma=turma,
            )

        return redirect("login_aluno")

    return render(request, "cadastro_aluno.html")


def cadastro_professor(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        email = request.POST.get("email", "").strip().lower()
        telefone = request.POST.get("telefone", "").strip()
        rg = request.POST.get("rg", "").strip()
        senha = request.POST.get("senha", "")

        if not all([nome, email, rg, senha]):
            return render(request, "cadastro_professor.html", {
                "erro": "Preencha todos os campos obrigatórios."
            })

        if User.objects.filter(username=rg).exists() or Professor.objects.filter(rg=rg).exists():
            return render(request, "cadastro_professor.html", {
                "erro": "Esse RG já está cadastrado."
            })

        if User.objects.filter(email=email).exists() or Professor.objects.filter(email=email).exists():
            return render(request, "cadastro_professor.html", {
                "erro": "Esse e-mail já está cadastrado."
            })

        with transaction.atomic():
            user = User.objects.create_user(
                username=rg,
                email=email,
                password=senha,
            )
            Professor.objects.create(
                user=user,
                nome=nome,
                email=email,
                telefone=telefone,
                rg=rg,
            )

        return redirect("login_professor")

    return render(request, "cadastro_professor.html")


def login_aluno(request):
    if request.method == "POST":
        ra = request.POST.get("ra", "").strip()
        digito_ra = request.POST.get("digito_ra", "").strip()
        uf = request.POST.get("uf", "SP").strip().upper()
        senha = request.POST.get("senha", "")

        username = _identificador_aluno(ra, digito_ra, uf)
        usuario = authenticate(request, username=username, password=senha)

        # Compatibilidade com cadastros antigos, que usavam apenas o RA.
        if usuario is None:
            usuario = authenticate(request, username=ra, password=senha)

        if usuario and Aluno.objects.filter(user=usuario).exists():
            login(request, usuario)
            return redirect("painel_aluno")

        return render(request, "login_aluno.html", {
            "erro": "RA, dígito, UF ou senha inválidos."
        })

    return render(request, "login_aluno.html")


def login_professor(request):
    if request.method == "POST":
        rg = request.POST.get("rg", "").strip()
        senha = request.POST.get("senha", "")
        usuario = authenticate(request, username=rg, password=senha)

        if usuario and Professor.objects.filter(user=usuario).exists():
            login(request, usuario)
            return redirect("painel_professor")

        return render(request, "login_professor.html", {
            "erro": "RG ou senha inválidos."
        })

    return render(request, "login_professor.html")


def painel(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if Aluno.objects.filter(user=request.user).exists():
        return redirect("painel_aluno")
    if Professor.objects.filter(user=request.user).exists():
        return redirect("painel_professor")

    return redirect("login")


def painel_aluno(request):
    if not request.user.is_authenticated or not Aluno.objects.filter(user=request.user).exists():
        return redirect("login_aluno")
    aluno = Aluno.objects.get(user=request.user)
    return render(request, "painel_aluno.html", {"aluno": aluno})


def painel_professor(request):
    if not request.user.is_authenticated or not Professor.objects.filter(user=request.user).exists():
        return redirect("login_professor")
    professor = Professor.objects.get(user=request.user)
    return render(request, "painel_professor.html", {"professor": professor})


def logout_usuario(request):
    logout(request)
    return redirect("home")
