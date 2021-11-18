from django.db import models
from django.forms import ModelForm
from django import forms

class User(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    Gender = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    IsActive = models.BooleanField(default=True)

class Quiz(models.Model):
    Title = models.CharField(max_length=200)
    Genre_ID = models.ForeignKey(Quiz_Genre, on_delete=models.SET_NULL, null=True)
    User_ID = models.ForeignKey(User)
    IsActive = models.BooleanField(default=True)
    DateCreated = models.DateTimeField(auto_now_add=True)
    LastModified = models.DateTimeField(auto_now=True)

class Quiz_Question(models.Model):
    Quiz_ID = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    Number = models.IntegerField()
    
class Quiz_Question_Option(models.Model):
    Quiz_Question_ID = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    IsAnswer = models.BooleanField(default=False)

class Quiz_Question_User_Answer(models.Model):
    User_ID = models.ForeignKey(User)
    Quiz_Question_ID = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
    Quiz_Question_Option_ID = models.ForeignKey(Quiz_Question_Option, on_delete=models.CASCADE)
    IsCorrect = models.BooleanField(default=self.Quiz_Question_Option_ID.IsAnswer)

class Quiz_User_Attempt(models.Model):
    User_ID = models.ForeignKey(User)
    Quiz_ID = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Number_Correct = models.IntegerField()
    Time_Taken = models.DurationField()
    DateOfAttempt = models.DateTimeField(auto_now_add=True)

class Quiz_Genre(models.Model):
    Text = models.CharField(max_length=200)

