# Importa o painel administrativo padrão do Django
from django.contrib import admin

# Importa:
# path = usado para criar rotas/URLs
# include = usado para "puxar" URLs de outro arquivo
from django.urls import path, include

# Lista principal de rotas do projeto
urlpatterns = [
    # Rota do painel administrativo do Django
    # Exemplo: http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # Diz que a página inicial do projeto ("")
    # vai usar as rotas do app "usuarios"
    # Ou seja, tudo que estiver em usuarios/urls.py
    # será controlado por essa linha
    path('', include('usuarios.urls')),
]
