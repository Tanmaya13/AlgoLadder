from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
import os
from glob import glob
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from myapp.models import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def home(request):
    return HttpResponse("hello")

def mentor_or_not(usertype):
    
    # mentor = Mentor_user.objects.all()
    # for i in mentor:
    #     if i.user == usertype:
    #         return "mentor"
    # faculty = Faculty_user.objects.all()
    # for i in faculty:
    #     if i.user == usertype:
    #         return "faculty"
    ambassador = AmbassadorUser.objects.all()
    for i in ambassador:
        if i.user == usertype:
            return "ambassador"
            # localStorage.setItem("type","mentor")
    return "student"

def all_contests(request):
    print("in contest*******")
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contests = Contests.objects.all()
    current_time = datetime.now(timezone.utc)
    print(current_time)
    current_contest = []
    past_contest = []
    for i in contests:
        print(i.name)
        print(i.start_on)
        if(current_time > i.end_on):
            past_contest.append(i)
        else:
            current_contest.append(i)
    past_list = True
    current_list = True
    if len(past_contest)==0 :
        past_list = False
    if len(current_contest)==0:
        current_list = False
    context = {
        'contests': contests,
        'past_contest':past_contest,
        'current_contest':current_contest,
        'past_list':past_list,
        'current_list':current_list,
        'account_type':account_type
    }

    return render(request, 'all_contest.html', context)


@login_required(login_url='/accounts/login/')
def single_contest(request, contest_name):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contest = Contests.objects.get(name = contest_name)

    start_time = contest.start_on
    end_time = contest.end_on
    now = datetime.now(timezone.utc)

    print("start time = ", start_time)
    print("current time = ", now)
    print("difference = ", start_time - now)

    if start_time > now :
        status = "U"

    if start_time <= now and end_time > now:
        status = "A"

    if end_time < now:
        status = "E"

    context = {
        'contest': contest,
        'status':status,
        'start_time': start_time,
        'end_time': end_time,
        'account_type':account_type
    }

    return render(request, 'single_contest.html', context)




def active_contest(request, contest_name):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    all = UserProfile.objects.all()
    
   
    contest = Contests.objects.get(name = contest_name)
    
    usr = request.user
    
    p = False

    for i in all:
        if i.user == request.user:
            p = True


    if p:
        print("user exists" , "###################")
        if contest.check == 'Private':
            Email_split = str(usr.email).split('.')
            const = Email_split[0].split('@')
            print(const)
            if const[1].lower() != contest.contraint:
                start_time = contest.start_on
                end_time = contest.end_on
                now = datetime.now(timezone.utc)

                print("start time = ", start_time)
                print("current time = ", now)
                print("difference = ", start_time - now)

                if start_time > now :
                    status = "U"

                if start_time <= now and end_time > now:
                    status = "A"

                if end_time < now:
                    status = "E"

                context = {
                    'contest': contest,
                    'status':status,
                    'start_time': start_time,
                    'end_time': end_time,
                    'No':'1',
                    'account_type':account_type
                }
                return render(request, 'single_contest.html', context)
    else:
        obj = UserProfile(user=request.user, contest_name=contest_name, score=0, start_time=datetime.now(timezone.utc),penalty_time=0)
        print(contest.check , "%%%%%%%%%%%%%%%%")
        if contest.check == 'Private':
            Email_split = str(usr.email).split('.')
            const = Email_split[0].split('@')
            print(const)
            if const[1].lower() == contest.contraint:
                obj.save()
            else:
                start_time = contest.start_on
                end_time = contest.end_on
                now = datetime.now(timezone.utc)

                print("start time = ", start_time)
                print("current time = ", now)
                print("difference = ", start_time - now)

                if start_time > now :
                    status = "U"

                if start_time <= now and end_time > now:
                    status = "A"

                if end_time < now:
                    status = "E"

                context = {
                    'contest': contest,
                    'status':status,
                    'start_time': start_time,
                    'end_time': end_time,
                    'No':'1',
                    'account_type':account_type
                }
                return render(request, 'single_contest.html', context)
   
        else:
            obj.save()
    participant = UserProfile.objects.get(user = request.user)
    contest.participants.add(participant)
    print(usr.email , "ds%%%%%%%%%%%%%%%%%%")
    start_time = contest.start_on
    end_time = contest.end_on

    coding_questions = contest.coding_problems.all()
    mcq_questions = contest.mcq_problems.all()
    print(len(coding_questions))
    submission_list = []
    
    submissions = CodingSubmissions.objects.filter(user = participant, contest = contest).all()
    
    for i in range(len(coding_questions)):
        f = 0
        for j in range (len(submissions)):
            print("###############################",coding_questions[i].name,"==",submissions[j].question)
            if(str(coding_questions[i].name) == str(submissions[j].question)):
                if(submissions[j].result == "partial"):
                    submission_list.append("partial")
                if(submissions[j].result == "submitted"):
                    submission_list.append("submitted")
                if(submissions[j].result == "wrong"):
                    submission_list.append("wrong")
                f = 1
        if (f==0):
            submission_list.append("no")
        
    print("start time =", start_time)
    print("end time =", end_time)
    final_list = {}
    for i in range(len(coding_questions)):
        final_list[coding_questions[i]] = submission_list[i]
    print(final_list)
    context = {
        'contest': contest,
        'code': coding_questions,
        'mcq': mcq_questions,
        'start_time': start_time,
        'end_time': end_time,
        'submission_list':submission_list,
        'final_list':final_list,
        'account_type':account_type
    }

    return render(request, 'active_contest.html', context)





