from django.db import models


class Data(models.Model):
    data = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.data)
