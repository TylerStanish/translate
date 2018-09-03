# from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(application)
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
