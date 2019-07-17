from django.urls import path

from . import views

app_name = 'monitor'

urlpatterns = [
    path('', views.monitor2_test, name='monitor2_test'),
    path('monitor/<str:stop>/<str:left>/<str:left_name>/<str:right>/<str:right_name>',
         views.monitor2_url, name='monitor2'),
    path('monitor/<str:stop>/<str:left>/<str:right>', views.monitor2_url, name='monitor2'),
    path('debug', views.monitor2_test_debug, name='monitor2_debug'),
    path('clock', views.clock, name='clock'),
    path('refresh/<str:stop>/<str:quays>', views.refresh, name='refresh')
]
