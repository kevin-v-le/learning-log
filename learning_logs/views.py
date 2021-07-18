from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """the home page for learning log"""
    return render(request, 'learning_logs/index.html')

#topics
def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

#def new_topic():
    """form where user can create a new topic"""
