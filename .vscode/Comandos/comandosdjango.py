# # # comandos django

# senha ubunto MKAqsD/3


# python manage.py runserver
# django-admin startproject project .
# django-admin --help
# python manage.py startapp home
# python manage.py collectstatic
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py makemigrations

# # # instalaçoes

# pip install whitenoise
# pip install django
# pip freeze > 'requirements.txt'
# pip freeze
# pip help uninstall
# pip help install

# # # Ativaçao do venv

# primeiro
# python -m venv venv
# depois
# python -m .venv venv
# .venv\Scripts\activate
# python.exe -m pip install --upgrade pip

# # # desinstala todos o requirementos

# pip freeze > requirementstmp.txt
# Isso vai gerar um arquivo requirementstmp.txt.
# Com este arquivo basta desinstalar todos os pacotes:
# pip uninstall -r requirementstmp.txt -y

# # # instalando todos o requirementos

# pip install -r 'requirements.txt'

# # Configurar o git
"""
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore

git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
git log
git push origin main -u
git status
git push
"""
# Trabalhando com o model do Django

# # Importe o módulo
# from contact.models import Contact
# # Cria um contato (Lazy)
# # Retorna o contato
# contact = Contact(**fields)
# contact.save()
# # Cria um contato (Não lazy)
# # Retorna o contato
# contact = Contact.objects.create(**fields)
# # Seleciona um contato com id 10
# # Retorna o contato
# contact = Contact.objects.get(pk=10)
# # Edita um contato
# # Retorna o contato
# contact.field_name1 = 'Novo valor 1'
# contact.field_name2 = 'Novo valor 2'
# contact.save()
# # Apaga um contato
# # Depende da base de dados, geralmente retorna o número
# # de valores manipulados na base de dados
# contact.delete()
# # Seleciona todos os contatos ordenando por id DESC
# # Retorna QuerySet[]
# contacts = Contact.objects.all().order_by('-id')
# # Seleciona contatos usando filtros
# # Retorna QuerySet[]
# contacts = Contact.objects.filter(**filters).order_by('-id')
