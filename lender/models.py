from django.db import models


class LoanPlans(models.Model):
    class_name = models.CharField(max_length=255)
    count = models.IntegerField()
    amount = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.class_name
