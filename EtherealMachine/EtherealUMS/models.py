from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('superadmin', 'Super Admin'),
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
        ('operator', 'Operator'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    
    def __str__(self):
        return self.username

class Machine(models.Model):
    machine_id = models.CharField(max_length=20, unique=True)
    machine_name = models.CharField(max_length=50)
    tool_capacity = models.IntegerField()
    tool_offset = models.FloatField()
    feedrate = models.IntegerField()
    tool_in_use = models.IntegerField()

    def __str__(self):
        return self.machine_name

class Axis(models.Model):
    axis_name = models.CharField(max_length=10)
    max_acceleration = models.FloatField()
    max_velocity = models.FloatField()
    actual_position = models.FloatField()
    target_position = models.FloatField()
    distance_to_go = models.FloatField()
    homed = models.BooleanField(default=False)
    acceleration = models.FloatField()
    velocity = models.FloatField()
    machine = models.ForeignKey(Machine, related_name='axes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.axis_name} of {self.machine}"

