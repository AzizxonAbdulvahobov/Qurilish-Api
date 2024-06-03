from django.db import models

# Create your models here.

class Hudud(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name



class Tashkilot(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name


class Bino(models.Model):
    tashkilot = models.ForeignKey(Tashkilot, on_delete=models.CASCADE)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    maydon = models.IntegerField()
    qavat = models.IntegerField()
    parkovka = models.BooleanField(default=False)
    plashatka = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)


    def __str__(self) :
        return self.name