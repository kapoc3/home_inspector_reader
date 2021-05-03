from tortoise.models import Model
from tortoise import fields


class Device(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "device"

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return self.name