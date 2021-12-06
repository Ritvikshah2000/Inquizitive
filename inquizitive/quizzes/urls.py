from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('create_quiz',login_required(views.QuizCreateView.as_view()), name='create_quiz'),
    path('delete_quiz/<int:pk>', views.QuizDeleteView.as_view(), name='delete_quiz'),
    path('view_quiz/<int:pk>', views.QuizDetailView.as_view(), name='view_quiz'),
    path('view_genre/<int:pk>', views.QuizGenreDetailView.as_view(), name='view_genre'),
    path('view_quiz_question/<int:pk>', views.QuizQuestionDetailView.as_view(), name='view_quiz_question'),
    path('delete_quiz_question/<int:pk>', views.QuizQuestionDeleteView.as_view(), name='delete_quiz_question'),
    path('<int:quiz_id>/create_quiz_question', views.QuizQuestionCreateView.as_view(), name='create_question'),
    path('<int:question_id>/add_question_option', views.QuizQuestionOptionCreateView.as_view(), name='add_question_option'),
]
