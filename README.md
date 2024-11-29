# Shop

> [!TIP]
> [Main Django commands](https://github.com/DeMonA1/MyBlog__Django/blob/main/README.md#diamonds-basic-django-commands)

## Launch service
In order to run myshop app:

1. [RabbitMQ (docker container)](#rabbitmq):
   ```
   docker run -it <--rm> --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
2. Runserver:
   ```
   python manage.py runserver
3. [Celery (cmd)](#celery):
   ```
   celery -A myshop worker -l info
4. [Stripe webhook (cmd)](#stripe):
   ```
   stripe listen --forward-to 127.0.0.1:8000/payment/webhook/
6. [Redis (docker container)](#redis):
   ```
    docker run --it --name redis -p 6379:6379 redis
   
## Necessary services

### RabbitMQ
You have to install Celery and RabbitMQ for executing asynchronous tasks. Celery is used as the Worker and RabbitMQ as the Message Broker:
```
docker run -it <--rm> --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```
> [!NOTE]
> Run web-based management user interface on port 15672.
> 
> login/password: guest/guest; <http://localhost:15672/>

### Celery
To use Celery, you have to create celery config file such as ***celery.py***.
So following command to launch Celery:
```
celery -A myshop worker -l info
```
> -A -> -app, -l => log-level to info (info messages).

### Celery[Flower]
You can add Flower to monitor the asynchronous tasks that are executing with Celery
```
celery -A myshop flower --basic-auth=username:password
```

### Stripe
1. For implementation payment for our app, we have to choose the 
payment gateway providers. We chose Stripe. Also you need to 
[register](https://www.stripe.com).
2. Next step, you have to create the account to process payments.
3. Go to the [link](https://dashboard.stripe.com/test/apikeys)
and take publishable and secret keys to ***.env*** file inside root
derictory.
4. Add ***STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, STRIPE_API_VERSION*** and ***STRIPE_API_VERSION = 'xxxx'***,
which you can find using this [link](https://docs.stripe.com/upgrades), to the ***settings*** file.
5. Any credit card you can find by [link](https://docs.stripe.com/testing#international-cards>)

<ins>***To use stripe webhook***</ins>:

1. You have to install stripe-cli via brew:
```
brew install stripe/stripe-cli/stripe
```
or, if you haven't brew,
download it from <https://github.com/stripe/stripe-cli/releases/latest>
3. After installation, go with next command:
```
stripe login
```
4. Run this command:
```
stripe listen --forward-to 127.0.0.1:8000/payment/webhook/
```
5. Use the secret key, which you got as ***STRIPE_WEBHOOK_SECRET***
in ***.env*** file.

### Redis
Run Redis container as follows:
```
 docker run --it --name redis -p 6379:6379 redis
```
In this app we used Redis for the recommendation system. First of all, to do this,
you have to add Redis settings to ***settings.py*** file:
- REDIS_HOST = 'localhost'
- REDIS_PORT = 6379
- REDIS_DB = 1

## About static files
In order to use common static files in our your Shop project, you need
to add ***STATIC_ROOT*** constant to ***settings.py*** file of myshop project.
Next, run the command, which copies all static files from your apps 
defined in STATIC_ROOT directory:
```
python manage.py collectstatic
```

## [About e-mail](https://github.com/DeMonA1/MyBlog__Django/blob/main/README.md#dart-settings)



## Internalization and localization
1. For internalization of your app, you should add ***LANGUAGE*** constant
to ***settings.py*** file specifying languages which available for app. If this
parameter is not defined, app will be available in all the languages that Django
is translated into. Example:
LANGUAGES = [

    ('en', 'English'),

    ('ru', 'Russian'),

]

If you use gettext_lazy function (which frequently imported as '_'), the languages names will be translating only when they are accessed.
3. After set up LANGUAGE_CODE = 'en' (the last parameter Django refers to)
4. Add 'django.middleware.locale.LocaleMiddleware' to the MIDDLEWARE
setting. Make sure that this middleware comes after SessionMiddleware 
because LocaleMiddleware needs to use session data. It also has to be
placed before CommonMiddleware because the latter needs an active
language to resolve the requested URL.
5. Create the following directory structure inside the main project 
directory, next to the manage.py file:
locale/
    en/
    ru/
and add this to settings.py file: 
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
6. Run the following command (you will create .po files for each language):
django-admin makemessages --all
7. Fill msgstr in .po files with translations of msgid  
8. Run following command:
django-admin compilemessages

When you will be use django-parler for models translation,
change bases parameter on:
bases=(parler.models.TranslatableModel, models.Model)
(may be, this drawback will be correct in the future version)

Note about localization.
This feature don't appropriate for outputting JS or JSON, which
has provide a machine-readable format. In order to on/off localization:
{% load l10n %}
{% localize on %}
{{ value }}
{% endlocalize %}
{% localize off %}
{{ value }}
{% endlocalize %}
OR use special filters: {{ value|localize }} {{ value|unlocalize }}

You can access to rosetta application by URI:
<http://127.0.0.1:8000/en/rosetta/>


CONTAINER.
REDIS_HOST = 'cache' # localhost without docker compose
