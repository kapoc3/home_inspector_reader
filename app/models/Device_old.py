from tortoise.models import Model
from tortoise import fields


class Device(Model):
    name = fields.CharField(max_length=255, null=True)
    public_ip = fields.CharField(max_length=100, null=True)
    private_ip = fields.CharField(max_length=100, null=True)
    mac = fields.CharField(max_length=100, null=True)
    city = fields.CharField(max_length=255, null=True)
    country = fields.CharField(max_length=255, null=True)
    latitude = fields.FloatField(null=True)
    longitude = fields.FloatField(null=True)
    region = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "device"

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return self.name