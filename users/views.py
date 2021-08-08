from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """form where new users can register"""
    if request.method != 'POST':
        #no data submitted, process data
        form = UserCreationForm()
    else:
        #POST data submitted, process data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    #display a blank or invalid form
    context = {'register': register}
    return render(request, 'registration/register.html', context)

