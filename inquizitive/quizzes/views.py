from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import *

class index(ListView):
    model = Quiz_Genre

class QuizGenreDetailView(DetailView):
    model = Quiz_Genre
    template_name = "quizzes/quiz_genre_view.html"

class QuizCreateView(CreateView):
    model = Quiz
    fields = ('Title', 'Genre')

    def get_success_url(self):
        return reverse('create_question', kwargs={'quiz_id': self.object.id})
    
    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.User_ID = User.objects.get(pk=(self.request.user.pk))
        quiz.save()
        return HttpResponseRedirect(reverse('create_question', args=(quiz.id,)))

class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = "quizzes/confirm_delete.html"

    def get_success_url(self):
        return reverse('index')


QuizQuestionOptionFormset = inlineformset_factory(Quiz_Question, Quiz_Question_Option, form=QuizQuestionOptionForm, extra=4, can_delete=False)

class QuizQuestionCreateView(CreateView):
    model = Quiz_Question
    fields = ('Text',)
  
    def form_valid(self, form):
        self.Quiz_ID = get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        form.instance.User_ID = self.request.user
        form.instance.Quiz_ID = self.Quiz_ID
        form.instance.Number = 1
        form.save()
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # TODO: redirect to QuizQuestionOptionCreateView
        return reverse('view_your_quiz', kwargs={'pk': self.Quiz_ID.id})


class QuizQuestionDetailView(DetailView):
    model = Quiz_Question
    template_name = "quizzes/quiz_question_view.html"


class QuizQuestionDeleteView(DeleteView):
    model = Quiz_Question
    template_name = "quizzes/confirm_delete.html"

    def get_success_url(self):
        return reverse('view_quiz', kwargs={'pk': getattr(self.get_object(), 'Quiz_ID').id})


class QuizQuestionUpdateView(UpdateView):
    model = Quiz_Question
    fields = ('Text',)
    extra_context={'update': True}
  
    def form_valid(self, form):
        self.Quiz_ID = get_object_or_404(Quiz, id=self.kwargs['pk'])
        form.instance.Quiz_ID = self.Quiz_ID
        form.save()
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('view_quiz', kwargs={'pk': self.Quiz_ID.id})


class QuizQuestionOptionCreateView(CreateView):
    model = Quiz_Question_Option
    fields = ('Text', 'IsAnswer')
 
    def form_valid(self, form):
        self.Quiz_Question_ID = get_object_or_404(Quiz_Question, id=self.kwargs['question_id'])
        form.instance.Quiz_Question_ID = self.Quiz_Question_ID
        form.save()
        form.instance.save()

        done = True
        if 'add' in self.request.POST:
            done = False

        return HttpResponseRedirect(self.get_success_url(done))

    def get_success_url(self, done):
        if done:
            return reverse('view_quiz_question', kwargs={'pk': self.Quiz_Question_ID.id})
        else:
            return reverse('add_question_option', kwargs={'question_id': self.Quiz_Question_ID.id})


class QuizQuestionOptionUpdateView(UpdateView):
    model = Quiz_Question_Option
    fields = ('Text', 'IsAnswer')
    extra_context={'update': True}
 
    def form_valid(self, form):
        self.Quiz_Question_ID = get_object_or_404(Quiz_Question, id=getattr(self.get_object(), 'Quiz_Question_ID').id)
        form.instance.Quiz_Question_ID = self.Quiz_Question_ID
        form.save()
        form.instance.save()

        done = True
        if 'add' in self.request.POST:
            done = False

        return HttpResponseRedirect(self.get_success_url(done))

    def get_success_url(self, done):
        if done:
            return reverse('view_quiz_question', kwargs={'pk': self.Quiz_Question_ID.id})
        else:
            return reverse('add_question_option', kwargs={'question_id': self.Quiz_Question_ID.id})


class QuizQuestionOptionDeleteView(DeleteView):
    model = Quiz_Question_Option
    template_name = "quizzes/confirm_delete.html"

    def get_success_url(self):
        return reverse('view_quiz_question', kwargs={'pk': getattr(self.get_object(), 'Quiz_Question_ID').id})
        # return reverse('index')


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quizzes/quiz_view.html"

class UserQuizDetailView(DetailView):
    model = Quiz
    template_name = "quizzes/quiz_user_view.html"


def answer_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    quiz_attempt = Quiz_User_Attempt(User_ID = request.user, Quiz_ID = quiz)

    # get ids of all questions in this quiz
    all_quiz_questions = list(quiz.quiz_question_set.values_list('id', flat=True))

    current_question_index = all_quiz_questions.index(question_id)
    # if we find the question id and it's not the last one
    if(current_question_index and current_question_index < len(all_quiz_questions)-1):
        # get id of next question in this quiz 
        next_question = all_quiz_questions[current_question_index + 1]
    elif(current_question_index == len(all_quiz_questions)-1): 
        next_question = None

    question = get_object_or_404(Quiz_Question, pk=question_id)

    try:
        selected_choice = question.quiz_question_option_set.get(pk=request.POST['option'])
    except (KeyError, Quiz_Question_Option.DoesNotExist):
        # Redisplay the question answering form
        return render(request, 'quizzes/answer_question.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        is_correct = False
        correct_options = question.quiz_question_option_set.filter(IsAnswer=1).values_list('id', flat=True)
        if selected_choice.id in correct_options:
            is_correct = True

        user_answer = Quiz_Question_User_Answer(User_ID = request.User, Quiz_User_Attempt_ID = quiz_attempt, Quiz_Question_ID = question_id, Quiz_Question_Option_ID = selected_choice.id, IsCorrect = is_correct)

        if(next_question):
            return HttpResponseRedirect(reverse('answer_question', args=(quiz_id, next_question,)))
        else:
            # TODO: redirect to a 'quiz results' view which shows how many questions they got right
            #  and maybe even show all the quiz questions, which option they selected and which was the correct option
            return HttpResponseRedirect(reverse('index'))
            