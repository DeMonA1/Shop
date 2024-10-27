# Shop

You have to install Celery and RabbitMQ for executing asynchronous tasks. Celery is used as the Worker and RabbitMQ as the Message Broker:

docker run -it <--rm> --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
# run web-based management user interface on port 15672
login/password: guest/guest


To use Celery, you have to create celery config file such as celery.py

So following command to launch Celery:

# -A - app, -l log-level to info (info messages)
celery -A myshop worker -l info