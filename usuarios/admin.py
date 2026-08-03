# Importa o sistema de administração do Django
from django.contrib import admin

# Importa os models criados no app
from .models import Aluno, Professor

# Registra o model Aluno no painel admin
# Assim ele poderá ser visualizado e gerenciado em /admin/
admin.site.register(Aluno)

# Registra o model Professor no painel admin
admin.site.register(Professor)

