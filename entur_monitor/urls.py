from django.urls import path

from . import views

app_name = 'monitor'

urlpatterns = [
    path('', views.monitor2_test, name='monitor2_test'),
    path('monitor/<str:stop>/<str:left>/<str:left_name>/<str:right>/<str:right_name>',
         views.monitor2_url, name='monitor2'),
    path('monitor/<str:stop>/<str:left>/<str:right>', views.monitor2_url, name='monitor2'),
    path('stops/<str:stop1>/<str:stop2>', views.monitor2_stops, name='monitor2'),
    path('debug', views.monitor2_test_debug, name='monitor2_debug'),
    path('monitor/<str:stop>', views.monitor1),
    path('clock', views.clock, name='clock'),
    path('refresh/<str:stop>/<str:quays>', views.refresh, name='refresh'),
    path('refresh/<str:stop>', views.refresh, name='refresh'),
]

"""path('limit', views.departure_limit, name='limit'),
# path('find_limit', views.departure_limit_find, name='limit_find'),"""