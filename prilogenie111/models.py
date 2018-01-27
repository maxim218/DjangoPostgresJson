from django.db import models
from django.utils import timezone

class PeopleModel(models.Model):
    man_name = models.TextField()
    man_sername = models.TextField()
    man_age = models.IntegerField()

    def __str__(self):
        return str(self.man_name) + "___" + str(self.man_sername)


