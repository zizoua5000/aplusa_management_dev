from django.urls import path
from qaime.api.views import QaimeListAPIView,QaimeCreateAPIView,QaimeCreateReturnAPIView,QaimeDetailAPIView,QaimeUpdateDeleteAPIView,QaimeUpdateDeleteReturnAPIView,QaimeChangeStatusAPIView

app_name='qaime'
urlpatterns = [
    path('list/', QaimeListAPIView.as_view(),name='list'),
    path('detail/<pk>', QaimeDetailAPIView.as_view(),name='detail'),
    path('create/', QaimeCreateAPIView.as_view(),name='create'),
    path('create_return/', QaimeCreateReturnAPIView.as_view(),name='create_return'),
    path('update_delete/<pk>', QaimeUpdateDeleteAPIView.as_view(),name='update_delete'),
    path('update_delete_return/<pk>', QaimeUpdateDeleteReturnAPIView.as_view(),name='update_delete_return'),
    path('change_status/<pk>', QaimeChangeStatusAPIView.as_view(),name='change_status')
]
