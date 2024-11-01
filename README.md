# Shop

You have to install Celery and RabbitMQ for executing asynchronous tasks. Celery is used as the Worker and RabbitMQ as the Message Broker:

docker run -it <--rm> --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
# run web-based management user interface on port 15672
login/password: guest/guest; <http://localhost:15672/>


To use Celery, you have to create celery config file such as celery.py

So following command to launch Celery:

# -A - app, -l log-level to info (info messages)
celery -A myshop worker -l info

You can add Flower to monitor the asynchronous tasks that are executing with Celery

celery -A myshop flower --basic-auth=username:password

1. For implementation payment for our app, we have to choose the 
payment gateway providers. You chose Stripe. Also you need to 
register on the <https://www.stripe.com>.
2. Next step, you have to create the account to process payments.
3. Go to the link <https://dashboard.stripe.com/test/apikeys>
and take publishable and secret keys to .env file inside root
derictory
4. Add STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY, STRIPE_API_VERSION and STRIPE_API_VERSION = 'xxxx', which you can find using this link <https://docs.stripe.com/upgrades>, to the settings file.
5. Any credit card you can find by link <https://docs.stripe.com/testing#international-cards>

To use stripe webhook:

1. You have to install stripe-cli via brew:
brew install stripe/stripe-cli/stripe or, if you haven't brew,
download it from <https://github.com/stripe/stripe-cli/releases/latest>
2. After installation, go with next command: 
stripe login
3. Run this command:
stripe listen --forward-to 127.0.0.1:8000/payment/webhook/
4. Use the secre key which you got as STRIPE_WEBHOOK_SECRET in .env
file.

In order to run myshop app:

1. RabbitMQ (docker)
2. Runserver
3. Celery (cmd)
4. Stripe webhook (cmd)
