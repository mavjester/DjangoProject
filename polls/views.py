from django.http import HttpResponse

from .models import Question

def index(request):
<<<<<<< HEAD
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
=======
    return HttpResponse("Hello, world. You're at the polls index.")
>>>>>>> features/be/view


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def result(request, question_id):
<<<<<<< HEAD
    response = "You're looking at the results of question %s."
=======
    response = "You're looking at the result of question %s."
>>>>>>> features/be/view
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

<<<<<<< HEAD
=======
#
>>>>>>> features/be/view
