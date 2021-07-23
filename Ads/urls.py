from django.urls import path
from . import views


urlpatterns = [
    path('channel/all/', views.channel_list, name='list of all channels'),
    path('channel/<int:pk>/', views.ChannelDetail.as_view(), name = 'channel detail'),
    path('discount/all/', views.DiscountList.as_view(), name='discount list'),
]