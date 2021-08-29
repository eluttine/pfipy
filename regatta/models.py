from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


class Club(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.id}, {self.name}'

class AbstractBoat(models.Model):
    sail_number = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    finrating = models.DecimalField(max_digits=5, decimal_places=4)

    club = models.ForeignKey(Club, on_delete=SET_NULL, null=True)

    class Meta:
        abstract = True

class Boat(AbstractBoat):
    def __str__(self) -> str:
        return f'{self.id}, {self.name}'

class Regatta(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    place = models.CharField(max_length=30, null=True)
    organizer = models.CharField(max_length=30, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    club = models.ForeignKey(Club, on_delete=SET_NULL, null=True)

class Clazz(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)

    regatta = models.ForeignKey(Regatta, on_delete=CASCADE)

class Race(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30, null=True)
    start_time = models.DateTimeField()

    clazz = models.ForeignKey(Clazz, on_delete=CASCADE)

class RaceResult(AbstractBoat):
    position = models.IntegerField()
    end_time = models.DateTimeField()
    racing_time = models.IntegerField()
    handicap_time = models.IntegerField()

    race = models.ForeignKey(Race, on_delete=CASCADE)
    boat = models.ForeignKey(Boat, on_delete=SET_NULL, null=True)
