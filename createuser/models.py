from django.db import models

class user_details(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class message(models.Model): 
    authentication = models.CharField(max_length=255)
    boolean = models.BooleanField()

class user_details_quiz(models.Model):
    user = models.ForeignKey(user_details, null=True, on_delete=models.CASCADE)
    username= models.CharField(max_length= 50)
    user_points = models.IntegerField(default=0)
    user_questions_answered = models.IntegerField(default=0)
    user_answer_questions_correct = models.IntegerField(default=0)
    user_answer_questions_incorrect = models.IntegerField(default=0)
