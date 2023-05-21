from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=5000)
    correct_option = models.CharField(max_length=5000)
    topic = models.CharField(max_length=5000)
    solution = models.TextField()
    level = models.CharField(max_length=5000)
    subject  = models.CharField(max_length=5000)

    def __str__(self):
        return self.topic + " "+self.question_text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=5000)
    choice_label = models.CharField(max_length=5000)
    def __str__(self):
        return self.question.topic + " "+ self.question.question_text[:50] + " " + self.choice_text[:50]

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests')
    marks_obtained = models.IntegerField( )
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True , null= True )
    
    

    def __str__(self):
        return str(self.id) + " " + str(self.date)


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='tests')
    attempted_option = models.CharField(max_length=5000 , null=True,default="Not Attempted")

    def __str__(self):
        return str(self.test) + " " + str(self.question) 