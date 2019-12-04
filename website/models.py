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
    tutionOutState = models.IntegerField()
    size = models.IntegerField()
    highestDegree = models.IntegerField()
    menOnly = models.IntegerField()
    womenOnly = models.IntegerField()
    averageACT = models.IntegerField()

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    passwordHash = models.CharField(max_length=58)

class Application(models.Model):
    # fields from college data table
    name = models.CharField(max_length = 300)
    state = models.CharField(max_length = 5)
    url = models.CharField(max_length = 300)
    tutionInState = models.IntegerField()
    tutionOutState = models.IntegerField()
    size = models.IntegerField()
    highestDegree = models.IntegerField()
    menOnly = models.IntegerField()
    womenOnly = models.IntegerField()
    averageACT = models.IntegerField()
    # fields from applications tables
    status = models.IntegerField()