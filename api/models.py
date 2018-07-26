from django.db import models
# Create your models here.
class Car(models.Model):
    #Types of cars
    SEDAN = "S"
    LIMOUSINE = "LI"
    STRETCH_LIMOUSINE ="S_LI"
    MINIBUS = "MB"
    SUV = "SUV"
    VAN = "VAN"

    #Types of classes
    FIRST = "F"
    ECONOMY = "ECO"
    BUSINESS = "B"
    SPECIAL = "S"

    class_choices =(
    (FIRST, "Pierwsza"),
    (ECONOMY, "Ekonomiczna"),
    (BUSINESS, "Biznesowa"),
    (SPECIAL, "Specjalna"),
    )

    types_choices = (
    (SEDAN, "Sedan"),
    (LIMOUSINE, "Limousine"),
    (STRETCH_LIMOUSINE, "Stretch Limousine"),
    (MINIBUS, "MiniBus"),
    (SUV, "Suv"),
    (VAN, "Van"),
    )

    Manufacturer = models.CharField(max_length=100)
    CarModel = models.CharField(max_length=10)
    CarClass = models.CharField(max_length=10, choices=class_choices)
    CarType = models.CharField(max_length=10, choices=types_choices)
    CarInfo = models.TextField()
    CarID = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __del__(self):
        pass

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' %(self.CarID, self.Manufacturer, self.CarModel, self.CarType, self.CarClass, self.CarInfo)
