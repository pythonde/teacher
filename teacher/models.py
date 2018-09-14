from django.db.models import *


class TestModel(Model):
    tname = CharField(max_length=30,unique=True)