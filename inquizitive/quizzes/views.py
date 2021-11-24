from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.forms.models import inlineformset_factory

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

    # def get_context_data(self, **kwargs):
    #     context = super(QuizDetailView, self).get_context_data(**kwargs)
    #     quiz = Quiz.objects.get(id=self.id)
    #     questions = quiz.question_set.all()
    #     context['quiz_questions'] = questions
    #     return context


# def selectview(request):
#    item  = Item.objects.all() # use filter() when you have sth to filter ;)
#    form = request.POST # you seem to misinterpret the use of form from django and POST data. you should take a look at [Django with forms][1]
#    # you can remove the preview assignment (form =request.POST)
#    if request.method == 'POST':
#       selected_item = get_object_or_404(Item, pk=request.POST.get('item_id'))
#       # get the user you want (connect for example) in the var "user"
#       user.item = selected_item
#       user.save()

#       # Then, do a redirect for example

#    return render_to_response ('select/item.html', {'items':item}, context_instance =  RequestContext(request),)