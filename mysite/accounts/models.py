from pickle import NONE
from django.db import models
from django.forms import NullBooleanField

class Checking(models.Model):
    name = models.CharField(max_length=50)
    acc_id = models.IntegerField(Checking)
    balance = models.FloatField()

    def __str__(self):
            return self.name

class Transaction(models.Model):
    sender = NONE
    reciever = NONE
    amount = 0
    status = 'incomplete'

    def __init__(self, senderid, receiverid, amount):    
        self.sender = Checking(acc_id=senderid)
        self.receiver = Checking(acc_id=receiverid)
        self.amount = models.FloatField()
        self.status = models.CharField()
        if (self.sender.balance >= amount):
            self.sender.balance = self.sender.balance - amount
            self.receiver.balance = self.receiver.balance + amount
            self.status = 'complete'
            self.sender.save()
            self.receiver.save()
            self.save()
        else:
            self.status = 'Sender balance too low'
            self.save()


