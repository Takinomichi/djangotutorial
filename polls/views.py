from django.http import HttpResponse
# from django.template import loader
# from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Question

# That code loads the template called polls/index.html and passes it a context.
# The context is a dictionary mapping template variable names to Python objects.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # Django provides a shortcut for rendering a template. Just use render() function instead of loader and HttpResponse
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # Do a 404 Error check
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # There is a get_object_or_404 shortcut to make it easier:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question, "question_id": question_id})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)