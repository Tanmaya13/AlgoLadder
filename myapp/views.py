from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponse, HttpResponseRedirect
import sys
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.html import strip_tags
from django.http import JsonResponse


from django.core.mail import send_mail

from .models import *
import json
import os
import subprocess
import datetime
from datetime import datetime as dt
from datetime import  timedelta,date,timezone
import calendar
import random
from time import perf_counter

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from myapp.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, phoneUpdateForm
from django.contrib import messages
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from glob import glob
from localStoragePy import localStoragePy
from contest.models import *
import razorpay

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
razorpay_client = razorpay.Client(auth=("rzp_live_M5Nipb7kgTzycb", "mLKgSD5CTOZb9leo46dJQNSS"))
localStorage = localStoragePy('')
# localStorage.setItem("type", "")
# login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
datastructure = ['Array','Linked List','Stack','Queue','Binary Tree','Binary Search Tree','Strings','Graph','Hashing','STL']
datastructure_temp = ['Array','Linked List','Stack','Queue','Binary Tree','BST','Strings','Graph','Hashing','STL']
algorithm = ['Searching','Sorting','Mathematical','Greedy','Dynamic Programmings','Divide And Conquers','back Tracking','Graph Algorithms','Pattern Matching'] 
algorithm_temp = ['Searching','Sorting','Mathematical','Greedy','DP','Div & Con','Back Track','Graph Algo','Pattern Match'] 
python_list = ['pythondatatypes','pythonoperators','pythonconditions','pythonloops','pythonfunctions']
python_list_temp = ['Data Types', 'Operators', 'Conditions','Loops','Functions']
flask_list = ['flaskbasics','flaskrouting','flaskmethods','flasktemplates','flaskdeployment']
flask_list_temp = ['Bascis','Routing','Methods','Templates','Deployment']
django_list = ['djangobasics','djangoviews','djangomodels','djangoforms','djangodeployment']
django_list_temp = ['Basics','Views','Models','Forms','Deployment']
ml_list = ['djangobasics','djangoviews','djangomodels']
ml_list_temp = ['Basics','Supervised','Non-Supervised']

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

    

# class Get_NoteAPI(APIView):
#
#     authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
#
#     def post(self, request, *args, **kwargs):
#
#         response = {}
#         response["status"] = 500
#
#         try:
#             data = request.data
#             note_pathname = data["note_pathname"]
#
#             try:
#                 note = Note.objects.get(pathname=note_pathname)
#                 response['name'] = note.name
#                 response['content'] = note.content
#                 response['result'] = 1
#             except:
#                 response["result"] = 0
#
#             response['status'] = 200
#
#         except Exception as e:
#             print("ERROR ", str(e))
#
#         return Response(data=response)
#
#
# Get_Note = Get_NoteAPI.as_view()


# class Get_All_NotesAPI(APIView):
#
#     authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
#
#     def post(self, request, *args, **kwargs):
#
#         response = {}
#         response["status"] = 500
#
#         try:
#             temp_list = []
#
#             for note in Note.objects.all():
#
#                 temp_dict = {}
#
#                 temp_dict['name'] = note.name
#                 temp_dict['pathname'] = note.pathname
#
#                 if(note.thumbnail):
#                     temp_dict['thumbnail'] = note.thumbnail
#
#                 temp_list.append(temp_dict)
#
#             response['notes'] = temp_list
#
#             response['status'] = 200
#
#         except Exception as e:
#             print("ERROR ", str(e))
#
#         return Response(data=response)
#
#
# Get_All_Notes = Get_All_NotesAPI.as_view()


# class Get_Domain_Problems_ListAPI(APIView):
#
#     authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
#
#     def post(self, request, *args, **kwargs):
#
#         response = {}
#         response["status"] = 500
#
#         try:
#             data = request.data
#             note_pathname = data['note_pathname']
#
#             try:
#                 note = Note.objects.get(pathname=note_pathname)
#                 temp_list = []
#
#                 for problem in Problem.objects.filter(note=note):
#
#                     temp_dict = {}
#
#                     temp_dict['name'] = problem.name
#                     temp_dict['code'] = problem.code
#                     temp_dict['solved_by'] = problem.solved_by
#
#                     temp_list.append(temp_dict)
#
#                 response['problems'] = temp_list
#                 response['result'] = 1
#
#             except Exception as e:
#                 print("ERROR ", str(e))
#                 response['result'] = 0
#
#             response['status'] = 200
#
#         except Exception as e:
#             print("ERROR ", str(e))
#
#         return Response(data=response)
#
#
# Get_Domain_Problems_List = Get_Domain_Problems_ListAPI.as_view()


# class Get_ProblemsAPI(APIView):
#
#     authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
#
#     def post(self, request, *args, **kwargs):
#
#         response = {}
#         response["status"] = 500
#
#         try:
#             data = request.data
#             problem_name = data["problem_name"]
#
#             try:
#                 problem = Problem.objects.get(code=problem_name)
#                 response['name'] = problem.name
#                 response['content'] = problem.content
#                 response['result'] = 1
#             except:
#                 response["result"] = 0
#
#             response['status'] = 200
#
#         except Exception as e:
#             print("ERROR ", str(e))
#
#         return Response(data=response)
#
# Get_Problems = Get_ProblemsAPI.as_view()

# @login_required(login_url='/login')
# def linkedlist(request):
#     return render(request,'linkedlist.html')
#
# @login_required(login_url='/login')
# def linkedlistquestions(request):
#     return render(request,'linkedlistquestions.html')



# def Problems(request,note_name,problem_name):
#     return render(request,'problems.html')


