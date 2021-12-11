from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('create_quiz',login_required(views.QuizCreateView.as_view()), name='create_quiz'),
    # path('create_quiz',views.QuizCreateView.as_view(), name='create_quiz'),
    path('delete_quiz/<int:pk>',login_required(views.QuizDeleteView.as_view()), name='delete_quiz'),
    # path('delete_quiz/<int:pk>', views.QuizDeleteView.as_view(), name='delete_quiz'),
    path('view_quiz/<int:pk>', views.QuizDetailView.as_view(), name='view_quiz'),
    path('view_your_quiz/<int:pk>', login_required(views.UserQuizDetailView.as_view()), name='view_your_quiz'),
    # path('view_your_quiz/<int:pk>', views.UserQuizDetailView.as_view(), name='view_your_quiz'),
    path('view_genre/<int:pk>', views.QuizGenreDetailView.as_view(), name='view_genre'),
    path('view_quiz_question/<int:pk>', views.QuizQuestionDetailView.as_view(), name='view_quiz_question'),
    path('delete_quiz_question/<int:pk>',login_required(views.QuizQuestionDeleteView.as_view()), name='delete_quiz_question'),
    # path('delete_quiz_question/<int:pk>', views.QuizQuestionDeleteView.as_view(), name='delete_quiz_question'),
    path('<int:quiz_id>/create_quiz_question',login_required(views.QuizQuestionCreateView.as_view()), name='create_question'),
    # path('<int:quiz_id>/create_quiz_question', views.QuizQuestionCreateView.as_view(), name='create_question'),
    path('<int:question_id>/add_question_option',login_required(views.QuizQuestionOptionCreateView.as_view()), name='add_question_option'),
    # path('<int:question_id>/add_question_option', views.QuizQuestionOptionCreateView.as_view(), name='add_question_option'),
    path('<int:quiz_id>/answer_question/<int:question_id>', login_required(views.answer_question), name='answer_question'),
    # path('<int:quiz_id>/answer_question/<int:question_id>', views.answer_question, name='answer_question'),
    path('update_question_option/<int:pk>', login_required(views.QuizQuestionOptionUpdateView.as_view()), name='update_question_option'),
    path('delete_question_option/<int:pk>', login_required(views.QuizQuestionOptionDeleteView.as_view()), name='delete_question_option'),

