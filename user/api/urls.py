from django.urls import path
from user.api.views import UserRegisterListCreateAPIView,UserUpdateDeleteAPIView

app_name='user'
urlpatterns = [
    path('register_list/', UserRegisterListCreateAPIView.as_view(),name='register_list'),
    path('update_delete/<pk>', UserUpdateDeleteAPIView.as_view(),name='update_delete'),
]
