from django.contrib import admin

# Register your models here.
from ads.models import Ad
from ads.models import Category
from ads.models import Char
from ads.models import Buyer
#from ads.models import Ad_char

class AdCharsInLine(admin.TabularInline):
    model = Ad.chars.through
    extra = 1

class AdAdmin(admin.ModelAdmin):
    inlines = (AdCharsInLine,)
    search_fields=['name']

admin.site.register(Ad, AdAdmin)
admin.site.register(Category)
admin.site.register(Char)
admin.site.register(Buyer)
#admin.site.register(Ad_char)
