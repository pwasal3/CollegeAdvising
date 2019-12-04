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
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class SchoolOutput(models.Model):
    schoolName = models.CharField(max_length = 300)
    cityName = models.CharField(max_length = 300)
    state = models.CharField(max_length = 5)
    site = models.CharField(max_length = 300)
    tuition = models.IntegerField()
    size = models.IntegerField()
    actScore = models.IntegerField()
    satScore = models.IntegerField()
