# docker run -it --name redis -p 6379:6379 redis
# python manage.py shell

from shop.models import Product
black_tea = Product.objects.get(name='Black tea')
green_tea = Product.objects.get(name='Green tea')
plate = Product.objects.get(name='Simple plate')
pot = Product.objects.get(name='Tea pot')
vic_pot = Product.objects.get(name='Victorian tea pot')

from shop.recommender import Recommender
r = Recommender()
r.produts_bought([black_tea, green_tea])
r.produts_bought([black_tea, pot])
r.produts_bought([black_tea, green_tea, vic_pot])
r.produts_bought([vic_pot, plate])
r.produts_bought([plate, pot])
r.produts_bought([black_tea, green_tea, plate])

r.suggest_products_for([black_tea])
r.suggest_products_for([green_tea])
r.suggest_products_for([vic_pot])
r.suggest_products_for([plate])


# using translations in QuerySets
from shop.models import Product
from django.utils.translation import activate
activate('de')
product=Product.objects.first()
product.name
# another way
product=Product.objects.language('en').first()
product.name # 'Green tea'
# set another language for an object
product.set_current_language('de')
product.name # 'Grüner Tee'
product.get_current_language() # 'de
# we cna filter using the related translation objects with
# translations__xxxx
Product.objects.filter(translations__name="Green tea")