from django.contrib import admin
from .models import Card, Element, Expansion, Pokemon
# Register your models here.

admin.site.register(Card)
admin.site.register(Element)
admin.site.register(Expansion)
admin.site.register(Pokemon)