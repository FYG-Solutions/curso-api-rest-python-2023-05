from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
