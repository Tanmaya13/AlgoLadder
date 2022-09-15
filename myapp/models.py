
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date
from contest.models import *
from PIL import Image

# Create your models here.

class Track(models.Model):

    name = models.CharField(max_length=200)
    description = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    prerequisites = models.ManyToManyField("self", blank=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.track_name

class Section(models.Model):

    name = models.CharField(max_length=200)
    description = RichTextUploadingField()
    tracks = models.ManyToManyField(Track)
    created_date = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.section_name

class Topic(models.Model):

    name = models.CharField(max_length=200)
    description = RichTextUploadingField()
    sections = models.ManyToManyField(Section)
    created_date = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.topic_name

class University(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.university_name

class Achievement(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    image = models.ImageField(upload_to ='achievements/')

    def __str__(self):
        return self.achievement_name

class Enroll(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    course = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

class Problem(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    content = RichTextUploadingField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    # author = models.ForeignKey(Custom_User,on_delete=models.CASCADE,blank=True, null=True)
    # discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, blank=True, null=True)
    solved_by = models.IntegerField(default=0, blank=True)
    total_submissions = models.IntegerField(default=0, blank=True)
    time_limit = models.FloatField(default=1, blank=True)
    memory_limit = models.IntegerField(default=50000, blank=True)
    points = models.IntegerField(default=100, blank=True)
    # test_cases = models.ManyToManyField(Test_Case, blank=True)
    solution = models.FileField(upload_to='solutions', blank=True, null=True)
    analyse_link = models.TextField(blank =True)
    # note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name




class Custom_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200,default = "fullname")
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    university = models.CharField(max_length=200,blank=True)
    universitystartyear=models.IntegerField(default=0,blank = True)
    universityendyear=models.IntegerField(default=0,blank = True)
    universitycgpa=models.IntegerField(default=0,blank = True)
    points = models.IntegerField(default=0,blank = True)
    achievements = models.ManyToManyField(Achievement,blank=True)
    phone = models.CharField(max_length=13, blank=True)
    current_topic = models.TextField(default = "Array:00000; javasprings:0000; Binary Search Tree:00000; Sorting:00000000; Divide And Conquer:00000; djangoviews:00; pythonflask:; Graph:000; Searching:0000; Mathematical:0000; Pattern Matching:000; flaskrouting:00; ibmbluemix:; Divide And Conquers:00000; flaskmethods:00; pythondjango:; djangomodels:000; djangoforms:00; Dynamic Programming:0000; Stack:000; Binary Tree:0000; firebase:; back Tracking:000; Binary Search Tree:00000; pythonconditions:00; heroku:; s:; Queue:000; Graph Algorithms:000; pythonfunctions:00; Dynamic Programmings:0000; djangodeployment:00; pythondatatypes:0000; pythonoperators:00000000; flasktemplates:00; flaskbasics:00; Hashing:000; Greedy:00000; flaskdeployment:00; pythonloops:00000; Strings:00; csharpdotnet:; awss:; djangobasics:0000; Linked List:0000;STL:0000;",blank=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    # problem_solved = models.ManyToManyField(Problem, blank=True)
    points_earned = models.IntegerField(default=0,blank = True)
    problems_solved = models.ManyToManyField(Problem, blank=True)
    start_date = models.CharField(max_length = 200, default = "No Course Purchased")
    end_date = models.CharField(max_length = 200, default = "No Course Purchased")
    questionsallotted =  RichTextField(null=True,blank=True,default = "No Mentor Allotted ! Mentors allot questions every week for practice according to learning pace of each individual student. Purchase a course to get a mentor assigned to you.")
    scheduledclass =  RichTextField(null=True,blank=True,default = "No One to One Class Scheduled ! Mentors take One-to-One Class of each individual student. Purchase a course to get One to One Classes with mentors.")
    link = models.URLField(max_length = 200,blank=True)
    referral_code =  models.CharField(max_length = 200, default = "Generate Your Coupon Code")
    method_type = models.CharField(default = "Not Purchased" , max_length = 20)
    counter = models.CharField(default ="1-0,2-0,4-0",max_length= 20)
    mentors_alloted = models.ManyToManyField('Mentor_user',blank=True)
    AlgoEdge_enrolled=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if created:
        Custom_User.objects.create(user=instance)
    instance.custom_user.save()


class Faculty_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200,default = "fullname")
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    allotedcontest = models.ManyToManyField(Contests,blank=True)
    def __str__(self):
        return self.fullname


class Groups_learn(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    group_members = models.ManyToManyField(Custom_User,blank=True)
    questionsallotted =  RichTextField(null=True,blank=True,default = "No Questions Allotted ! Mentors allot questions every week for practice according to learning pace of each individual student. Purchase a course to get a mentor assigned to you.")
    link = models.URLField(max_length = 200,blank=True)
    
    def __str__(self):
        return self.name

class Mentor_user(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200,default = "fullname")
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    allotedstudents = models.ManyToManyField(Custom_User,blank=True)
    groupalloted =  models.ManyToManyField(Groups_learn,blank=True)
    course_alloted = models.CharField(max_length=200,default = "no course alloted")
    def __str__(self):
        return self.fullname

class Note(models.Model):


    name = models.CharField(max_length=200)
    content = RichTextUploadingField(null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(Custom_User, on_delete=models.CASCADE, blank=True,null=True)
    pathname = models.CharField(max_length=200,default="")
    thumbnail = models.ImageField(upload_to ='thumbnail/',null=True,blank=True)
    label = models.CharField(max_length=200, default="no_label")



    def __str__(self):
        return self.name

# class Tag(models.Model):
#
#     tag_name = models.CharField(max_length=200)

# class Discussion(models.Model):
#
#     discussion_name = models.CharField(max_length=200)
#     discussion_content = models.TextField()
#     discussion_created_date = models.DateTimeField(default=timezone.now)
#     discussion_tags = models.ManyToManyField(Tag)
#     discussion_code = models.CharField(max_length=10)
#     discussion_author = models.ForeignKey(Custom_User,on_delete=models.CASCADE)
#     discussion_votes = models.IntegerField()
#
#     DISCUSSION_FLAG_CHOICES = (
#
#         ("Normal", "Normal"),
#         ("Important", "Important"),
#         ("Spam", "Spam"),
#     )
#
#     discussion_flag = DISCUSSION_FLAG_CHOICES
#
#     def __str__(self):
#         return self.discussion_name

# class Comment(models.Model):
#
#     comment_content = models.TextField()
#     comment_created_date = models.DateTimeField(default=timezone.now)
#     comment_author = models.ForeignKey(Custom_User,on_delete=models.CASCADE)
#     comment_discussion = models.ForeignKey(Discussion,on_delete=models.CASCADE)
#     comment_reply = models.ForeignKey("self",blank=True,on_delete=models.CASCADE)
#
#     COMMENT_FLAG_CHOICES = (
#
#         ("Normal", "Normal"),
#         ("Important", "Important"),
#         ("Spam", "Spam"),
#     )
#
#     comment_flag = COMMENT_FLAG_CHOICES
#
#     def __str__(self):
#         return self.comment_info

# class Test_Case(models.Model):
#
#     name = models.CharField(max_length=200, default="test_case_no")
#     input = models.FileField(upload_to='problems/', default=None)
#     output = models.FileField(upload_to='problems/', default=None)
#
#     def __str__(self):
#         return self.name





class Activity(models.Model):

    user = models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    submit_time = models.DateTimeField(default=timezone.now)
    points = models.IntegerField()

class Leaderboard(models.Model):

    activity = models.ManyToManyField(Activity)

class Contest(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    description = RichTextUploadingField(null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    hosted_by = models.CharField(max_length = 200, default="AlgoLadder")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    problems = models.ManyToManyField(Problem, blank = True)
    leaderboard = models.OneToOneField(Leaderboard,on_delete=models.CASCADE,blank = True, null=True)

class Post(models.Model):

    content = RichTextField()
    content_img = RichTextUploadingField(null=True,blank=True)


class InterviewExperiences(models.Model):

    name = models.CharField(max_length=500)
    content = RichTextUploadingField(null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=500)
    linkofauthor = models.CharField(max_length=200,default="")
    companyname= models.CharField(max_length=500, blank=True)
    logo = models.ImageField(default='default.jpg', upload_to='interview_pics/')
    def __str__(self):
        return self.name

class Blogs(models.Model):

    name = models.CharField(max_length=500)
    content = RichTextUploadingField(null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=500)
    linkofauthor = models.CharField(max_length=200,default="")
    logo = models.ImageField(default='default.jpg', upload_to='blogs_pics/')
    def __str__(self):
        return self.name



class Ambassador(models.Model):
    name = models.CharField(max_length=500)
    college_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    code = models
    
    def __str__(self):
        return self.name

class AmbassadorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200,default = "fullname")
    email = models.EmailField(max_length=254,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    allotedstudents = models.ManyToManyField(Custom_User,blank=True)
    college_name = models.CharField(max_length=500)
    phone = models.CharField(max_length=13)
    code = models.CharField(max_length=200, unique=True)
    studentCount = models.CharField(max_length=500, default="0")

    
    def __str__(self):
        return self.fullname

class FreeTrial(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    interest = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name



class Courses(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(Custom_User, on_delete=models.CASCADE, blank=True,null=True)
    #pathname = models.CharField(max_length=200,default="")
    summary = models.TextField(blank=True)
    videolink = models.URLField(max_length = 200,blank=True)
    courselink = models.URLField(max_length = 200,blank=True)
    topiccovered = models.TextField(blank=True)
    faqquestion = models.TextField(blank=True)
    faqanswer = models.TextField(blank=True)
    description = RichTextUploadingField()
    instructors = models.CharField(max_length=500)
    price= models.IntegerField(default=0)
    notesincourse = models.ManyToManyField(Note, blank=True)
    enrolledusers = models.ManyToManyField(Custom_User, blank = True)
    date1 = models.DateField(default=date.today, blank = True)
    seat1 = models.IntegerField(default=10, blank = True)
    date2 = models.DateField(default=date.today, blank = True)
    seat2 = models.IntegerField(default=10, blank = True)
    date3 = models.DateField(default=date.today, blank = True)
    seat3 = models.IntegerField(default=10, blank = True)
    date4 = models.DateField(default=date.today, blank = True)
    seat4 = models.IntegerField(default=10, blank = True)
    group_date1 = models.DateField(default=date.today, blank = True)
    group_seat1 = models.IntegerField(default=10, blank = True)
    group_date2 = models.DateField(default=date.today, blank = True)
    group_seat2 = models.IntegerField(default=10, blank = True)
    group_price= models.IntegerField(default=0)
    logo = models.ImageField(upload_to ='thumbnail/',blank=True)
    content = models.TextField(blank=True)
    structure = models.TextField(blank=True)
    def __str__(self):
        return self.name



class CouponCode(models.Model):
    name = models.CharField(max_length=500)
    discount = models.IntegerField(default=0)
    assignedto = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.name


class Mentor_Lead(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.IntegerField( blank=True)
    availability = models.TextField(blank =True)
    subject = models.CharField(max_length=200, blank=True)
    achievements = models.TextField(blank =True)
    resume = models.FileField(upload_to='resume/',default=None, blank=True)

    def __str__(self):
        return self.name

class Time_Slot(models.Model):
    from_time = models.TimeField()
    mentor = models.ManyToManyField(Mentor_user,blank=True)

    def __str__(self):
        y = self.from_time
        y = str(y)
        return y

YEAR_CHOICES = (
    ("1st year", "1st year"),
    ("2nd year", "2nd year"),
    ("3rd year", "3rd year"),
    ("4th year", "4th year"),
     
)
class AlgoEdge(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    college_name = models.CharField(max_length=500)
    Resume = models.FileField(upload_to='resume/',default=None, blank=True)
    phone = models.CharField(max_length=500)
    Year = models.CharField(
        max_length = 20,
        choices = YEAR_CHOICES,
        default = '1'
        )
    def __str__(self):
        return str(self.first_name) + "-" + str(self.phone)

class ask_doubt(models.Model):	
    user_name=models.CharField(max_length=200)	
    doubt=models.CharField(max_length=2000)	
    def __self__(self):	
        return self.user_name

 


