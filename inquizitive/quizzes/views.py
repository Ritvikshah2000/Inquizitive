from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required


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
        form.instance.Quiz_ID = self.Quiz_ID
        form.save()
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('view_quiz', kwargs={'pk': self.Quiz_ID.id})


class QuizQuestionDetailView(DetailView):
    model = Quiz_Question
    template_name = "quizzes/quiz_question_view.html"


class QuizQuestionDeleteView(DeleteView):
    model = Quiz_Question
    template_name = "quizzes/confirm_delete.html"

    # TODO: Set up redirect to quiz instead of index
    # def form_valid(self, form):
    #     self.Quiz_ID = get_object_or_404(Quiz, id=self.kwargs['object'].kwargs['quiz_id'])
    #     form.instance.Quiz_ID = self.Quiz_ID
    #     form.save()
    #     form.instance.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('view_quiz', kwargs={'pk': self.Quiz_ID.id})
        return reverse('index')

class QuizQuestionOptionCreateView(CreateView):
    model = Quiz_Question_Option
    fields = ('Text', 'IsAnswer')
 
    def form_valid(self, form):
        self.Quiz_Question_ID = get_object_or_404(Quiz_Question, id=self.kwargs['question_id'])
        form.instance.Quiz_Question_ID = self.Quiz_Question_ID
        form.save()
        form.instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('view_quiz_question', kwargs={'pk': self.Quiz_Question_ID.id})


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quizzes/quiz_view.html"

