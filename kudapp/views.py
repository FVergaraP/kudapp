from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    template = loader.get_template('kudapp/index.html')
    return HttpResponse(template.render())


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('kudapp.views.index')
    else:
        form = UserForm()
    return render(request, 'kudapp/user_edit.html', {'form': form})