from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class CreateQuizForm(ModelForm):
#     class Meta:
#         model=Quiz
#         fields="__all__"


class QuizQuestionForm(forms.Form):
    class Meta:
        model = Quiz_Question
        fields = ('Quiz_ID', 'Text')


YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)

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