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


For implementation payment for our app, we have to choose the 
payment gateway providers. You chose Stripe. Also you need to 
register on the <https://www.stripe.com>.
Next step, you have to create the account to process payments.
3. <https://dashboard.stripe.com/test/apikeys>