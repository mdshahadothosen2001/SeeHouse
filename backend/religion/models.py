from django.db import models


class ReligionModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = "Religions"
        db_table = "religion"
