from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # PÁGINA INICIAL
    # =========================
    path(
        '',
        views.home,
        name='home'
    ),


    # =========================
    # ESCOLHA DE CADASTRO
    # =========================
    path(
        'cadastro/',
        views.escolha_cadastro,
        name='escolha_cadastro'
    ),


    # =========================
    # JÁ TENHO CADASTRO
    # =========================
    path(
        'ja_tenho_cadastro/',
        views.ja_tenho_cadastro,
        name='ja_tenho_cadastro'
    ),


    # =========================
    # CADASTROS
    # =========================

    path(
        'cadastro/aluno/',
        views.cadastro_aluno,
        name='cadastro_aluno'
    ),


    path(
        'cadastro/professor/',
        views.cadastro_professor,
        name='cadastro_professor'
    ),


    # =========================
    # LOGIN ESCOLHA
    # =========================

    path(
        'login/',
        views.login_escolha,
        name='login'
    ),


    # =========================
    # LOGIN ALUNO
    # =========================

    path(
        'login/aluno/',
        views.login_aluno,
        name='login_aluno'
    ),


    # =========================
    # LOGIN PROFESSOR
    # =========================

    path(
        'login/professor/',
        views.login_professor,
        name='login_professor'
    ),


    # =========================
    # PAINEL
    # =========================

    path(
        'painel/',
        views.painel,
        name='painel'
    ),


    # =========================
    # LOGOUT
    # =========================

    path(
        'logout/',
        views.logout_usuario,
        name='logout'
    ),

]