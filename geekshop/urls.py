# from django.conf.urls import url, include
from django.conf.urls import include
from django.contrib import admin
import mainapp.views as mainapp
from adminapp import views

from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path, path

urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    re_path(r'^contact/', mainapp.contact, name='contact'),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    path('order/', include('ordersapp.urls', namespace='order')),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('export_users_xls/', views.export_users_xls),
    path('export_products_xls/', views.export_products_xls),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#    import debug_toolbar
#
#    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
