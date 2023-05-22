from django.shortcuts import render
from main import models
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


import random 

# Create your views here.
@login_required(login_url='login')
def homepage(request):
    if (request.method == "POST"):
        right = 0
        testid = request.POST['testid'];
        test = models.Test(id = testid)
        test.user = request.user
        test.completed = True

        for i in request.POST:
            if i == "csrfmiddlewaretoken" or i== "testid":
                continue
            #get the question in TestQuestion with questionid = i and testid = testid
            question = models.TestQuestion.objects.get(question_id = i , test_id = testid)
            choices = (request.POST[i]).split(" ")
            question.attempted_option = choices[0]
            question.save()
            if (choices[0]== choices[1]):
                right+=1
        
        test.marks_obtained = right
        test.save()
        questions = models.TestQuestion.objects.filter(test_id = testid)
        choices = []
        for question in questions:
            choices.append(models.Choice.objects.filter(question=question.question))
        context = {
            "questions":zip(questions, choices),
            "test" : test,

        }
        return render(request , "main/result.html", context )
    
    #get all the test by the user 
    temp = models.Test.objects.filter(user = request.user)
    totalTest = len(temp)+1
    if totalTest < 7:
        questions = models.Question.objects.all(level="easy")
    else:
        questions = models.Question.objects.all()
    
    #get random 50 question 
    questions = random.sample(list(questions), 50)
    choices = []
    #create an instance of test 
    new_test = models.Test.objects.create(user=request.user, marks_obtained=0 , completed=False)
    new_test.save()
    for question in questions:
        choices.append(models.Choice.objects.filter(question=question))
        #add question to test 
        models.TestQuestion.objects.create(test=new_test , question = question ).save()
    
    context = {
        "questions":zip(questions, choices),
        "test" : new_test,

    }
    
    

    return render(request, "main/home.html" , context)

@login_required(login_url='login')
def test(request,test_id):
    questions = models.TestQuestion.objects.filter(test_id = test_id)
    temp = models.Question.objects.all()
    for i in temp:
        i.solution = i.solution.replace("Â" , "")
        i.save()
    choices = []
    for question in questions:
        choices.append(models.Choice.objects.filter(question=question.question))
    context = {
        "questions":zip(questions, choices),
        "test" : models.Test.objects.get(id = test_id),

    }
    return render(request, "main/result.html" , context)


@login_required(login_url='login')
def index(request):
    test = models.Test.objects.filter(user = request.user )
    total_test = len(test)
    print(total_test)
    average_marks = 0
    for i in test:
        average_marks += i.marks_obtained
    if total_test != 0:
        average_marks = average_marks/total_test

    context ={
        "tests" : test ,
        "total_test" : total_test,
        "average_marks" : average_marks,
    }
    return render(request, "main/index.html" , context)

@login_required(login_url='login')
def getTest(request , test_id):
    if (request.method == "POST"):
        right = 0
        testid = request.POST['testid'];
        test = models.Test(id = testid)
        test.user = request.user
        test.completed = True

        for i in request.POST:
            if i == "csrfmiddlewaretoken" or i== "testid":
                continue
            #get the question in TestQuestion with questionid = i and testid = testid
            question = models.TestQuestion.objects.get(question_id = i , test_id = testid)
            choices = (request.POST[i]).split(" ")
            question.attempted_option = choices[0]
            question.save()
            if (choices[0]== choices[1]):
                right+=1
        
        test.marks_obtained = right
        test.save()
        questions = models.TestQuestion.objects.filter(test_id = testid)
        choices = []
        for question in questions:
            choices.append(models.Choice.objects.filter(question=question.question))
        context = {
            "questions":zip(questions, choices),
            "test" : test,

        }
        return render(request , "main/result.html", context )
    
    questions = models.TestQuestion.objects.filter(test_id = test_id)
    choices = []
    ques = []
    for question in questions:
        choices.append(models.Choice.objects.filter(question=question.question))
        ques.append(question.question)
    

    context = {
        "questions":zip(ques, choices),
        "test" : models.Test.objects.get(id = test_id),

    }
    return render(request, "main/home.html" , context)

@login_required(login_url='login')
def deleteTest(request , test_id):
    test = models.Test.objects.get(id = test_id)
    test.delete()
    return redirect("index")


def Login(request):
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["passowrd"]
            print(username , password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return render(request, "main/login.html", {"message": "Invalid credentials."})
    return render(request, "main/login.html")

def Logout(request):
    logout(request)
    return redirect("login")
