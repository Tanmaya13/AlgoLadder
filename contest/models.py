from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contest_name = models.CharField(max_length=100, blank=True)
    score = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True, null=True)
    penalty_time = models.BigIntegerField(default=0)

    def __str__(self):
        return self.user.username





class CodingProblems(models.Model):
    name = models.CharField(max_length=200)
    question = RichTextUploadingField(null=True, blank=True)
    total_submissions = models.IntegerField(default=0, blank=True)
    time_limit = models.FloatField(default=1, blank=True)
    memory_limit = models.IntegerField(default=50000, blank=True)
    points = models.IntegerField(default=100, blank=True)
    editorial = models.FileField(upload_to='solutions', blank=True, null=True)


    def __str__(self):
        return self.name



class McqProblems(models.Model):
    question = RichTextUploadingField(null=True, blank=True)
    optiona = models.TextField(max_length=100)
    optionb = models.TextField(max_length=100)
    optionc = models.TextField(max_length=100)
    optiond = models.TextField(max_length=100)
    correct_ans = models.IntegerField(default=0)


class McqSubmissions(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(McqProblems, on_delete=models.CASCADE)
    submitted_output = models.IntegerField(default=0)
    result = models.BooleanField(default=None, null=True)




class Contests(models.Model):
    participants = models.ManyToManyField(UserProfile, blank=True)
    name = models.CharField(max_length = 1000)
    contest_link = models.CharField(max_length = 1000)
    overview = RichTextUploadingField(null=True, blank=True)
    start_on = models.DateTimeField(default=timezone.now, blank=True)
    end_on = models.DateTimeField(default=timezone.now, blank=True)
    coding_problems = models.ManyToManyField(CodingProblems, blank=True)
    mcq_problems = models.ManyToManyField(McqProblems, blank=True)
    image_link =  models.CharField(max_length = 1000,default= "/static/newtheme/img/test.jpeg" ,blank = True) 
    ACTIVE = 'A'
    PAST = 'P'
    UPCOMING = 'U'
    STATUS = [(ACTIVE, 'Active'), (PAST, 'Past'), (UPCOMING, 'Upcoming')]
    status = models.CharField(max_length=1, choices=STATUS, default=ACTIVE)
    leaderboard = models.BooleanField(default=True)
    runcode = models.BooleanField(default =True)
    #check = models.CharField(max_length=100, default = 'Public')
    contraint = models.CharField(max_length= 200, blank= True) 

    def __str__(self):
        return self.name
    
class LeaderBoard(models.Model):
    name = models.CharField(max_length=100, blank=True)
    participant = models.TextField(null=True)
    score = models.TextField(null = True)



class CodingSubmissions(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(CodingProblems, on_delete=models.CASCADE)
    submitted_output = models.TextField(default="")
    contest = models.ForeignKey(Contests, on_delete = models.CASCADE)
    marks_obtained = models.FloatField(default = 0 )
    result = models.CharField(max_length = 1000, null=True)
