from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('filldata', views.FillData().as_view(), name = 'filldata'),
    path('deldata', views.DelData().as_view(), name = 'deldata'),
    path('getjson', views.GetJson().as_view(), name = 'getjson'),
]