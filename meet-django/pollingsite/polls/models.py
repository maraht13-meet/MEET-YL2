from django.db import models

# Create your models(classes) here.

class Poll(models.Model):
	Questions = models.CharField(max_length=200)
class Choice(models.Model):
	Choice = models.CharField(max_length=200)
	poll= models.ForeignKey(Poll)