def About_Us(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    return render(request,'about-us.html')

# def Notes(request,note_name):
#     return render(request,'notes.html')
#
# def Problems(request,note_name,problem_name):
#     return render(request,'problems.html')

# def Problems_List(request,note_name):
#
#     try:
#         note = Note.objects.get(pathname=note_name)
#         problems = Problem.objects.filter(note=note)
#
#     except Note.DoesNotExist:
#         raise Http404("Note does not exist")
#
#     return render(request, 'problems_list.html', {'problems': problems })







@login_required(login_url='/accounts/login/')
def Profile(request, username):
    
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    return render(request,'Profile.html')

# def activate(request, uidb64, token):
#     try:
#         uid = uidb64
#         user = Custom_User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('/dashboard')
#     else:
#         return HttpResponse('Activation link is invalid!')

# class Signup_SubmitAPI(APIView):
#
#     authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
#
#     def post(self, request, *args, **kwargs):
#
#         response = {}
#         response["status"] = 500
#
#         try:
#
#             data = request.data
#             response['result'] = 0
#
#             if(len(Custom_User.objects.filter(username=data['username'])) == 0):
#                 try:
#
#                     user = Custom_User.objects.create(username=data['username'],password=data['password'],email=data['email'],phone=data['phone'],university=data['university'])
#                     user.is_active = False
#                     user.save()
#
#                     current_site = get_current_site(request)
#                     mail_subject = 'Activate your CoInterview account.'
#
#                     message = render_to_string('acc_active_email.html', {
#                         'user': user,
#                         'domain': current_site.domain,
#                         'uid': str(user.pk),
#                         'token':account_activation_token.make_token(user),
#                     })
#
#                     email = EmailMessage(mail_subject, message, to=[str(data['email'])])
#                     try:
#                         email.send()
#                     except Exception as e:
#                         print("ERROR ", str(e))
#
#                     response['result'] = 1
#
#                 except Exception as e:
#                     print("ERROR ", str(e))
#                     response['result'] = 0
#
#             response['status'] = 200
#
#         except Exception as e:
#             print("ERROR ", str(e))
#
#         return Response(data=response)
#
# Signup_Submit = Signup_SubmitAPI.as_view()

# class Login_SubmitAPI(APIView):
#
#     authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
#
#     def post(self, request, *args, **kwargs):
#
#         response = {}
#         response["status"] = 500
#
#         try:
#             data = request.data
#
#             try:
#                 user = authenticate(username=data['username'], password=data['password'])
#
#                 print(data['username'])
#                 print(data['password'])
#
#                 if(user.is_active == True):
#                     login(request, user)
#                     response['result'] = "Welcome " + data['username'] + "!"
#                     print("USER IS ACTIVE")
#                 else:
#                     print("USER IS NOT ACTIVE")
#
#             except Exception as e:
#                 response['result'] = 0
#
#             response['status'] = 200
#
#         except Exception as e:
#             print("ERROR ", str(e))
#
#         return Response(data=response)
#
# Login_Submit = Login_SubmitAPI.as_view()

class Get_ProfileAPI(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)

    def post(self, request, *args, **kwargs):

        response = {}
        response["status"] = 500

        try:
            data = request.data

            try:
                user = Custom_User.objects.get(username=data['username'])

                response['profile_username'] = user.username
                response['profile_university'] = user.university
                response['profile_email'] = user.email
                response['profile_contact'] = user.phone
                response['university_start_year'] = user.universitystartyear
                response['university_end_year'] = user.universityendyear
                response['university_name'] = user.university
                response['university_cgpa'] = user.universitycgpa

                temp_list = []

                for activity in Activity.objects.filter(user=user.username):

                    temp_dict = {}

                    temp_dict['problem_code'] = activity.problem.code
                    temp_dict['problem_name'] = activity.problem.name
                    temp_dict['points'] = activity.points
                    temp_dict['submit_time'] = activity.submit_time

                    temp_list.append(temp_dict)

                response['activity'] = temp_list
                response['result'] = 1

            except Exception as e:
                print("ERROR IS ", str(e))
                response['result'] = 0
                pass

            response['status'] = 200

        except Exception as e:
            print("PROFILEAPI ERROR ", str(e))

        return Response(data=response)

Get_Profile = Get_ProfileAPI.as_view()

TIME_LIMIT = 5
TIME_MULTIPLIER_PYTHON3 = 2
TIME_MULTIPLIER_CPP = 1
TIME_MULTIPLIER_C = 1
TIME_MULTIPLIER_JAVA = 2

class Submit_CodeAPI(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500

        try:
            data = request.data
            username = request.user.username
            response = {}

            response["time_excecution"] = ""
            response["output"]="before filepath"
            filepath = "files/ide/"+username
            filepath_input = filepath+"/input.txt"
            filepath_output = filepath+"/output.txt"
            stream = "< "+filepath_input+" > "+filepath_output
            response["output"]="above any function"
            f = open(filepath_input, "w")
            f.write(data["input"])
            f.close()

            if(data["language"] == "cpp"):
                response["output"]="inside cpp"
                filepath_compile = filepath+"/file.cpp"
                filepath_exceution = filepath+"/file.out"

                f = open(filepath_compile, "w")
                f.write(data["code"])
                f.close()

                result = subprocess.Popen("g++ "+filepath_compile+" -o "+filepath_exceution, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output = ""

                if result.wait() != 0:
                    output1, error = result.communicate()
                    output = error.decode('utf8').encode('ascii', errors='ignore')
                    response["output"] = output
                else:
                    result = subprocess.Popen("timeout "+str(TIME_LIMIT*TIME_MULTIPLIER_CPP)+" "+filepath_exceution+" "+stream+" -l --kill-after "+str(TIME_LIMIT*TIME_MULTIPLIER_CPP+1), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                    if result.wait() != 0:
                        output1, error = result.communicate()
                        output = error.decode('utf8').encode('ascii', errors='ignore')
                        if(len(output) == 0):
                            output = "SIGTSTP"
                        response["output"] = output

                    else:
                        result = subprocess.Popen(filepath_exceution + " " + stream, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                        if result.wait() != 0:
                            output1, error = result.communicate()
                            output = error.decode('utf8').encode('ascii', errors='ignore')
                            response["output"] = output
                        else:
                            t_start = perf_counter()
                            os.system(filepath_exceution + " " + stream)
                            t_end = perf_counter()

                            f = open(filepath_output, "r")
                            response["output"] = str(f.read())
                            f.close()

                            response["time_excecution"] += "Excecution Time: " + str(round(t_end - t_start,5))+"s"

            elif(data["language"] == "c"):

                filepath_compile = filepath+"/file.c"
                filepath_exceution = filepath+"/file.out"

                f = open(filepath_compile, "w")
                f.write(data["code"])
                f.close()

                result = subprocess.Popen("gcc "+filepath_compile+" -o "+filepath_exceution, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output = ""

                if result.wait() != 0:
                    output1, error = result.communicate()
                    output = error.decode('utf8').encode('ascii', errors='ignore')
                    response["output"] = output
                else:
                    result = subprocess.Popen("timeout "+str(TIME_LIMIT*TIME_MULTIPLIER_CPP)+" "+filepath_exceution+" "+stream+" -l --kill-after "+str(TIME_LIMIT*TIME_MULTIPLIER_CPP+1), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                    if result.wait() != 0:
                        output1, error = result.communicate()
                        output = error.decode('utf8').encode('ascii', errors='ignore')
                        if(len(output) == 0):
                            output = "SIGTSTP"
                        response["output"] = output

                    else:
                        result = subprocess.Popen(filepath_exceution + " " + stream, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                        if result.wait() != 0:
                            output1, error = result.communicate()
                            output = error.decode('utf8').encode('ascii', errors='ignore')
                            response["output"] = output
                        else:
                            t_start = perf_counter()
                            os.system(filepath_exceution + " " + stream)
                            t_end = perf_counter()

                            f = open(filepath_output, "r")
                            response["output"] = str(f.read())
                            f.close()

                            response["time_excecution"] = "Excecution Time: " + str(round(t_end - t_start,5))+"s"

            elif(data["language"] == "python3"):

                f = open("a.py", "w")
                f.write(data["code"])
                f.close()

                result = subprocess.Popen("timeout "+str(TIME_LIMIT*TIME_MULTIPLIER_PYTHON3)+" python3 a.py -l --kill-after "+str(TIME_LIMIT*TIME_MULTIPLIER_PYTHON3+1), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                if result.wait() != 0:
                    output1, error = result.communicate()
                    output = error.decode('utf8').encode('ascii', errors='ignore')
                    if(len(output) == 0):
                        output = "SIGTSTP"
                    response["output"] = output

                else:
                    result = subprocess.Popen("python3 a.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                    if result.wait() != 0:
                        output1, error = result.communicate()
                        output = error.decode('utf8').encode('ascii', errors='ignore')
                        response["output"] = output
                    else:
                        t_start = perf_counter()
                        response["output"] = subprocess.check_output("python3 a.py", shell=True)
                        t_end = perf_counter()
                        response["time_excecution"] = "Excecution Time: " + str(round(t_end - t_start,5))+"s"

            elif(data["language"]=="java"):

                f = open("a.java", "w")
                f.write(data["code"])
                f.close()

                result = subprocess.Popen("javac a.java", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output = ""

                if result.wait() != 0:
                    output1, error = result.communicate()
                    output = error.decode('utf8').encode('ascii', errors='ignore')
                    response["output"] = output
                else:

                    result = subprocess.Popen("timeout "+str(TIME_LIMIT*TIME_MULTIPLIER_JAVA)+" java a -l --kill-after "+str(TIME_LIMIT*TIME_MULTIPLIER_JAVA+1), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                    if result.wait() != 0:
                        output1, error = result.communicate()
                        output = error.decode('utf8').encode('ascii', errors='ignore')
                        if(len(output) == 0):
                            output = "SIGTSTP"
                        response["output"] = output

                    else:
                        result = subprocess.Popen("java a", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                        if result.wait() != 0:
                            output1, error = result.communicate()
                            output = error.decode('utf8').encode('ascii', errors='ignore')
                            response["output"] = output
                        else:
                            t_start = perf_counter()
                            output = subprocess.check_output("java a", shell=True)
                            t_end = perf_counter()
                            response["output"] = output
                            response["time_excecution"] = "Excecution Time: " + str(round(t_end - t_start,5))+"s"


        except Exception as e:
            print("Error Submit_CodeAPI", str(e))

        return Response(data=response)

Submit_Code = Submit_CodeAPI.as_view()

class Submit_Code_ProblemAPI(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500

        try:
            data = request.data
            username = request.user.username
            response = {}

            temp_list = []

            filepath = "files/ide/"+username

            problem = Problem.objects.get(code=data['problem_code'])
            points = problem.points
            contest_code = data['contest_code']
            time_limit_problem = problem.time_limit
            test_case_no = 0
            AC_COUNT = 0

            TLE = "Time Limit Exceeded"
            RUNTIME_ERROR = "Runtime Error"
            COMPILATION_ERROR = "Compilation Error"

            for test_case in problem.test_cases.all():

                temp_dict = {}
                temp_dict["time_excecution"]  = ""
                temp_dict["verdict"]  = ""

                filepath_input = test_case.input.path
                filepath_output = filepath+"/output.txt"
                stream = "< "+filepath_input+" > "+filepath_output
                expected_output = test_case.output.path

                if(data["language"] == "cpp"):

                    filepath_compile = filepath+"/file.cpp"
                    filepath_exceution = filepath+"/file.out"

                    f = open(filepath_compile, "w")
                    f.write(data["code"])
                    f.close()

                    result = subprocess.Popen("g++ "+filepath_compile+" -o "+filepath_exceution, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    output = ""

                    if result.wait() != 0:
                        output1, error = result.communicate()
                        output = error.decode('utf8').encode('ascii', errors='ignore')
                        temp_dict["verdict"] = COMPILATION_ERROR
                    else:
                        result = subprocess.Popen("timeout "+str(time_limit_problem*TIME_MULTIPLIER_CPP)+" "+filepath_exceution+" "+stream+" -l --kill-after "+str(time_limit_problem*TIME_MULTIPLIER_CPP+1), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                        if result.wait() != 0:
                            output1, error = result.communicate()
                            output = error.decode('utf8').encode('ascii', errors='ignore')
                            if(len(output) == 0):
                                temp_dict["verdict"] = TLE
                            else:
                                temp_dict["verdict"] = RUNTIME_ERROR

                        else:
                            result = subprocess.Popen(filepath_exceution + " " + stream, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                            if result.wait() != 0:
                                output1, error = result.communicate()
                                output = error.decode('utf8').encode('ascii', errors='ignore')
                                temp_dict["verdict"] = RUNTIME_ERROR
                            else:
                                t_start = perf_counter()
                                os.system(filepath_exceution + " " + stream)
                                t_end = perf_counter()

                                temp_dict["time_excecution"] = "Excecution Time: " + str(round(t_end - t_start,5))+"s"

                elif(data["language"] == "c"):

                    filepath_compile = filepath+"/file.c"
                    filepath_exceution = filepath+"/file.out"

                    f = open(filepath_compile, "w")
                    f.write(data["code"])
                    f.close()

                    result = subprocess.Popen("gcc "+filepath_compile+" -o "+filepath_exceution, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    output = ""

                    if result.wait() != 0:
                        output1, error = result.communicate()
                        output = error.decode('utf8').encode('ascii', errors='ignore')
                        temp_dict["verdict"] = COMPILATION_ERROR
                    else:
                        result = subprocess.Popen("timeout "+str(time_limit_problem*TIME_MULTIPLIER_C)+" "+filepath_exceution+" "+stream+" -l --kill-after "+str(time_limit_problem*TIME_MULTIPLIER_C+1), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                        if result.wait() != 0:
                            output1, error = result.communicate()
                            output = error.decode('utf8').encode('ascii', errors='ignore')
                            if(len(output) == 0):
                                temp_dict["verdict"] = TLE
                            else:
                                temp_dict["verdict"] = RUNTIME_ERROR
                        else:
                            result = subprocess.Popen(filepath_exceution + " " + stream, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                            if result.wait() != 0:
                                output1, error = result.communicate()
                                output = error.decode('utf8').encode('ascii', errors='ignore')
                                temp_dict["verdict"] = RUNTIME_ERROR
                            else:
                                t_start = perf_counter()
                                os.system(filepath_exceution + " " + stream)
                                t_end = perf_counter()

                                temp_dict["time_excecution"] = "Excecution Time: " + str(round(t_end - t_start,5))+"s"

                if(temp_dict['verdict'] == ""):

                    f_user = open(filepath_output, "r")
                    whole_user = f_user.read()
                    f_user.close()

                    whole_user = whole_user.rstrip()
                    whole_user = whole_user.split("\n")

                    f_expected = open(expected_output, "r")
                    whole_expected = f_expected.read()
                    f_expected.close()

                    whole_expected = whole_expected.rstrip()
                    whole_expected = whole_expected.split("\n")

                    if(len(whole_user) != len(whole_expected)):
                        temp_dict["verdict"] = "WA"
                    else:
                        for i in range(len(whole_user)):

                            line_user = whole_user[i].rstrip()
                            line_expected = whole_expected[i].rstrip()

                            if(line_user != line_expected):
                               temp_dict["verdict"] = "WA"
                               break

                        if(temp_dict["verdict"] == ""):
                            temp_dict["verdict"] = "AC"

                temp_list.append(temp_dict)

            response['result'] = temp_list
            print(temp_list)

            activity = Activity.objects.create(user=username,problem=problem,points=(points/(len(problem.test_cases.all())))*AC_COUNT)

            if(contest_code != ""):

                leaderboard = Contest.objects.get(code=contest_code).leaderboard
                leaderboard.activity.add(activity)

        except Exception as e:
            print("Error Submit_Code_ProblemAPI", str(e))

        return Response(data=response)

Submit_Code_Problem = Submit_Code_ProblemAPI.as_view()

class Get_LeaderboardAPI(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):

        response = {}
        response['status'] = 500

        try:
            data = request.data

            contest_code = data['contest_code']

            leaderboard = Contest.objects.get(code=contest_code).leaderboard

            dict = {}

            for user in leaderboard.activity.distinct("user").all():

                temp_dict = {}

                for problem in Contest.problems.all():

                    temp_dict[problem.code] = 0

                temp_dict['total'] = 0

                dict[user] = temp_dict

            for activity in leaderboard.activity.all():

                user = activity.user
                problem_code = activity.problem.code

                dict[user][problem_code] = max(dict[user][problem_code],points)

            for user in dict.keys():

                sum = 0

                for problem in dict[user].keys():

                    sum += dict[user][problem]

                dict[user]['total'] = sum

            response['leaderboard'] =  dict

        except Exception as e:
            print("Error Get_LeaderboardAPI", str(e))

        return Response(data=response)

Get_Leaderboard = Get_LeaderboardAPI.as_view()


# method to add problems to a contest through shell
# c1 = Contest(name='first_contest', code='#include<bits/stdc++.h>')
# c1.save()
# p1 = Problem(name='p1', code='linked_list')
# p1.save()
# c1.problems.add(p1)



def home(request):
    
    print("!!!!!!!!!!!!!!!!!!",request.user)
    login_type = mentor_or_not(request.user)
  
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    account_type = "student"
    if (login_type == "mentor"):
        return render(request,'newtheme/index_mentor.html')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    if request.user.is_authenticated:
        obj = User.objects.filter(username = str(request.user)).all()[0]
        email = obj.email
        Cust_user = Custom_User.objects.get(user = obj)
        phone = Cust_user.phone
        print(email)
        user_name    = str(request.user)
        url="/payment_confirmation"
    else:
        print("not authenticated")
        email = "0" 
        phone = "0"
        user_name="0"
        url="/accounts/login"
    course_id=1 
    group_price= Courses.objects.filter(id=course_id).all()[0].group_price

    name            = Courses.objects.filter(id=course_id).all()[0].name

    gdates = {}
    if Courses.objects.filter(id=course_id).all()[0].group_seat1 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = Courses.objects.filter(id=course_id).all()[0].group_seat1
    if Courses.objects.filter(id=course_id).all()[0].group_seat2 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = Courses.objects.filter(id=course_id).all()[0].group_seat2
    for i,j in gdates.items():
        if j!=0:
            join = i
            break
    course_id=2  
    group_price1       = Courses.objects.filter(id=course_id).all()[0].group_price
    name1            = Courses.objects.filter(id=course_id).all()[0].name

    gdates = {}
    if Courses.objects.filter(id=course_id).all()[0].group_seat1 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = Courses.objects.filter(id=course_id).all()[0].group_seat1
    if Courses.objects.filter(id=course_id).all()[0].group_seat2 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = Courses.objects.filter(id=course_id).all()[0].group_seat2
    for i,j in gdates.items():
        if j!=0:
            join1 = i
            break 
    course_id=4 
    group_price2       = Courses.objects.filter(id=course_id).all()[0].group_price
    name2            = Courses.objects.filter(id=course_id).all()[0].name
 
    gdates = {}
    if Courses.objects.filter(id=course_id).all()[0].group_seat1 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = Courses.objects.filter(id=course_id).all()[0].group_seat1
    if Courses.objects.filter(id=course_id).all()[0].group_seat2 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = Courses.objects.filter(id=course_id).all()[0].group_seat2
    for i,j in gdates.items():
        if j!=0:
            join2 = i
            break       
    context={
        'gprice_inPaise' :group_price * 100,
        'gprice_inPaise1' :group_price1 * 100,
        'gprice_inPaise2' :group_price2 * 100,
        'user_name':user_name,
        'name_trim'  : name.replace(" ",""),
        'name_trim1'  : name1.replace(" ",""),
        'name_trim2'  : name2.replace(" ",""),
        'join':join,
        'join1':join1,
        'join2':join2,
        'email':email,
        'phone':phone,
        'account_type':account_type
    }
    return render(request,'newtheme/index.html',context)

def algoedge(request):
    print("amanbhai")
    if request.method=='POST':
        print("amanbhai")
        st=AlgoEdge()
        st.first_name=request.POST['first_name']
        st.last_name=request.POST['Last_name']
        st.college_name=request.POST['College_name']
        st.Year=request.POST['Year']
        st.Resume=request.POST['Resume']
        st.save()
        print(st.first_name)
        print(st.last_name)
    context={}
    return render(request, 'newtheme/career_camp.html', context)

def doubt(request):
    print("amanbhai")
    if request.method=='POST':
        print("amanbhai")
        st=ask_doubt()
        st.user_name=request.POST['user_name']
        st.doubt=request.POST['doubt']
        st.save()
    customus= Custom_User.objects.get(user=request.user)
    print(customus)
    current_user = customus.user
    today = datetime.date.today() #reference point.
    print(today)
    today = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    print("today is ",today)
    print(customus.start_date)
    if (customus.start_date != "No Course Purchased"):
        c_start_date = customus.start_date
        print("date is uptodate is ",datetime.datetime.strptime(c_start_date, '%d/%m/%Y'))
        c_start_date = datetime.datetime.strptime(c_start_date, '%d/%m/%Y')
        print(c_start_date)
        if(today >= c_start_date):
            customus.scheduledclass = ""
            customus.save()
    uni_strt = customus.start_date
    uni_end = customus.end_date
    showit=customus.AlgoEdge_enrolled
    print(showit)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!",uni_strt,uni_end)
    enroll_list = []
    full_enroll_list = []
    for i in range (3):
        templist = Courses.objects.all()[i]
        for j in range(len(templist.enrolledusers.all())):
            if (str(current_user) == str(templist.enrolledusers.all()[j])):
                enroll_list.append(str(templist))
                full_enroll_list.append(templist)
    print(enroll_list) 
    course_id = "-1"
    show_course = False
    if (len(enroll_list)>0):
        show_course = True
        if(enroll_list[0]== "Speed Up with DS Algo"):
            course_id = "1"
        if(enroll_list[0]== "Web-Development with Python+Django"):
            course_id = "2"
        if(enroll_list[0]== "Data Science With AI & ML"):
            course_id = "4"
    saturday = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
    sunday = today + datetime.timedelta((calendar.SUNDAY-today.weekday()) % 7 )
   
    
    show_date = True
    saturday = "Next Class is Scheduled on" + str(saturday.strftime('%b %d,%Y')) + "(saturday)"
    sunday = "Next Class is Scheduled on" +str(sunday.strftime('%b %d,%Y')) + "(sunday)"

    questions= customus.questionsallotted
    schedule=customus.scheduledclass
    
    link = customus.link
    show = True
    schedule1 = ""
    
    schedule = schedule.replace("<p>","")
    schedule = schedule.replace("</p>","")
    print(schedule)
    if(schedule == "No One to One Class Scheduled ! Mentors take One-to-One Class of each individual student. Purchase a course to get One to One Classes with mentors."):
        show = False
    else:
        if (schedule != ""):
            show_date = False
            schedule1=customus.scheduledclass
            print(schedule1)
            schedule1 = schedule1.replace("<p>","")
            schedule1 = schedule1.replace("</p>","")

    fulln=customus.fullname
    questions = questions.replace("<p>", '<p><span style="color:#ffffff">')
    questions = questions.replace("</p>", "</span></p>")
    account_type = ""
    print("show is",show)

    list_speed = datastructure
    list_topic = customus.current_topic
    final_list = get_zip_list_name(list_speed,list_topic,datastructure_temp)

    list_speed = algorithm
    list_topic = customus.current_topic
    final_list_algo = get_zip_list_name(list_speed,list_topic,algorithm_temp)

    list_speed = python_list
    list_topic = customus.current_topic
    final_list_python = get_zip_list_name(list_speed,list_topic,python_list_temp)
    
    list_speed = flask_list
    list_topic = customus.current_topic
    final_list_flask = get_zip_list_name(list_speed,list_topic,flask_list_temp)
    
    list_speed = django_list
    list_topic = customus.current_topic
    final_list_django = get_zip_list_name(list_speed,list_topic,django_list_temp)
    


    context = {
        'questions':questions ,
        'schedule' :schedule,
        'fulln':fulln,
        'saturday': saturday,
        'sunday': sunday,
        'show': show,
        'link':link,
        'uni_strt': uni_strt,
        'uni_end': uni_end,
        'enroll_list': enroll_list,
        'course_id':course_id,
        'show_date':show_date,
        'schedule1' :schedule1,
        'show_course':show_course,
        'account_type':account_type,
        'final_list':final_list,
        'final_list_algo':final_list_algo,
        'final_list_python':final_list_python,
        'final_list_flask':final_list_flask,
        'final_list_django':final_list_django,
        'full_enroll_list':full_enroll_list,
        'showit':showit,   
        'Issubmit':True,     
    }
    return render(request, 'newtheme/mylearning.html', context)

def sitemap(request):
    #return render(request,'newtheme/sitemap.xml')
    path = os.path.join(BASE_DIR,'files') 
    test_case = path + "/sitemap/"
    print(test_case)
    test_paths = glob(test_case + "*.xml")
    print(test_paths)
    for path in test_paths:
        file = open(path, 'r')
        temp = file.read()
        print(temp)
    return HttpResponse(temp, content_type='text/xml')

@login_required(login_url='/accounts/login/')
def myreferral(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    username = request.user
    myUser = User.objects.filter(username = username).all()[0]
    myCustomUser = Custom_User.objects.filter(user = myUser)[0]
    show = True
    code = "Generate Your Coupon Code"
    showit = True
    showit1=True
    showit2 = True
    final_show = True
    if request.user.is_authenticated:
        myuser= (request.user)
        email = User.objects.filter(username = str(request.user)).all()[0].email
        user_name    = str(request.user)
        templist= Courses.objects.filter(id="1").all()[0].enrolledusers.all().filter(user=myuser)
        templist1= Courses.objects.filter(id="2").all()[0].enrolledusers.all().filter(user=myuser)
        templist2= Courses.objects.filter(id="4").all()[0].enrolledusers.all().filter(user=myuser)
        print(templist)
        print(templist1)
        print(templist2)
        if not templist :
            print("not show")
            showit=False
        if not templist1 :
            showit1 = False
        if not templist2 :
            showit2 = False
        
        if showit or showit1 or showit2 :
            final_show = True
        else:
            final_show = False
    
    print("!!!!!!!!!!!", final_show)
   

    if(myCustomUser.referral_code == "Generate Your Coupon Code"):
        show = False
    else:
        code = myCustomUser.referral_code
    return render(request,'newtheme/referral.html', context = {'show':show , 'code':code,'swal':'False','final_show':final_show })

@login_required(login_url='/accounts/login/')
def generateCode(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    username = request.user
    myUser = User.objects.filter(username = username).all()[0]
    myCustomUser = Custom_User.objects.filter(user = myUser)[0]
    show = True
    if(myCustomUser.referral_code == "Generate Your Coupon Code"):
        code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        code = ''
        
        for i in range(0, 8):
            slice_start = random.randint(0, len(code_chars) - 1)
            code += code_chars[slice_start: slice_start + 1]
        username = request.user
        p = CouponCode(name = code, discount = 200)
        p.save()
        myUser = User.objects.filter(username = username).all()[0]
        myCustomUser = Custom_User.objects.filter(user = myUser)[0]
        myCustomUser.referral_code = code
        myCustomUser.save()

    else:
        code = myCustomUser.referral_code
    
    return render(request,'newtheme/referral.html', context = {'show':show , 'code':code , 'swal':'True','final_show':'True'})




def Login(request):
    if request.method == 'GET' and 'next' in request.GET:
        print("in gettt")
        nextUrl = request.GET['next']
        print(nextUrl)
        return render(request,'newtheme/login.html',{'nextUrl':nextUrl, 'show': False})
    else:
        print("not")
        nextUrl = "/mylearning#cop"
        return render(request,'newtheme/login.html',{'nextUrl':nextUrl, 'show': False})

@login_required(login_url='/accounts/login/')
def mentordashbord(request):
    mentor = Mentor_user.objects.get(user = request.user)
    print("alloted students")
    print(mentor.allotedstudents.all())
    students = mentor.allotedstudents.all()
    context={
        'students':students,
    }
    return render(request,'newtheme/mentordashboard.html',context=context)

@login_required(login_url='/accounts/login/')
def facultydashboard(request):
    faculty = Faculty_user.objects.get(user = request.user)
    contest = faculty.allotedcontest.all()
    context={
        'contest':contest,
    }
    return render(request,'newtheme/facultydashboard.html',context=context)

# @login_required(login_url='/accounts/login/')
# def home(request):
#     return render(request,'newtheme/index_mentor.html')

@login_required(login_url='/accounts/login/')
def coursementor(request):
    
    mentor = Mentor_user.objects.get(user = request.user)
    course_id = int(mentor.course_alloted)
    showit=True
    print("c_id",course_id)
    context = {
        'course_id':course_id, 
        'showit':showit
        }
   
    return render(request,'newtheme/course_mentor.html', context=context)


def logintodashboard(request):
    #nextUrl = request.GET['next'] 
    nextUrl=request.POST['nextUrl']
    print("******************************************************")
    print(nextUrl)
    usern=request.POST['usern']
    # passw=request.POST['passw']
    passw = request.POST.get('passw', False)

    user = authenticate(username=usern, password=passw)
    if user is not None:
        login(request, user)
        enroll_list = []
        customus= Custom_User.objects.get(user=request.user)
        print(customus)
        current_user = customus.user
        for i in range (3):
            templist = Courses.objects.all()[i]
            for j in range(len(templist.enrolledusers.all())):
                if (str(current_user) == str(templist.enrolledusers.all()[j])):
                    enroll_list.append(str(templist))
        print(enroll_list) 
        mentor = Mentor_user.objects.all()
        login_type = mentor_or_not(request.user)
       
          
                

        
        # if len(enroll_list) == 0:
        #     localStorage.setItem("type","notenrolled")
        # else:
        #     localStorage.setItem("type","enrolled")
            
        if (login_type == "mentor"):
            return redirect('mentordashbord')
        if(login_type == "faculty"):
            return redirect('facultydashboard')
        if(login_type=="ambassador"):
            return redirect('ambassdordashboard')
            
        return HttpResponseRedirect(nextUrl)
        #return HttpResponseRedirect('/practice')
    else:
        nextUrl = "/mylearning#cop"
        return render(request,'newtheme/login.html',{'nextUrl':nextUrl, 'show': True})
   

def mentor_or_not(usertype):
    mentor = Mentor_user.objects.all()
    for i in mentor:
        if i.user == usertype:
            return "mentor"
    faculty = Faculty_user.objects.all()
    for i in faculty:
        if i.user == usertype:
            return "faculty"
    ambassador = AmbassadorUser.objects.all()
    for i in ambassador:
        if i.user == usertype:
            return "ambassador"
            # localStorage.setItem("type","mentor")
    return "student"




# def Signup(request):
#     return render(request,'newsignup.html')




@login_required(login_url='/accounts/login/')
def ambassdordashboard(request):
    ambassador = AmbassadorUser.objects.get(user =request.user )
    context={
        'ambassador':ambassador
    }
    return render(request,'ambassador/dashboard.html',context=context)

#dnd @login_required(login_url='/login')
@login_required(login_url='/accounts/login/')
def Idementor(request):
    
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    return render(request,'newtheme/idementor.html')

def Ide(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    account_type="student"
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    return render(request,'newtheme/ide.html',{'account_type':account_type})

def blogs(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    account_type="student"
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    blogObject = Blogs.objects.all()
    #pagination code
    paginator = Paginator(blogObject, 9)
    page = request.GET.get('page')
    makePages = False
    if(len(blogObject)>9):
        makePages = True

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #paginaton code ends
    context = {
        'blogObject': blogObject,
        'page':page,
        'posts':posts,
        'makePages':makePages,
        'account_type':account_type
    }
    return render(request,'newtheme/blogs-home.html',context)


def single_blogs(request, blogs_name):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    account_type ="student"
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    experience = Blogs.objects.get(name=blogs_name)
    context = {
        'name': experience.name,
        'content': experience.content,
        'created_date': experience.created_date,
        'author': experience.author,
        'linkofauthor': experience.linkofauthor,
        'account_type':account_type
        
    }

    return render(request, 'newtheme/blogs-home-single.html', context)

@login_required(login_url='/accounts/login/')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#dnd @login_required(login_url='/login')
def practice(request):
    return render(request,'new_template/practice.html')




#dnd @login_required(login_url='/login')
def courses(request):
    #user = request.user
    #print("User++++++++++++++++++++++++++++++",user)
    login_type = mentor_or_not(request.user)
    account_type ="student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    courses_list = Courses.objects.all()
    print("this is the courses",courses_list)
    context = {
        "courses_list" : courses_list,
        'account_type':account_type
    }
    return render(request,'newtheme/courses-home.html',context=context)

@login_required(login_url='/accounts/login/')
def courses_detail(request, course_id):
    
    login_type = mentor_or_not(request.user)
    account_type ="student"
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # if (login_type == "mentor"):
    #     return redirect('mentordashbord')
    user = request.user
    notes_list = Courses.objects.filter(id=course_id).all()[0].notesincourse.all()
    print("this is the courses",notes_list)
    context = {
        "notes_list" : notes_list
    }
    return render(request,'new_template/courses_detail.html',context=context)


def courses_promo(request, course_id):
    
    login_type = mentor_or_not(request.user)
    account_type ="student"
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    showit=True
    if request.user.is_authenticated:
        myuser= (request.user)
        obj = User.objects.filter(username = str(request.user)).all()[0]
        email = obj.email
        Cust_user = Custom_User.objects.get(user = obj)
        phone = Cust_user.phone
        user_name    = str(request.user)
        templist= Courses.objects.filter(id=course_id).all()[0].enrolledusers.all().filter(user=myuser)
        if not templist :
            showit=False
        else:
            print("show")
    else:
        print("not authenticated")
        email = "0"
        user_name = "0"
        phone="0"
        showit=False

    name            = Courses.objects.filter(id=course_id).all()[0].name
    start_date       = Courses.objects.filter(id=course_id).all()[0].start_date
    end_date       = Courses.objects.filter(id=course_id).all()[0].end_date
    description       = Courses.objects.filter(id=course_id).all()[0].description
    instructors       = Courses.objects.filter(id=course_id).all()[0].instructors
    price       = Courses.objects.filter(id=course_id).all()[0].price
    group_price       = Courses.objects.filter(id=course_id).all()[0].group_price
    duration = int(end_date.strftime("%m")) - int(start_date.strftime("%m")) +  12*(int(end_date.strftime("%Y")) - int(start_date.strftime("%Y")))
    start_date=start_date.strftime("%d/%m/%Y")
    end_date=end_date.strftime("%d/%m/%Y")
    coupons ={}
    dates = {}
    datesnot={}
    gdates = {}
    if Courses.objects.filter(id=course_id).all()[0].group_seat1 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = Courses.objects.filter(id=course_id).all()[0].group_seat1
    if Courses.objects.filter(id=course_id).all()[0].group_seat2 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = Courses.objects.filter(id=course_id).all()[0].group_seat2
 

    if Courses.objects.filter(id=course_id).all()[0].seat1 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date1] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date1] = Courses.objects.filter(id=course_id).all()[0].seat1
    if Courses.objects.filter(id=course_id).all()[0].seat2 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date2] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date2] = Courses.objects.filter(id=course_id).all()[0].seat2
    if Courses.objects.filter(id=course_id).all()[0].seat3 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date3] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date3] = Courses.objects.filter(id=course_id).all()[0].seat3
    if Courses.objects.filter(id=course_id).all()[0].seat4 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date4] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date4] = Courses.objects.filter(id=course_id).all()[0].seat4
    
    for i in range(len(CouponCode.objects.all())):
        coupons[str(CouponCode.objects.all()[i].name)] = str(CouponCode.objects.all()[i].discount)
    
    method_type=""
    context = {
        'name'       :name      ,
        'start_date' :start_date ,
        'end_date'   :end_date   ,
        'description':description,
        'instructors':instructors,
        'price'      :price,
        'showit'     :showit,
        'course_id'  :course_id,
        'user_name'  :user_name,
        'email'      :email,
        'price_inPaise' :price * 100,
        'gprice_inPaise' :group_price * 100,
        'name_trim'  : name.replace(" ",""),
        'description_trim' : description.replace(" ",""),
        'coupons' : coupons,
        'duration' : duration,
        'discount_label':"",
        'dates':dates,
        'phone':phone,
        'datesnot':datesnot,
        'coupon' : "No Coupon Code Used",
        'gprice'      :group_price,
        'gdates':gdates,
        'method_type':method_type,
        'account_type':account_type
        
    }
    return render(request,'newtheme/courses-home-'+str(course_id)+'.html',context=context)

def applyCoupon(request,course_id):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    coupon = request.POST['coupon'] 
    method_type = request.POST['method_type'] 
    print(request.POST , "dscsdc**********************" , request.POST.get('method_type'))
    discount = 0 
    for i in range(len(CouponCode.objects.all())):
        if(coupon == CouponCode.objects.all()[i].name ):
            discount =  (CouponCode.objects.all()[i].discount)
            break

    showit=True
    if request.user.is_authenticated:
        myuser= (request.user)
        obj = User.objects.filter(username = str(request.user)).all()[0]
        email = obj.email
        Cust_user = Custom_User.objects.get(user = obj)
        phone = Cust_user.phone
        user_name    = str(request.user)
        templist= Courses.objects.filter(id=course_id).all()[0].enrolledusers.all().filter(user=myuser)
        if not templist :
            print("not show")
            showit=False
        else:
            print("show")
    else:
        print("not authenticated")
        email = "0"
        user_name = "0"
        phone = "0"
        showit=False

    name            = Courses.objects.filter(id=course_id).all()[0].name
    start_date       = Courses.objects.filter(id=course_id).all()[0].start_date
    end_date       = Courses.objects.filter(id=course_id).all()[0].end_date
    description       = Courses.objects.filter(id=course_id).all()[0].description
    instructors       = Courses.objects.filter(id=course_id).all()[0].instructors
    price       = Courses.objects.filter(id=course_id).all()[0].price
    duration = int(end_date.strftime("%m")) - int(start_date.strftime("%m")) +  12*(int(end_date.strftime("%Y")) - int(start_date.strftime("%Y")))

    price = price - discount
    group_price       = Courses.objects.filter(id=course_id).all()[0].group_price
    group_price = group_price - discount
    dates = {}
    datesnot = {}
    gdates = {}
    if Courses.objects.filter(id=course_id).all()[0].group_seat1 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date1] = Courses.objects.filter(id=course_id).all()[0].group_seat1
    if Courses.objects.filter(id=course_id).all()[0].group_seat2 == 0:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = False
    else:
        gdates[Courses.objects.filter(id=course_id).all()[0].group_date2] = Courses.objects.filter(id=course_id).all()[0].group_seat2
 

    if Courses.objects.filter(id=course_id).all()[0].seat1 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date1] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date1] = Courses.objects.filter(id=course_id).all()[0].seat1
    if Courses.objects.filter(id=course_id).all()[0].seat2 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date2] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date2] = Courses.objects.filter(id=course_id).all()[0].seat2
    if Courses.objects.filter(id=course_id).all()[0].seat3 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date3] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date3] = Courses.objects.filter(id=course_id).all()[0].seat3
    if Courses.objects.filter(id=course_id).all()[0].seat4 == 0:
        dates[Courses.objects.filter(id=course_id).all()[0].date4] = False
    else:
        dates[Courses.objects.filter(id=course_id).all()[0].date4] = Courses.objects.filter(id=course_id).all()[0].seat4
    
    discount_label = "Invalid Coupon Code"
    if (discount > 0):
        discount_label =  "Hurray ! You got discount of Rs "+ str(discount) + "."
    start_date=start_date.strftime("%d/%m/%Y")
    end_date=end_date.strftime("%d/%m/%Y")
    coupons ={}
    for i in range(len(CouponCode.objects.all())):
        coupons[str(CouponCode.objects.all()[i].name)] = str(CouponCode.objects.all()[i].discount)
    print(coupons)
    #end_date=str(end_date).split(' ')[0]
    print(end_date)
    #if (course_id == 1):
    #    return render(request, )
    #print("this is the courses",notes_list)
   
    context = {
        'name'       :name      ,
        'start_date' :start_date ,
        'end_date'   :end_date   ,
        'description':description,
        'instructors':instructors,
        'price'      :price,
        'showit'     :showit,
        'course_id'  :course_id,
        'user_name'  :user_name,
        'email'      :email,
        'phone':phone,
        'price_inPaise' :price * 100,
        'gprice_inPaise' :group_price * 100,
        'name_trim'  : name.replace(" ",""),
        'description_trim' : description.replace(" ",""),
        'coupons' : coupons,
        'discount_label': discount_label,
        'coupon':coupon,
        'dates':dates,
        'datesnot':datesnot,
        'gprice'      :group_price,
        'gdates':gdates,
        'method_type':method_type,
        'duration':duration,
        
    }
    #context={}
    return render(request,'newtheme/courses-home-'+str(course_id)+'.html',context=context)



@login_required(login_url='/accounts/login/')
def contest_list(request):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contests = Contest.objects.all()
    context = {
        'contests': contests,
        'account_type':account_type
    }
    return render(request, 'newtheme/contest-home.html', context)

def free_trial(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    if request.method == 'POST':
        name = request.POST['name']
        interest = request.POST['course']
        email = request.POST['email']
        phone = request.POST['phone']
        print("if---------------")
        print(name, interest)
        val = 0
        try:
            FreeTrial.objects.get(phone=phone)
            val = 2
        except:
            p = FreeTrial(name= name,email=email,phone=phone, interest = interest)
            p.save()
            val = 0
        
        context = {'show':val}
        return render(request, 'newtheme/free-trial.html', context)
    else:
        print("else-------------")
        context = {'show':False}
        return render(request, 'newtheme/free-trial.html', context)


def payment_confirmation(request):
    print(request.POST , "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    course_id = request.POST['course_id']
    username = request.user
    obj = Courses.objects.filter(id=course_id).all()[0]
    price       = obj.price
    subscriber  = obj.enrolledusers.all()
    myUser = User.objects.filter(username = username).all()[0]
    print(myUser)
    obj2 = Custom_User.objects.get(user = myUser)
    myCustomUser = obj2
    myCustomUserN = obj2
    myCourse = obj
    amount = request.POST['finalval']
    print(amount)
    payment_id = request.POST['razorpay_payment_id']
    print(payment_id)
    paymentMessage = "Sorry! Payment Failed"
    paymentImage = False
    razorpay_client.payment.capture(payment_id, amount)
    print(razorpay_client.payment.fetch(payment_id))
    if (str(razorpay_client.payment.fetch(payment_id)['status'])=="captured" ):      
        coupon_code = request.POST['coupon_applied']
        try:
            amb = AmbassadorUser.objects.get(code = str(coupon_code))
            amb.studentCount = int(amb.studentCount) + 1
        except:
            pass
        p = Enroll(name = myCustomUserN.fullname , code = coupon_code , course = myCourse.name )
        p.save()
        myCourse.enrolledusers.add(myCustomUser)
        
        paymentMessage = "Payment Successfull!"
        schedule = obj2
        schedule.questionsallotted = str("Mentor will alot you questions soon")
        
        method_type = request.POST['method_type']
        

        date = datetime.date.today()
        date=str(date)
        date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        course_object = Courses.objects.get(id=course_id)
        schedule.start_date =  date
        x1 = Courses.objects.filter(id=course_id).all()[0].date1
        x1 = x1.strftime('%d/%m/%Y')
        x2 = Courses.objects.filter(id=course_id).all()[0].date2
        x2 = x2.strftime('%d/%m/%Y')
        x3 = Courses.objects.filter(id=course_id).all()[0].date3
        x3 = x3.strftime('%d/%m/%Y')
        x4 = Courses.objects.filter(id=course_id).all()[0].date4
        x4 = x4.strftime('%d/%m/%Y')
        gx1 = Courses.objects.filter(id=course_id).all()[0].group_date1
        gx1 = gx1.strftime('%d/%m/%Y')
        gx2 = Courses.objects.filter(id=course_id).all()[0].group_date2
        gx2 = gx2.strftime('%d/%m/%Y')
        if(str(myCourse.name) == "Data Science With AI & ML"):
            # today = date
            # future_day = today.day
            # future_month = (today.month + 12) % 12
            # future_year = today.year + ((today.month + 12) // 12)
            # six_months_later = datetime.date(future_year, future_month, future_day)
            # six_months_later = (datetime.datetime.strptime(date, '%b %d %Y') + datetime.timedelta(days=365)).strftime('%d/%m/%Y')
            # schedule.end_date = str(six_months_later.strftime('%b %d,%Y'))
            six_months_later = (datetime.datetime.strptime(date, '%d/%m/%Y') + datetime.timedelta(days=365)).strftime('%d/%m/%Y')
            print(six_months_later)
            schedule.end_date = six_months_later
        else:
            # today = date
            # future_day = today.day
            # future_month = (today.month + 2) % 12
            # future_year = today.year + ((today.month + 2) // 12)
            # six_months_later = datetime.date(future_year, future_month, future_day)
            # six_months_later = (datetime.datetime.strptime(date, '%b %d %Y') + datetime.timedelta(days=60)).strftime('%d/%m/%Y')
            # schedule.end_date = str(six_months_later.strftime('%b %d,%Y'))
            six_months_later = (datetime.datetime.strptime(date, '%d/%m/%Y') + datetime.timedelta(days=60)).strftime('%d/%m/%Y')
            schedule.end_date = six_months_later
        
        date_next = (datetime.datetime.strptime(date,  '%d/%m/%Y') + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        classes = "Next Class is Scheduled on " + str(date) + "( Saturday)" + "\nNext Class is Scheduled on" + str(date_next) + " (Sunday)"
        schedule.scheduledclass = str(classes)
        if str(method_type) == "one":
            if str(schedule.method_type) == "Not Purchased":
                schedule.method_type = "One"
            elif str(schedule.method_type) == "Group":
                schedule.method_type = schedule.method_type + " + One"
            if (date == x1):
                course_object.seat1 = course_object.seat1-1
            if (date == x2):
                course_object.seat2 = course_object.seat2-1
            if (date == x3):
                course_object.seat3 = course_object.seat3-1
            if (date == x4):
                course_object.seat4 = course_object.seat4-1

        else:
            if str(schedule.method_type) == "Not Purchased":
                    schedule.method_type = "Group"
            elif str(schedule.method_type) == "One":
                schedule.method_type = schedule.method_type + " + Group"
            if date == gx1:
                course_object.group_seat1 = course_object.group_seat1-1
            if date == gx2:
                course_object.group_seat2 = course_object.group_seat2-1

        course_object.save()
        schedule.save()
        paymentImage = True
        #enter code to add entry to table
        x =2
    
    context={
        'id'            :razorpay_client.payment.fetch(payment_id)['id'],
        'amount'        :razorpay_client.payment.fetch(payment_id)['amount']/100,
        'status'        :razorpay_client.payment.fetch(payment_id)['status'],
        'email'         :razorpay_client.payment.fetch(payment_id)['email'],
        'description'   :razorpay_client.payment.fetch(payment_id)['description'],
        'course_id'     :course_id,
        'paymentMessage'  :paymentMessage,
        'paymentImage'     :paymentImage
    }
    return render(request, 'newtheme/payment_confirmation.html', context)

@login_required(login_url='/accounts/login/')
def onotes_list(request, course_id):
    login_type = mentor_or_not(request.user)
    account_type = "student" 
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador" 
    showit=True
    if request.user.is_authenticated:
        myuser= (request.user)
        templist= Courses.objects.filter(id=course_id).all()[0].enrolledusers.all().filter(user=myuser)
        print((templist))
        print((request.user))
        if not templist :
            print("not show")
            showit=False
        else:
            print("show")
    else:
        print("not authenticated")
        showit=False  
    context = {'course_id':course_id, 'showit':showit,'account_type':account_type}
    return render(request, 'newtheme/myfile.html', context)


def ambassador_form(request):
    name = request.POST['name']
    cllg_name = request.POST['cllg']
    email = request.POST['email']
    phone = request.POST['phone']
    print("######################################")

    context = {}
    return render(request, 'new_template/enroll_now.html', context)



def enroll_now(request):
    context = {}
    return render(request, 'new_template/enroll_now.html', context)

def problem_list(request):
    login_type = mentor_or_not(request.user)
    account_type = "student" 
    if(login_type=="ambassador"):
        account_type = "ambassador" 
    problems = Problem.objects.all()
    post_list = problems
    makePages = False
    if(len(problems)>9):
        makePages = True
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')
 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'problems': problems,
        'page':page,
        'posts':posts,
        'makePages':makePages,
        'account_type':account_type
    }
    return render(request, 'newtheme/practice-home.html', context)


@login_required(login_url='/accounts/login/')
def note_list(request):
    context ={}
    return render(request, 'new_template/index.html', context)




@login_required(login_url='/accounts/login/')
def contest(request, contest_name):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    c = Contest.objects.get(name=contest_name)
    problem = c.problems.all()
    context = {
        'problems': problem,
    }
    return render(request, 'contest.html', context)



def dashboard(request):

    note = Note.objects.all()
    problem = Problem.objects.all()

    context = {
        'problems': problem,
        'notes': note,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='/accounts/login/')
def video_list(request):
    return render(request, 'new_template/video_note2.html')

def ambassador(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    if request.method == 'POST':
        name = request.POST['name']
        cllg_name = request.POST['cllg']
        email = request.POST['email']
        phone = request.POST['phone']
        print("if---------------")
        print(name)
        try:
            Ambassador.objects.get(phone = phone)
            val = 2
        except:
            p = Ambassador(name= name,college_name= cllg_name,email=email,phone=phone)
            p.save()
            val = 0
        
        context = {'show':val}
        return render(request, 'newtheme/ambassador.html', context)
    else:
        print("else-------------")
        context = {'show':False}
        return render(request, 'newtheme/ambassador.html', context)

@login_required(login_url='/accounts/login/')
def single_note(request, label, note_name, course_id):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type = "ambassador"
    showit=True
    user_name= (request.user)
    name= Courses.objects.filter(id=course_id).all()[0].name
    if request.user.is_authenticated:
        myuser= (request.user)
        obj = User.objects.filter(username = str(request.user)).all()[0]
        email = obj.email
        Cust_user = Custom_User.objects.get(user = obj)
        phone = Cust_user.phone
        templist= Courses.objects.filter(id=1).all()[0].enrolledusers.all().filter(user=myuser)
        templist2= Courses.objects.filter(id=2).all()[0].enrolledusers.all().filter(user=myuser)
        templist3= Courses.objects.filter(id=4).all()[0].enrolledusers.all().filter(user=myuser)
        print((templist))
        print((request.user))
        if course_id==1 and (not templist):
            showit=False
        elif course_id==2 and (not templist2):
            showit=False
        elif course_id==4 and (not templist3):
            showit=False

    else:
        print("not authenticated")
        showit=False
    note = Note.objects.get(name=note_name)
    note_eg = Note.objects.filter(label ='Array').all()
    print(note_eg)
    # print("note_eg is ........",note_eg)
    # list_need = []
    # for i in note_eg:
    #     list_need.append(i)
    # print("list_need is ......",list_need, len(list_need))
    cust = Custom_User.objects.get(user = request.user)
    list_topic = cust.current_topic
    
    index = list_topic.find(label)
    index = int(index) + int(len(label)) + 1

    note_list = Note.objects.filter(label=label)
    last_index = index - 1 + len(note_list) 
    c = 0
    string_to_update = list_topic[index:last_index+1]
    subst = list_topic[index:last_index+1]
    subst = list(subst)
    for i in note_list:
        if str(i.name) == str(note.name):
            print(note_list)
            break
        c = c+1
    if(list_topic[index+c]=='0'):
        list_topic = list(list_topic)
        list_topic[index+c] = '1'
        list_topic = "".join(list_topic)
    # print(list_topic)
    cust.current_topic = list_topic
    cust.save()

    #
    # note_list = note_list.exclude(name=note.name)
    #
    # print(note_list)
    prev = ""
    next = ""
    status = ""
    
    l = len(note_list)
    print("length is",l,label)
    for i in range (len(note_list)):
        if(str(note_list[i])==str(note.name)):
            if(i>0 and i<l-1):
                prev = note_list[i-1]
                next = note_list[i+1]
                status = "okay"
            if(i==0):
                next = note_list[i+1]
                status = "next"
            if(i==l-1):
                prev = note_list[i-1]
                status = "prev"

    final_list = zip(subst,note_list)
    print(note.name)
    print(l)
    print('mana')
    if course_id==1:
        gprice_inPaise=399900
    elif course_id==2:
        gprice_inPaise=399900
    else:
        gprice_inPaise=1199900
    context = {
        'name': note.name,
        'content': note.content,
        'other_notes': final_list,
        'len': l,
        'label': label,
        'prev': prev,
        'next': next,
        'status': status,
        'showit' : showit,
        'course_id':course_id,
        'account_type':account_type,
        'user_name':user_name,
        'gprice_inPaise':gprice_inPaise,
        'name_trim'  : name.replace(" ",""),
        'email':email,
        'phone':phone,
    }
    if course_id==1:
        return render(request, 'newtheme/myfile.html', context)
    elif course_id==2:
        return render(request, 'newtheme/myfile1.html', context)
    else:
        return render(request, 'newtheme/myfile2.html', context)
          
    


@login_required(login_url='/accounts/login/')
def single_note_mentor(request, label, note_name, course_id):
    showit=True
    print("single_note_mentor")
    if request.user.is_authenticated:
        mentor = Mentor_user.objects.get(user = request.user )
        if (mentor.course_alloted == "1" or mentor.course_alloted == "2" or mentor.course_alloted == "4"):
            showit = True
        else:
            showit = False
    else:
        print("not authenticated")
        showit=False
        
    note = Note.objects.get(name=note_name)

    note_list = Note.objects.filter(label=label)

    print(note_list)
    #
    # note_list = note_list.exclude(name=note.name)
    #
    # print(note_list)
    prev = ""
    next = ""
    status = ""
    l = len(note_list)
    for i in range (len(note_list)):
        if(str(note_list[i])==str(note.name)):
            if(i>0 and i<l-1):
                prev = note_list[i-1]
                next = note_list[i+1]
                status = "okay"
            if(i==0):
                next = note_list[i+1]
                status = "next"
            if(i==l-1):
                prev = note_list[i-1]
                status = "prev"

    print(l)
    print(next)
    print(prev)
    
    context = {
        'name': note.name,
        'content': note.content,
        'other_notes': note_list,
        'len': l,
        'label': label,
        'prev': prev,
        'next': next,
        'status': status,
        'showit' : showit,
        'course_id':course_id
        
    }
    return render(request, 'newtheme/note-mentor-single.html', context= context)



@login_required(login_url='/accounts/login/')
def single_problem(request, problem_name):
    login_type = mentor_or_not(request.user)
    account_type ="student"
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type ="ambassador"
    problem = Problem.objects.get(name=problem_name)
    path = os.path.join(BASE_DIR,'files')
    print("##############")
    print(path)
    test_case = path + "/Problems/" + problem_name + "/test-cases/"
    exp_out = path + "/Problems/" + problem_name + "/expected-output/"
    print(test_case)
    test_paths = glob(test_case + "*.txt")
    print(test_paths)
    test_paths.sort()
    print(test_paths)
    exp_paths = glob(exp_out + "*.txt")
    exp_paths.sort()


    #print("test case path = ", test_case)
    #print("expected output paths = ", exp_out)

    l=0
    tc=0
    eo=0
    all_tc = []
    all_eo = []

    for path in test_paths:
        file = open(path, 'r')
        temp = file.read()
        tc = temp
        all_tc.append(tc)
        print(tc)
        print("all tc = ",all_tc)
        l = len(tc)
        print("length = ", l)

    for path in exp_paths:
        file = open(path, 'r')
        temp = file.read()
        eo = temp
        all_eo.append(eo)
        print(eo)
        print("all eo = ", all_eo)


    files = len(all_tc)


    context = {
        'name': problem.name,
        'content': problem.content,
        'created_date': problem.created_date,
        'points': problem.points,
        'test_cases': all_tc,
        'exp_outs': all_eo,
        'files': files,
        'analyse_link':problem.analyse_link,
        'account_type':account_type
    }

    return render(request, 'newtheme/practice-home-single.html', context)

def about(request):
    return render(request, 'newtheme/about.html',context={})




dsa = ['Introduction to Array and Pointers in Arrays','Arrray Operations','Multi-Dimension Array','Arrays and Functions','Introduction to Linked List and Types of Linked Lists','Linked List Operations','Comparison with other data structures','Introduction to Stack and Implementation of Stack','Expression Notifications using Stack','Introduction to Queue and Operations on Queue','Queue Implementation','Introduction to Binary Tree and Binary Tree and its Types','Tree Traversal','Implementation of Binary Tree','Introduction to Binary Search Tree and Binary Search Tree Operations','Identify whether BST','Min Max of BST','Height of BST','Introduction to Strings and String Manipulation Functions','Introduction to Graph andTypes of Graphs','BFS & DFS','Introduction to Hash Table','Collision and Chaining','Open Addressing','Vectors','Sets','Pairs','Maps','Introduction to Searching and Linear Search','Binary Search','Jump Search','Introduction to Sorting , Bubble Sort and Selection Sort','Insertion Sort','Merge Sort','Quick Sort','Counting Sort','Wave Sort','Introduction to Mathematical Logics and Euler Totient Function','Fermat Little Theorem','Sieve of Eratosthenes','Introduction to Greedy Approach and Activity Selection Problem','Job Sequencing Problem','Fractional Knapsack','Bin Packing','Introduction to Dynamic Programming','Longest Increasing Subsequence','House Robber','Edit Distance','Introduction to Divide and Conquer and Square Root','Search element in a rotated sorted array','Tiling Problem','Modular Exponentiation','Introduction to Backtracking','N QUEEN Problem','Knights Tour Problem','Introduction to Graph Algorithms','Floyd Warshall','Dijkstra’s Algorithm','Introduction to Pattern Matching and KMP Algorithm','Rabin Karp Algorithm' ]
webdev = ['Introduction to Python Data Types','Text and Numeric','Sequence and Mapping','Set, Boolean and Binary','Introduction to Python Operators','Arithmetic Operators','Bitwise Operators','Assignment Operators','Comparison Operators','Identity Operators','Logical Operators','Membership Operators','Introduction to Python Conditions','Nested & Short-Hand','Introduction to Python Loops','WHILE loop','FOR loop','NESTED loop','LOOP CONTROL SYSTEM','Introduction to Python Functions','Syntax and Examples','Introduction to Flask Basics','Creating Basic Flask App','Introduction to Flask Routing','Routes with Parameters','Introduction to Flask Methods','Methods in Route','Introduction to Flask Templates','Jinja2 Template','Introduction to Flask Deployment','Flask Web App on Heroku','Introduction to Django Basics','Creating a Project','Creating An App','Running Your First Project','Introduction to Django Views and Url','Url Mapping','Introduction to Django Models','Connecting Models','CRUD','Introduction to Django Redirection and Forms','Forms','Introduction to Django Deployment','Git and Heroku']
def eg(request,rid):
    print("cool")
    if(str(rid)=='29'):
        whatsapp_msg()
        whatsapp_msg1()
    return HttpResponse("200")



def whatsapp_msg():
  try:
    course_id=1
    list_students = Courses.objects.get(id=course_id).enrolledusers.all()
    sample("algoladder message start")
    for i in list_students:
      name = i.fullname
      day = i.counter
      sp = day.split(",")
      sp1= sp[0].split("-")
      wtdy = int(sp1[1])
      if wtdy<60:
        url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"
        headers = {
          "Content-Type": "application/json",
          "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
          }
        body ={
          #  "to_number": "91"+i.phone,
          "to_number": "91"+str(i.phone),
          "type":"text",
          "message": "Hello " + name + ", Greetings from AlgoLadder, Your Today's Topic is "+dsa[wtdy] + " and your course link is http://algoladder.com/onotes_list/1"
          }
        res = requests.post(url1,json=body,headers = headers)
        print("message sent")
        change = sp1[1].replace(sp1[1],str(int(sp1[1])+1))
        new = sp1[0]+'-'+change +','+sp[1]+','+sp[2]
        
        print("value of new is ",new)
        i.counter = new
        i.save()
        
      today = (dt.now(timezone.utc) +  timedelta(hours=5.5)).strftime("%A")
      if(today == "Saturday" or today == "Sunday"):
        url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"

        headers = {
          "Content-Type": "application/json",
          "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
        }
        body ={
          "to_number": "91"+str(i.phone),
          "type":"text",
          "message": "Hello "+name+" This message is just a reminder that classes will be held today of Course Speed Up with DS and algo , Greetings from Algoladder."
        }
        res = requests.post(url1,json=body,headers = headers)
    sample("algoladder message sent")
    
  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    message = ("error: %s ", e)
    message = str(message)
    sample(message)
  return 1
    
def whatsapp_msg1():
  course_id=2
  list_students = Courses.objects.get(id=course_id).enrolledusers.all()
  for i in list_students:
    name = i.fullname
    day = i.counter
    sp = day.split(",")
    sp1= sp[1].split("-")
    wtdy = int(sp1[1])
    if wtdy<44:
      url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"
      headers = {
        "Content-Type": "application/json",
        "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
      }
      body ={
        "to_number": "91"+str(i.phone),
        # "to_number": "91"+i.phone,
        "type":"text",
        "message": "Hello " + name + ", Greetings from AlgoLadder, Your Today's Topic is "+webdev[wtdy] + " and your course link is http://algoladder.com/onotes_list/2"
      }
      res = requests.post(url1,json=body,headers = headers)
      print("message sent")
      change = sp1[1].replace(sp1[1],str(int(sp1[1])+1))
      new = sp[0]+','+sp1[0]+'-'+change+','+sp[2]
      i.counter = new
      i.save()
    today = (dt.now(timezone.utc) +  timedelta(hours=5.5)).strftime("%A")
    if(today == "Saturday" or today == "Sunday"):
      url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"

      headers = {
        "Content-Type": "application/json",
        "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
      }
      body ={
        "to_number": "91"+str(i.phone),
        "type":"text",
        "message": "Hello "+name+" This message is just a reminder that classes will be held today of Course Web Development With python + Django , Greetings from Algoladder."
      }
      res = requests.post(url1,json=body,headers = headers)
      print("message sent")
    sample("algoladder message sent webdev")
  return 1


def sample(message):
  url1 = "https://api.maytapi.com/api/d055938a-28e2-4cd3-84af-e04e33b8f6e4/10360/sendMessage"
  headers = {
    "Content-Type": "application/json",
    "x-maytapi-key": "2256d8ad-0ed1-4474-9d33-7a1827861061",
  }
  body ={
    "to_number": "917906334045",
    "type":"text",
    "message": message
  }
  res = requests.post(url1,json=body,headers = headers)

  return 1



def problem_submit_success(request):
    print("inside problem submit ")

    if request.method == 'POST':
        p_name = request.POST.get('text')

        points = request.POST.get('p')
        obj = Custom_User.objects.get(user=request.user)

        print("points = ", points)
        print("problem name = ", p_name)
        print("user = ", obj)

        p = Problem.objects.get(name=p_name)

        l = obj.problems_solved.all()
        if p in l:
            print("points = ", points)
        else:

            obj.problems_solved.add(p)
            obj.points_earned = obj.points_earned + int(points)
            obj.save()
            print("new points = ", obj.points_earned)

        print("success")
        return HttpResponse("Solution Accepted")




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.email = form.cleaned_data.get('email')

            user.custom_user.email = form.cleaned_data.get('email')
            user.custom_user.phone = form.cleaned_data.get('phone')
            user.custom_user.fullname = form.cleaned_data.get('fullname')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'newtheme/signup.html', {'form': form})





# def contestone(request):
#     return render(request, 'contestone.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    obj = Custom_User.objects.get(user=request.user)
    fullname = obj.fullname
    current_user = obj.user
    email = obj.email
    phone = obj.phone
    university = obj.university
    uni_strt = obj.start_date
    uni_end = obj.end_date
    uni_cg = obj.universitycgpa
    points = obj.points_earned
    enroll_list = []
    for i in range (3):
        templist = Courses.objects.all()[i]
        for j in range(len(templist.enrolledusers.all())):
            if (str(current_user) == str(templist.enrolledusers.all()[j])):
                enroll_list.append(str(templist))
    print(enroll_list)    
    print("######################################")
    if(len(enroll_list)==0):
        enroll_list.append("No Course Purchased")
    prob = []
    for i in obj.problems_solved.all():
        prob.append(i.name)

    print("problems solved = ", prob)
    print("points = ", points)



    img = current_user.custom_user.image,

    print("image url = ", current_user.custom_user.image)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.custom_user)
        phoneform = phoneUpdateForm(request.POST, instance=request.user.custom_user)
        if u_form.is_valid() and phoneform.is_valid():
            user = u_form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.custom_user.email = u_form.cleaned_data.get('email')
            # user.custom_user.phone = u_form.cleaned_data.get('phone')
            # user.custom_user.university = u_form.cleaned_data.get('university')
            user.save()
            #u_form.save()
            phoneform.save()
            
            customus= Custom_User.objects.get(user=request.user)
            us=request.user
            customus.email=us.email
            customus.save()
        elif p_form.is_valid():
            p_form.save()
        messages.success(request, 'Your profile has been updated. ')
        return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        print("u form = ", u_form)
        p_form = ProfileUpdateForm(instance=request.user.custom_user)
        phoneform = phoneUpdateForm(instance=request.user.custom_user)

    context = {
        'fullname':fullname,
        'name': current_user,
        'email': email,
        'phone': phone,
        'university': university,
        'uni_strt': uni_strt,
        'uni_end': uni_end,
        'uni_cg': uni_cg,
        'points': points,
        'problems': prob,
        'enroll_list': enroll_list,
        'u_form': u_form,
        'p_form': p_form,
        'phoneform':phoneform,
        'img':str(current_user.custom_user.image)
    }
  

    return render(request, 'newtheme/profile-home.html', context)





@login_required(login_url='/accounts/login/')
def student(request,stu_id):
    stu = Custom_User.objects.get(id = stu_id)
    questions = stu.questionsallotted
    questions = questions.replace("<p>", " ") if questions else ""
    questions = questions.replace("</p>", " ") if questions else ""
    schedule_class = stu.scheduledclass
    schedule_class = schedule_class.replace("<p>", " ") if schedule_class else ""
    schedule_class = schedule_class.replace("</p>", " ") if schedule_class else ""
    context={
        'stu':stu,
        'questions':questions,
        'schedule_class':schedule_class,
        'id':stu_id
    }
    return render(request, 'newtheme/single_student.html', context)

@login_required(login_url='/accounts/login/')
def studentsave(request,stu_id):
    link = request.POST.get("link")
    #topic = request.POST.get("topic")
    ques = request.POST.get("que")
    cla = request.POST.get("class")
    print("link is",link)
    #print("link is",topic)
    print("questions is ", ques)
    print("class is ",cla)
    stu = Custom_User.objects.get(id = stu_id)
    stu.link = link
    #stu.current_topic = topic
    stu.questionsallotted = ques
    stu.scheduledclass = cla
    stu.save()
    url = "/student/" + str(stu_id)
    return redirect(url)





@login_required(login_url='/accounts/login/')
def update_profile(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.custom_user)

        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.custom_user.email = u_form.cleaned_data.get('email')
            # user.custom_user.phone = u_form.cleaned_data.get('phone')
            # user.custom_user.university = u_form.cleaned_data.get('university')
            user.save()
            #u_form.save()

            p_form.save()


        messages.success(request, 'Your profile has been updated. ')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        print("u form = ", u_form)
        p_form = ProfileUpdateForm(instance=request.user.custom_user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'new_template/update_profile2.html', context)







def interview_experiences(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    account_type ="student"
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type ="ambassador"
    interviewexp = InterviewExperiences.objects.all()
    #pagination code
    post_list = interviewexp
    makePages = False
    if(len(interviewexp)>9):
        makePages = True
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')
 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #paginaton code ends
    context = {
        'interviewexp': interviewexp,
        'page':page,
        'posts':posts,
        'makePages':makePages,
        'account_type':account_type
    }
    return render(request, 'newtheme/interview-home.html', context)




def single_experience(request, experience_name):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    account_type ="student"
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        account_type ="ambassador"
    experience = InterviewExperiences.objects.get(name=experience_name)
    context = {
        'name': experience.name,
        'companyname': experience.companyname,
        'content': experience.content,
        'created_date': experience.created_date,
        'author': experience.author,
        'linkofauthor': experience.linkofauthor,
        'account_type':account_type
        
    }

    return render(request, 'newtheme/interview-home-single.html', context)


def validate_coupon_code(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    coupon_code = request.GET.get('coupon_code', None)
    try:
        mycoupon =  CouponCode.objects.get(name=coupon_code)
        if mycoupon:
            data = {
                'exist': True ,
                'name': CouponCode.objects.get(name=coupon_code).name,
                'discount': CouponCode.objects.get(name=coupon_code).discount
            }
        else:
            data = {
                'exist':False,
                'name': 'no',
                'discount': 0
            }
    except:
        data = {
            'exist':False,
            'name': 'no',
            'discount': 0
        }
        
    return JsonResponse(data)








def couponapply(request, course_id):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    coupon_code = request.GET.get('coupon_code', None)
    myprice = request.POST["finalvalue"]
    print(myprice)
    showit=True
    if request.user.is_authenticated:
        myuser= (request.user)
        templist= Courses.objects.filter(id=course_id).all()[0].enrolledusers.all().filter(user=myuser)
        if not templist :
            print("not show")
            showit=False
        else:
            print("show")
    else:
        print("not authenticated")
        showit=False

    name            = Courses.objects.filter(id=course_id).all()[0].name
    start_date       = Courses.objects.filter(id=course_id).all()[0].start_date
    end_date       = Courses.objects.filter(id=course_id).all()[0].end_date
    description       = Courses.objects.filter(id=course_id).all()[0].description
    instructors       = Courses.objects.filter(id=course_id).all()[0].instructors
    price       = myprice
    email = User.objects.filter(username = str(request.user)).all()[0].email
    user_name    = str(request.user)
    start_date=start_date.strftime("%d/%m/%Y")
    end_date=end_date.strftime("%d/%m/%Y")
    coupons ={}
    for i in range(len(CouponCode.objects.all())):
        coupons[str(CouponCode.objects.all()[i].name)] = str(CouponCode.objects.all()[i].discount)
    print(coupons)
    #end_date=str(end_date).split(' ')[0]
    print(end_date)
    #if (course_id == 1):
    #    return render(request, )
    #print("this is the courses",notes_list)
    context = {
        'name'       :name      ,
        'start_date' :start_date ,
        'end_date'   :end_date   ,
        'description':description,
        'instructors':instructors,
        'price'      :price,
        'showit'     :showit,
        'course_id'  :course_id,
        'user_name'  :user_name,
        'email'      :email,
        'price_inPaise' :price * 100,
        'name_trim'  : name.replace(" ",""),
        'description_trim' : description.replace(" ",""),
        'coupons' : coupons
        
    }
    #context={}
    return render(request,'new_template/'+str(course_id)+'.html',context=context)

def analyse(request):
    context ={}
    return render(request, 'newtheme/analyse.html',context= context)

@login_required(login_url='/accounts/login/')
def mylearning(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    customus= Custom_User.objects.get(user=request.user)
    current_user = customus.user
    today = datetime.date.today() #reference point.
    today = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    date = datetime.date.today()
    date=str(date)
    date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    if (customus.start_date != "No Course Purchased"):
        c_start_date = customus.start_date
        c_start_date = datetime.datetime.strptime(c_start_date, '%d/%m/%Y')
        if(today >= c_start_date):
            customus.scheduledclass = ""
            customus.save()
    uni_strt = customus.start_date
    uni_end = customus.end_date
    showit=customus.AlgoEdge_enrolled
    enroll_list = []
    full_enroll_list = []
    for i in range (3):
        templist = Courses.objects.all()[i]
        for j in range(len(templist.enrolledusers.all())):
            if (str(current_user) == str(templist.enrolledusers.all()[j])):
                enroll_list.append(str(templist))
                full_enroll_list.append(templist)
    course_id = "-1"
    show_course = False
    if (len(enroll_list)>0):
        show_course = True
        if(enroll_list[0]== "Speed Up with DS Algo"):
            course_id = "1"
        if(enroll_list[0]== "Web-Development with Python+Django"):
            course_id = "2"
        if(enroll_list[0]== "Data Science With AI & ML"):
            course_id = "4"
    saturday = today + datetime.timedelta((calendar.SATURDAY-today.weekday()) % 7 )
    sunday = today + datetime.timedelta((calendar.SUNDAY-today.weekday()) % 7 )
   
    
    show_date = True
    saturday = "Next Class is Scheduled on" + str(saturday.strftime('%b %d,%Y')) + "(saturday)"
    sunday = "Next Class is Scheduled on" +str(sunday.strftime('%b %d,%Y')) + "(sunday)"

    questions= customus.questionsallotted
    schedule=customus.scheduledclass
    
    link = customus.link
    show = True
    schedule1 = ""
    
    schedule = schedule.replace("<p>","")
    schedule = schedule.replace("</p>","")
    print(schedule)
    if(schedule == "No One to One Class Scheduled ! Mentors take One-to-One Class of each individual student. Purchase a course to get One to One Classes with mentors."):
        show = False
    else:
        if (schedule != ""):
            show_date = False
            schedule1=customus.scheduledclass
            print(schedule1)
            schedule1 = schedule1.replace("<p>","")
            schedule1 = schedule1.replace("</p>","")

    fulln=customus.fullname
    questions = questions.replace("<p>", '<p><span style="color:#ffffff">')
    questions = questions.replace("</p>", "</span></p>")
    account_type = ""
    print("show is",show)

    list_speed = datastructure
    list_topic = customus.current_topic
    final_list = get_zip_list_name(list_speed,list_topic,datastructure_temp)

    list_speed = algorithm
    list_topic = customus.current_topic
    final_list_algo = get_zip_list_name(list_speed,list_topic,algorithm_temp)

    list_speed = python_list
    list_topic = customus.current_topic
    final_list_python = get_zip_list_name(list_speed,list_topic,python_list_temp)
    
    list_speed = flask_list
    list_topic = customus.current_topic
    final_list_flask = get_zip_list_name(list_speed,list_topic,flask_list_temp)
    
    list_speed = django_list
    list_topic = customus.current_topic
    final_list_django = get_zip_list_name(list_speed,list_topic,django_list_temp)
    
    list_speed = ml_list
    list_topic = customus.current_topic
    final_list_ml = get_zip_list_name(list_speed,list_topic,ml_list_temp)

    context = {
        'questions':questions ,
        'schedule' :schedule,
        'fulln':fulln,
        'saturday': saturday,
        'sunday': sunday,
        'show': show,
        'link':link,
        'uni_strt': uni_strt,
        'uni_end': uni_end,
        'enroll_list': enroll_list,
        'course_id':course_id,
        'show_date':show_date,
        'schedule1' :schedule1,
        'show_course':show_course,
        'account_type':account_type,
        'final_list':final_list,
        'final_list_algo':final_list_algo,
        'final_list_python':final_list_python,
        'final_list_flask':final_list_flask,
        'final_list_django':final_list_django,
        'full_enroll_list':full_enroll_list,
        'final_list_ml':final_list_ml,
        'showit':showit,        
    }
    return render(request, 'newtheme/mylearning.html',context=context)


def get_zip_list_name(list_speed,list_topic,temp_list):
    label = []
    mark = []
    for i in list_speed:
        index = list_topic.find(i)
        index = int(index) + int(len(i)) + 1

        note_list = Note.objects.filter(label=i).all()
        last_index = index + len(note_list)

        temp_list_topic = list_topic[index:last_index]
        if(temp_list_topic.find('0')==-1):
            mark.append(True)
        else:
            mark.append(False)
    for i in temp_list:
        label.append(i)
    
    final_list = zip(label,mark)
    return final_list


def mentor_form(request):
    login_type = mentor_or_not(request.user)
    # login_type = localStorage.getItem("type") if localStorage.getItem("type") else " "
    # print("!!!!!!!!!!!!!!!!!!",login_type)
    if (login_type == "mentor"):
        return redirect('mentordashbord')
    if(login_type == "faculty"):
        return redirect('facultydashboard')
    if(login_type=="ambassador"):
        return redirect('ambassdordashboard')
    if request.method == 'POST':
        resume = request.FILES.get('resume', False)
        print("resume is ",resume)
        name = request.POST["fname"]
        email = request.POST["email"]
        phone =  request.POST["phone"]
        ava = request.POST["ava"]
        ach = request.POST["ach"]
        subject = request.POST["sub"]
        ment = Mentor_Lead(name = name, email=email, phone=phone, availability= ava, subject=subject,achievements= ach, resume= resume )
        ment.save()
        return redirect('/')
        # return render(request, 'newtheme/mentor_lead_form.html' )
    else:
        print("working on forms")
        return render(request, 'newtheme/mentor_lead_form.html' )
  

def Round_Time():
    y = dt.now().time()
    
    time = str(y).split(':')

    if int(time[0]) > 12 :
        time[0]= int(time[0]) - 12

    now_time = int(time[0])
    return str(now_time)+":00:00" , str(now_time+1)+":00:00" , str(now_time+2)+":00:00" , str(now_time+3)+":00:00"



def time_slot(request):

    name  = Mentor_user.objects.get(fullname ="Mentor1")
    time1 , time2 , time3 , time4 = Round_Time()
    print(name.created_date)
    All_Mentors1 = Time_Slot.objects.filter(from_time=time1) 
    All_Mentors2 = Time_Slot.objects.filter(from_time=time2) 
    All_Mentors3 = Time_Slot.objects.filter(from_time=time3) 
    All_Mentors4 = Time_Slot.objects.filter(from_time=time4) 
    Mentors_list1 = []
    Mentors_list2 = []
    Mentors_list3 = []
    Mentors_list4 = []
    Total_Mentor1 = 0
    Total_Mentor2 = 0
    Total_Mentor3 = 0
    Total_Mentor4 = 0
    print(All_Mentors1 , All_Mentors2 , All_Mentors3 , All_Mentors4)
    print(time1 , time2 , time3 , time4)
    
    if len(All_Mentors1) >=1:
        Total_Mentor1 = len(All_Mentors1[0].mentor.all())
        for Mentor in All_Mentors1[0].mentor.all():
            Mentors_list1.append(Mentor.fullname)

    if len(All_Mentors2) >=1:      
        Total_Mentor2 = len(All_Mentors2[0].mentor.all())  
        for Mentor in All_Mentors2[0].mentor.all():
            Mentors_list2.append(Mentor.fullname)

    if len(All_Mentors3) >=1:
        Total_Mentor3 = len(All_Mentors3[0].mentor.all())
        for Mentor in All_Mentors3[0].mentor.all():
            Mentors_list3.append(Mentor.fullname)
    
    if len(All_Mentors4) >=1:
        Total_Mentor4 = len(All_Mentors4[0].mentor.all())
        for Mentor in All_Mentors4[0].mentor.all():
            Mentors_list4.append(Mentor.fullname)            


    context = {
        
        'At_Time1':time1,
        'Total_Mentor1': Total_Mentor1,
        'Mentors_list1': Mentors_list1,
        
        
        'At_Time2':time2,
        'Total_Mentor2': Total_Mentor2,
        'Mentors_list2': Mentors_list2,

        'At_Time3':time3,
        'Total_Mentor3': Total_Mentor3,
        'Mentors_list3': Mentors_list3,

        'At_Time4':time4,
        'Total_Mentor4': Total_Mentor4,
        'Mentors_list4': Mentors_list4,
    }    
    data = json.dumps(context , indent=4, sort_keys=True, default=str)
    return HttpResponse(data , content_type= 'application/json')



@login_required(login_url='/accounts/login/')
def groups_mentor(request):
    mentor = Mentor_user.objects.get(user = request.user)
    groups = mentor.groupalloted.all()
    print("alloted students")
   # print(groups.group_members.all())
    context={
        'groups':groups,
    }
    return render(request,'newtheme/groups_mentor_view.html',context=context)

@login_required(login_url='/accounts/login/')
def single_group(request,stu_id):
    members=Groups_learn.objects.filter(id=stu_id).all()
    groupedit= Groups_learn.objects.get(id=stu_id)

    id = stu_id
    linknow = groupedit.link
    quesnow = groupedit.questionsallotted
    context={
        'members':members,
        'id':id,
        'linknow':linknow,
        'quesnow':quesnow,
    }
    return render(request, 'newtheme/single_group.html', context)


@login_required(login_url='/accounts/login/')
def groupsave(request,stu_id):
    group= Groups_learn.objects.get(id=stu_id)
    link = request.POST.get("link")
    #topic = request.POST.get("topic")
    ques = request.POST.get("que")
    print("link is",link)
    #print("link is",topic)
    print("questions is ", ques)
    group.link=link
    group.questionsallotted = ques
    group.save()
    for i in group.group_members.all():
        student = Custom_User.objects.get(id=i.id)
        student.link = link
        #stu.current_topic = topic
        student.questionsallotted = ques
        #student.scheduledclass = cla
        student.save()
    url = "/single_group/" + str(stu_id)
    return redirect(url)



