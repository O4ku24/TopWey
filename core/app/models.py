from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    post = models.CharField(max_length=20)


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    student = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(auto_now=True)
