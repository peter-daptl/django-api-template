from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        ordering = ['make', 'model', 'year']

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
