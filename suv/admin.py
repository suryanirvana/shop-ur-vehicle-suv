from django.contrib import admin

# Importing Models
from .models import *

# Registering Models
admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Article)
admin.site.register(Review)
admin.site.register(Transaction)