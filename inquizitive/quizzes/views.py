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


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quizzes/quiz_view.html"


# def attempt_quiz(request, quiz_id):
#     quiz = get_object_or_404(Quiz, pk=quiz_id)
#     try:
#         selected_choice = question.quiz_question_option_set.get(pk=request.POST['choice'])
#     except (KeyError, Quiz_Question_Option.DoesNotExist):
#         # Redisplay the question answering form
#         return render(request, 'quizzes/answer_question.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))