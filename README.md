# Natural-World [![Build Status](https://skillicons.dev/icons?i=github)](https://github.com/klebersonfialhobaleeiro)

Sistema de sla oq



## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.9+
- [Django](http://www.djangoproject.com) == 4.2.5
- [Pillow](https://pypi.org/project/Pillow/) - Biblioteca principal de imagens
- [Python-dotenv](https://pypi.org/project/python-dotenv/) - Python-dotenv lê pares chave-valor de um .envarquivo e pode defini-los como variáveis ​​de ambiente. 
- [XAMPP](https://www.apachefriends.org/pt_br/index.html) (Opcional) - Caso queira outro banco de dados


## Instalação:

1. Instalar as bibliotecas/pacotes/dependências:

```bash
Instale o Python: https://www.python.org/downloads/
Clone o Repositório: $ git clone https://github.com/Anaaalisss/NaturalWorld.git 
```
```bash
Criar/ativar um ambiente virtual: 
    Criando: $ virtualenv nome_da_virtualenv

    Ativando:   $ source nome_da_virtualenv/bin/activate (Linux ou macOS)
                $ nome_da_virtualenv/Scripts/Activate (Windows) 
```

```bash
Depois com o ambiente já ativado instale as dependências:
    $ pip install -r requirements.txt
```

2. Configuração para o Django:

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate

Para criar um superusuário:
    $ python3 manage.py createsuperuser

Para rodar o projeto:
    $ python3 manage.py runserver
```
3. Criar um arquivo chamado .env (email configura aqui)
#### Adicione no arquivo .env:
```bash
    #Link com tutorial: https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'email'
    EMAIL_HOST_PASSWORD = 'senha'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
```

4. Configurar o Mysql(Opcional)

#### Adicione no arquivo .env:
```bash
    DATABASES_ENGINE=django.db.backends.mysql
    DATABASES_NAME=NameDataBase
    DATABASES_USER=NameUser
    DATABASES_PASSWORD=SenhaDataBase
    DATABASES_HOST=127.0.0.1
    DATABASES_PORT=3306
```

#### configurando no settings.py:
```bash
No lugar de: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Use:
    DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASES_ENGINE'),
        'NAME': os.getenv('DATABASES_NAME'),
        'USER': os.getenv('DATABASES_USER'),
        'PASSWORD': os.getenv('DATABASES_PASSWORD'),
        'HOST': os.getenv('DATABASES_HOST'),
        'PORT': os.getenv('DATABASES_PORT'),
    }
}
```
