from django.urls import path
from simcard.api.views import SimcardListCreateAPIView,SimcardUpdateDeleteAPIView

app_name='simcard'
urlpatterns = [
    path('list_create/', SimcardListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', SimcardUpdateDeleteAPIView.as_view(),name='update_delete')
]