@login_required(login_url='/accounts/login/')
def single_problem(request, contest_name, problem_name):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contest = Contests.objects.get(name=contest_name)
    start_time = contest.start_on
    end_time = contest.end_on

    problem = CodingProblems.objects.get(name = problem_name)
    # url = "/activae_contes/contest_id
    #  containt check
    usr = request.user
    if contest.check == 'Private':
        Email_split = str(usr.email).split('.')
        const = Email_split[0].split('@')
        print(const)
        if const[1].lower() != contest.contraint:
            return HttpResponseRedirect('/contest/all_contest')

    # name = problem.name
    # content = problem.question
    #
    # context = {
    #     'name': name,
    #     'content': content
    # }

    # problem = Problem.objects.get(name=problem_name)

    path = os.path.join(BASE_DIR, 'files')

    test_case = path + "/Contests/" + contest_name + "/" + problem_name + "/test-cases/"
    exp_out = path + "/Contests/" + contest_name + "/" + problem_name + "/expected-output/"

    test_paths = glob(test_case + "*.txt")
    test_paths.sort()
    exp_paths = glob(exp_out + "*.txt")
    exp_paths.sort()
    print("############################")
    print("test case path = ", test_case)
    print("expected output paths = ", exp_out)

    l = 0
    tc = 0
    eo = 0
    all_tc = []
    all_eo = []

    for path in test_paths:
        file = open(path, 'r')
        temp = file.read()
        tc = temp
        all_tc.append(tc)
        print(tc)
        print("all tc = ", all_tc)
        l = len(all_tc)
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
        'content': problem.question,
        'points': problem.points,
        'test_cases': all_tc,
        'exp_outs': all_eo,
        'files': files,
        'start_time': start_time,
        'end_time': end_time,
        'contest_name': contest_name,
        'contest':contest,
        'account_type':account_type
    }


    return render(request, 'single_problem.html', context)

@login_required(login_url='/accounts/login/')
def paticipantshow(request,id,id_cont):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contest = Contests.objects.get(id = int(id_cont))
    user = UserProfile.objects.get(id = int(id))
    all_submission = CodingSubmissions.objects.filter(user = user, contest=contest).all()
    context={
        'all_submission':all_submission,
        'contest':contest,
        'account_type':account_type
    }
    return render(request,'all_submission.html',context)

@login_required(login_url='/accounts/login/')
def submissionshow(request,id):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    submission = CodingSubmissions.objects.get(id = int(id))
    print("submission output is",submission.submitted_output)
    context = {
        'submission':submission,
        'account_type':account_type
    }
    return render(request,'single_submission.html',context)

@login_required(login_url='/accounts/login/')
def contestshow(request,id):
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contest = Contests.objects.get(id = int(id))
    print("contest is ", contest)
    users = contest.participants.all()
    custom_user_list = []
    for i in users:
        cust = Custom_User.objects.get(user=i.user)
        custom_user_list.append(cust)
    print("users are",users)
    result = zip(users,custom_user_list)
    context ={
        'participants':users,
        'result':result,
        'id_cont':id,
        'contest':contest,
        'account_type':account_type
    }
    return render(request,'single_contest_check.html',context)



