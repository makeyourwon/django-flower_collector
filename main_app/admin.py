from django.contrib import admin

# Register your models here.
from .models import Flower, Hydrate, Customer



admin.site.register(Flower)
admin.site.register(Hydrate)
admin.site.register(Customer)
