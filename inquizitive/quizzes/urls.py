from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('create_quiz', views.QuizCreateView.as_view(), name='create_quiz'),
    path('view_quiz/<int:pk>', views.QuizDetailView.as_view(), name='view_quiz'),
    path('view_genre/<int:pk>', views.QuizGenreDetailView.as_view(), name='view_genre'),
    path('view_quiz_question/<int:pk>', views.QuizQuestionDetailView.as_view(), name='view_quiz_question'),
    path('<int:quiz_id>/create_quiz_qestion', views.QuizQuestionCreateView.as_view(), name='create_question'),
    path('<int:question_id>/add_question_option', views.QuizQuestionOptionCreateView.as_view(), name='add_question_option'),
    # path('create_quiz', views.create_quiz, name='create_quiz'),

]