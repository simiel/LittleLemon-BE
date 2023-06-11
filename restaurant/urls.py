from django.urls import path, include
from django.conf.urls import url
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.bookingView.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    url(r'^auth/', include('djoser.urls')),    
]

