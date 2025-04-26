from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# These are the function-based views
# That code loads the template called polls/index.html and passes it a context.
# The context is a dictionary mapping template variable names to Python objects.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     # Django provides a shortcut for rendering a template. Just use render() function instead of loader and HttpResponse
#     # template = loader.get_template("polls/index.html")
#     # return HttpResponse(template.render(context, request))
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     # Do a 404 Error check
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # There is a get_object_or_404 shortcut to make it easier:
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question": question,
#         "question_id": question_id,
#     } 
#     return render(request, "polls/detail.html", context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


# Class-based view for the index page.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by("-pub_date")[:5]

# Class-based view for the detail page.
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# Class-based view for the results page.
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    # Get the question object
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Get the choice object from the form data
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message
        return render( 
            request, "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",    
            },
        )
    else:
        # the F() function is used to directly access the database field without having to do it through the model instance.
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # The reverse() function is a shortcut to avoid hardcoding a URL in the view.
        # It takes a view name and returns a URL matching that view.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))