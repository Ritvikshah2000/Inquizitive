from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    # path('create_quiz',login_required(views.QuizCreateView.as_view()), name='create_quiz'),
    path('create_quiz',views.QuizCreateView.as_view(), name='create_quiz'),
    path('delete_quiz/<int:pk>', views.QuizDeleteView.as_view(), name='delete_quiz'),
    path('view_quiz/<int:pk>', views.QuizDetailView.as_view(), name='view_quiz'),
    path('view_genre/<int:pk>', views.QuizGenreDetailView.as_view(), name='view_genre'),
    path('view_quiz_question/<int:pk>', views.QuizQuestionDetailView.as_view(), name='view_quiz_question'),
    path('delete_quiz_question/<int:pk>', views.QuizQuestionDeleteView.as_view(), name='delete_quiz_question'),
    path('update_quiz_question/<int:pk>', views.QuizQuestionUpdateView.as_view(), name='update_quiz_question'),
    path('create_quiz_question/<int:quiz_id>', views.QuizQuestionCreateView.as_view(), name='create_question'),
    path('add_question_option/<int:question_id>', views.QuizQuestionOptionCreateView.as_view(), name='add_question_option'),
    path('update_question_option/<int:pk>', views.QuizQuestionOptionUpdateView.as_view(), name='update_question_option'),
    path('delete_question_option/<int:pk>', views.QuizQuestionOptionDeleteView.as_view(), name='delete_question_option'),
]
