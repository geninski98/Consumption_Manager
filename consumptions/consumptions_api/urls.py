from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ConsumptionsView, ConsumptionsViewList

urlpatterns = [
    path('consumptions/', ConsumptionsViewList.as_view()),
    path('consumptions/<int:pk>/', ConsumptionsView.as_view())
]
