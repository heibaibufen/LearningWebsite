from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import Choice, Question, UserInfo


def index1(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index1.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def kun(request):
    name = 'kunkun'
    import requests
    res = requests.get("https://book.douban.com/subject/36209209/?icn=index-latestbook-subject", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"})
    new = res.text
    print(new)
    return render(request, 'polls/kun.html', {'n': new})


def gpt(request):
    return redirect("https://www.heibaibufen.site/")


def info_list(request):
    data_list = UserInfo.objects.all()

    return render(request, "polls/info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "polls/info_add.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    UserInfo.objects.create(name=user, password=pwd, age=age)
    return redirect("http://127.0.0.1:8000/polls/info/list/")


def index(request):
    return render(request, "polls/index.html")


def login(request):
    if request.method == 'GET':
        return render(request, "polls/login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
    if UserInfo.objects.filter(name=user)[0].password == pwd:
        return redirect("http://127.0.0.1:8000/polls/index/")
    else:
        er = "账号或密码错误"
        return render(request, "polls/login.html", {"n": er})


def register(request):
    if request.method == "GET":
        return render(request, "polls/register.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    UserInfo.objects.create(name=user, password=pwd)
    return redirect("http://127.0.0.1:8000/polls/login/")