def contest_problem_success(request):
    print("inside problem submit ")
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    if request.method == 'POST':
        contest = request.POST.get('contest')
        p_name = request.POST.get('text')
        points = request.POST.get('p')
        per = request.POST.get('per')
        print("contest is",contest) 
        code = request.POST.get('code')
        current_contest = Contests.objects.get(id = int(contest))
        print("current_contest",current_contest)
        # obj = CodingSubmissions(user=request.user, question=p_name, result=True)
        # obj.save()

        usr = UserProfile.objects.get(user = request.user)
        problem = CodingProblems.objects.get(name = p_name)
        start_time=datetime.now(timezone.utc)
        print("time")
        print(start_time)
        all = CodingSubmissions.objects.filter(user = usr, question = problem,contest = current_contest).all()
        submission = False
        for i in all:
            if i.user==usr and i.question==problem:
                obj1 = CodingSubmissions.objects.get(user = usr, question = problem,contest = current_contest)
                if(int(obj1.marks_obtained)<int(problem.points * float(per))):
                    usr.score = usr.score - obj1.marks_obtained + problem.points * float(per)
                    now= datetime.now(timezone.utc)
                    w=current_contest.start_on - now
                    minutes= w.total_seconds()
                    usr.penalty_time=minutes
                    obj1.marks_obtained = problem.points * float(per)
                if current_contest.runcode:
                    if(int(float(per)) ==1 ):   
                        obj1.result = "submitted"
                        obj1.submitted_output = code
                        usr.start_time=start_time
                        print("time")
                        print(start_time)
                    elif(int(float(per) != 1 ) and obj1.result != "submitted"):
                        obj1.result = "partial"
                        obj1.submitted_output = code
                        usr.start_time=start_time
                        print("time")
                        print(start_time)
                else:
                    obj1.result = "submitted"
                    obj1.submitted_output = code
                    usr.start_time=start_time
                    print("time")
                    print(start_time)
                
                obj1.save()
                usr.save()
                print("already submitted")
                submission = True
                break
        if submission == False:
            if(int(float(per)) ==1 ):
                obj = CodingSubmissions(user=usr,contest = current_contest, question=problem, submitted_output = code,result="submitted", marks_obtained = problem.points * float(per))
                obj.save()
                usr.score = usr.score + (problem.points * float(per))
                now= datetime.now(timezone.utc)
                w=current_contest.start_on - now
                minutes= w.total_seconds()
                usr.penalty_time=minutes
                usr.start_time=start_time
                usr.save()
            elif(per == "0"):
                obj = CodingSubmissions(user=usr,contest = current_contest, question=problem,submitted_output = code,result="wrong", marks_obtained = problem.points * float(per))
                obj.save()
                usr.score = usr.score + (problem.points * float(per))
                 
                usr.save()

            else:
                obj = CodingSubmissions(user=usr,contest = current_contest, question=problem,submitted_output = code, result="partial", marks_obtained = problem.points * float(per))
                obj.save()
                usr.score = usr.score + (problem.points * float(per))
                now= datetime.now(timezone.utc)
                w=current_contest.start_on - now
                minutes= w.total_seconds()
                usr.penalty_time=minutes
                usr.start_time=start_time
                usr.save()







        print("points = ", points)
        print("problem name = ", p_name)
        # print("user = ", obj)



        print("success")
        if(int(float(per)) ==1 ):
            return HttpResponse("Solution Accepted")
        elif(per=="0"):
            return HttpResponse("Wrong Solution")
        else:
            return HttpResponse("Solution Partially Accepted")
 



