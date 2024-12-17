from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.text import Truncator
from django.utils.html import format_html

from .models import Adresse, Servicecategorie,Service

# Register your models here.
class ServiceCategorieAdmin(admin.ModelAdmin):
    list_display=('nom_service','slug')
admin.site.register(Servicecategorie,ServiceCategorieAdmin)
###

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'photo', 'date_ajout', 'slug')
    list_filter = ('date_ajout',)
    search_fields = ('titre', 'slug')

    

admin.site.register(Service, ServiceAdmin)
#
class AdresseAdmin(admin.ModelAdmin):
    list_display=('id','pays','ville','quartier','repere','contact','utilisateur')
admin.site.register(Adresse,AdresseAdmin)
#