from django.urls import path
import market.views
from django.conf.urls.static import static
from django.conf import settings
#
app_name = "market"
urlpatterns = [
    path("",market.views.home,name='homepage'),
    path("services/",market.views.services,name='service_all'),
    path('contacts',market.views.contact,name='contact'),
    ##SERVICES PARTY
      path('dashboard/',market.views.dashboard_admin,name='dashboard'),
    ##ARTICLE
        path('add-service/', market.views.add_service, name='add_service'),
        path('<slug:slug>/update/', market.views.service_update, name='update_service'),
        path('<slug:slug>/delete/', market.views.service_delete, name='delete_service'),
     path('details/service/<slug:service_slug>/', market.views.detail, name='service_detail'),
     #CATEGORIE ARTICLE
    path('categorie_service',market.views.service_categorie,name='service'),
    path('add_categorie_service/',market.views.add_categorie_service,name='add_categorie_service'),
    path('<slug:slug>/service_categoriedelete/', market.views.categorie_service_delete, name='delete_categorie_service'),
    path('<slug:slug>/service_categorieupdate/', market.views.categorie_service_update, name='update_categorie_service'),

    path('create/', market.views.adresse_create, name='create_adresse'),
     path('addresses/update/<int:pk>/', market.views.update_address, name='update_adresse'),
    path('addresses/delete/<int:pk>/', market.views.delete_address, name='delete_adresse'),

]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)