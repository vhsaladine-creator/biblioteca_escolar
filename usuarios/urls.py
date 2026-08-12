from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.escolha_cadastro, name="escolha_cadastro"),
    path("ja_tenho_cadastro/", views.ja_tenho_cadastro, name="ja_tenho_cadastro"),
    path("cadastro/aluno/", views.cadastro_aluno, name="cadastro_aluno"),
    path("cadastro/professor/", views.cadastro_professor, name="cadastro_professor"),
    path("login/", views.login_escolha, name="login"),
    path("login/aluno/", views.login_aluno, name="login_aluno"),
    path("login/professor/", views.login_professor, name="login_professor"),
    path("painel/", views.painel, name="painel"),
    path("painel/aluno/", views.painel_aluno, name="painel_aluno"),
    path("painel/professor/", views.painel_professor, name="painel_professor"),
    path("logout/", views.logout_usuario, name="logout"),
]
