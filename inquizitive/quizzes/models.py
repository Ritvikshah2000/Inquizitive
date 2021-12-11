from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)

class Quiz_Genre(models.Model):
    Text = models.CharField(max_length=200)
    def __str__(self):
        return self.Text

class Quiz(models.Model):
    Title = models.CharField(max_length=200)
    Genre = models.ForeignKey(Quiz_Genre, on_delete=models.SET_NULL, null=True)
    User_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    IsActive = models.BooleanField(default=True)
    DateCreated = models.DateTimeField(auto_now_add=True)
    LastModified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Title

class Quiz_Question(models.Model):
    Quiz_ID = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    Number = models.IntegerField(null=True)
    def __str__(self):
        return self.Text
    
class Quiz_Question_Option(models.Model):
    Quiz_Question_ID = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    IsAnswer = models.BooleanField(default=False, choices=YES_OR_NO)
    def __str__(self):
        return self.Text

class Quiz_User_Attempt(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Quiz_ID = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Number_Correct = models.IntegerField()
    Time_Taken = models.DurationField()
    DateOfAttempt = models.DateTimeField(auto_now_add=True)

class Quiz_Question_User_Answer(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # link all user answers to a single quiz attempt - in case of multiple attempts of same quiz
    Quiz_User_Attempt_ID = models.ForeignKey(Quiz_User_Attempt, on_delete=models.CASCADE, null=True)
    Quiz_Question_ID = models.ForeignKey(Quiz_Question, on_delete=models.CASCADE, null=True)
    Quiz_Question_Option_ID = models.ForeignKey(Quiz_Question_Option, on_delete=models.CASCADE, null=True)
    IsCorrect = models.BooleanField(default=False)




