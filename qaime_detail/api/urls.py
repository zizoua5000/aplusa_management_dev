from django.urls import path
from qaime_detail.api.views import QaimeDetailListCreateAPIView,QaimeDetailUpdateDeleteAPIView

app_name='qaime_detail'
urlpatterns = [
    path('list_create/', QaimeDetailListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', QaimeDetailUpdateDeleteAPIView.as_view(),name='update_delete')
]
