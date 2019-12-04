from django.db import models

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Schools(models.Model):
    name = models.CharField(max_length = 300)
    state = models.CharField(max_length = 5)
    url = models.CharField(max_length = 300)
    tutionInState = models.IntegerField()
    size = models.IntegerField()
    averageACT = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

