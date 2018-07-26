from tastypie.resources import ModelResource
from api.models import Car
class CarResource(ModelResource):
    class Meta:
        queryset = Car.objects.all()
        resource_name = 'car'
