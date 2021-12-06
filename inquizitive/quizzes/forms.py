from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)


class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields=('Title', 'Genre')
        labels = {
            'Title': ('Title'),
            'Genre': ('Genre')
        }


class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = Quiz_Question
        fields = ('Quiz_ID', 'Text')
        labels = {
            'Text': ('Question'),
        }



class QuizQuestionOptionForm(forms.ModelForm):
    class Meta:
        model = Quiz_Question_Option
        fields = ('Text','IsAnswer')
        labels = {
            'Text': ('Option'),
            'IsAnswer': ('Is Correct Answer')
        }
        widgets = {
            'yes_or_no' : forms.RadioSelect
        }