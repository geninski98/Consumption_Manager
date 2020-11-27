from rest_framework import generics, filters
from .serializers import ConsumptionSerializer
from .models import Consumptions

# Create your views here.
class ConsumptionsViewList(generics.ListCreateAPIView):
    serializer_class = ConsumptionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__category__code']

    def get_queryset(self):
        queryset = Consumptions.objects.all()
        filterCategory = self.request.query_params.get('filterCategory', None)
        if filterCategory is not None:
            queryset = queryset.filter(product__category__code=filterCategory)
        return queryset

class ConsumptionsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consumptions.objects.all()
    serializer_class = ConsumptionSerializer