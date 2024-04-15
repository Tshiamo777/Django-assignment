from django.contrib.gis.db import models

# Create your models here.

class InfrustructureType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class InfrustructureItem(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    geometry = models.PointField(blank=True, null=True)
    infrustructure_item_type = models.ForeignKey(InfrustructureType, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.infrustructure_item_type}"

class LogAction(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class ManagmentLog(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=False)
    infrustructure_item = models.ForeignKey(InfrustructureItem, models.CASCADE, blank=True, null=True)
    infrustructure_log_action = models.ForeignKey(LogAction, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.infrustructure_item}, {self.infrustructure_log_action}"




