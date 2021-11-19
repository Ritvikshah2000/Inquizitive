from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView

from .models import *

class index(ListView):
    model = Quiz

class QuizCreateView(CreateView):
    model = Quiz
    fields = ('Title', 'Genre')
    success_url = "/"
    
    

def create_quiz(request):
    genre = Quiz_Genre.objects.all()
    if request.method == 'POST':
        genre = get_object_or_404(Quiz_Genre, pk=request.POST.get('genre_id'))
        formset = QuizForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    else:
        formset = QuizForm()
        return render(request, 'create_quiz.html', {'form': formset})


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