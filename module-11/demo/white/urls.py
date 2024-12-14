#Mark White
#CSD325
#11.2


from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home')
]