@login_required(login_url='/accounts/login/')
def leaderboard(request, contest_name):
    print("inside leaderboar")
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contest = Contests.objects.get(name = contest_name)
    participants = contest.participants.all()
    final = []
    usr = request.user
    if contest.check == 'Private':
        Email_split = str(usr.email).split('.')
        const = Email_split[0].split('@')
        print(const)
        if const[1].lower() != contest.contraint:
            return HttpResponseRedirect('/contest/all_contest/'+str(contest_name))
    for participant in participants:
        p = UserProfile.objects.get(user = participant.user)
        n = p.user.username
        s = p.score
        k=str(p.start_time)
        t = p.penalty_time
        temp = [n, s , k,t]
        print(temp)
        final.append(temp)
        print("contestants = ", participant.user)

    final = sorted(final, key = lambda x: (-x[1], x[2]))
    # final.reverse()
    result = []
    if contest.leaderboard:
        for i in range(len(final)):
            temp = final[i]
            temp2 = [i+1 , temp[0],temp[1]]
            result.append(temp2)
    else:
        for i in range(len(final)):
            temp = final[i]
            temp2 = [i+1 , temp[0]]
            result.append(temp2)
   

    print(result)

    context = {
        'result':result,
        'contest_name':contest_name,
        'contest':contest,
        'account_type':account_type
       
    }
    return render(request, 'leaderboard.html', context)


def contestcomplete(request, contest_name):
    print("*******************************************")
    print(contest_name)
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    allboard = LeaderBoard.objects.all()
    
    print(allboard)
    flag = False
    for i in allboard:
        if(i.name == contest_name):
            flag = True
            break
    
    if(flag):
        print("if")
        result = LeaderBoard.objects.get(name=contest_name)
        print(result)

    
    else:
        print("else")
        contest = Contests.objects.get(name = contest_name)
        participants = contest.participants.all()
        final = []
        for participant in participants:
            p = UserProfile.objects.get(user = participant.user)
            n = p.user.username
            s = p.score
            t= p.penalty_time
            temp = [n, s, t]
            final.append(temp)
            print("contestants = ", participant.user)
        final = sorted(final, key = lambda x: (x[1], x[2]))
        final.reverse()
        result = []
        parti = []
        scr = []
        for i in range(len(final)):
            temp = final[i]
            temp2 = [i+1 , temp[0],temp[1]]
            parti.append(temp[0])
            scr.append(temp[1])
            result.append(temp2)
        print(parti)
        print(scr)
        obj = LeaderBoard(name = contest_name, participant = json.dumps(parti) , score = json.dumps(scr))
        obj.save()
        user = UserProfile.objects.all()
        # CodingSubmissions.objects.all().delete()
        for i in user:
            print("!!!!!!!!!!!!!!!!!!!!!!##")
            print(i.score)
            i.score = 0
            i.penalty_time = 0
            i.save()
        result = LeaderBoard.objects.get(name=contest_name)
        print(result)
    context = {
        'result':result,
        'contest_name':contest_name,
        'account_type':account_type
       
    }
    return redirect('single_contest', contest_name = contest_name)

def showleaderboard(request, contest_name):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    login_type = mentor_or_not(request.user)
    account_type = "student"
    if(login_type=="ambassador"):
        account_type = "ambassador"
    contest = Contests.objects.get(name = contest_name)
    usr = request.user
    if contest.check == 'Private':
        Email_split = str(usr.email).split('.')
        const = Email_split[0].split('@')
        print(const)
        if const[1].lower() != contest.contraint:
            return HttpResponseRedirect('/contest/all_contest/'+str(contest_name))
    allboard = LeaderBoard.objects.all()
    # CodingSubmissions.objects.all().delete()
    contest = Contests.objects.get(name = contest_name)
    print(allboard)
    flag = False
    for i in allboard:
        if(i.name == contest_name):
            flag = True

    if(flag):
        entry = LeaderBoard.objects.get(name = contest_name)
        jsonDec = json.decoder.JSONDecoder()
        name = jsonDec.decode(entry.participant)
        src = jsonDec.decode(entry.score)
        result = []
        for i in range(len(name)):
            temp = []
            temp.append(i+1)
            temp.append(name[i])
            if contest.leaderboard:
                temp.append(src[i])
            result.append(temp)
        context = {
            'result': result,
            'show': True,
            'contest_name':contest_name,
            'contest':contest,
            'account_type':account_type
        }

    else:
        context = {
            'value': "There is no entry to show", 
            'show': False,
            'contest_name':contest_name,
            'contest':contest,
            'account_type':account_type
        }
    return render(request, 'leaderboardend.html', context)
    

