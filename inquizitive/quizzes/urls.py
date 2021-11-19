from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('create_quiz', views.QuizCreateView.as_view(), name='create_quiz'),
    # path('create_quiz', views.create_quiz, name='create_quiz'),

]