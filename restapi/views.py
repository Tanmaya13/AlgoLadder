from django.shortcuts import render
from .serializers import CustomSerializer, MentorSerializer,  CoursesSerializer, CourseSerailizer, StudentSerializer, CouseIdSerializer, GroupDetailSerializer
from .serializers import BlogSerailizer, BlogSerailizerAll, IneterViewSeralizer, IneterViewSeralizerAll, GroupSerializer
from rest_framework.response import Response
from myapp.models import Custom_User, Mentor_user, Courses, Blogs, InterviewExperiences, Groups_learn
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as l_login
from django.contrib.auth import authenticate
from myapp.forms import SignUpForm


class Custom_Login(APIView):

    # http://127.0.0.1:8000/Customlogin?username=q&password=asghasgh
    def get(self, request):
        Info = request.GET
        username = Info["username"]
        password = Info["password"]
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            detail = Custom_User.objects.get(user=user)
            serializer = CustomSerializer(detail)
            return Response(serializer.data,   status=status.HTTP_200_OK)
        else:
            detail = "Custom_User matching query does not exist"
            return Response(detail, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        form = SignUpForm(request.data)
        print(request.data)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')

            user.custom_user.email = form.cleaned_data.get('email')
            user.custom_user.phone = form.cleaned_data.get('phone')
            user.custom_user.fullname = form.cleaned_data.get('fullname')
            user.save()

            return Response(status=status.HTTP_201_CREATED)

        else:
            error_detail = []
            for field in form:
                for error in field.errors:
                    print(error)
                    error_detail.append(error)

            return Response(error_detail, status=status.HTTP_400_BAD_REQUEST)


'''
{
    "username":"Kuanl123",
    "password1":"kunal234",
    "password2":"kunal234",
    "email":"lunsk@gmail.com",
    "fullname":"Kuanl Kumar",
    "phone":"6643545"
    Format for Post Request (Json body)
}
'''


class Mentor_Login(APIView):

    #  http://127.0.0.1:8000/Mentorlogin?username=newmentor&password=mentor123
    def get(self, request):
        info = request.GET
        print(info)
        username = info["username"]
        password = info["password"]
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            detail = Mentor_user.objects.get(user=user)
            serializer = MentorSerializer(detail)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Course_data(APIView):

    # http://127.0.0.1:8000/Course?id=1
    def get(self, request):
        info = request.GET
        Id = info['id']
        print(Id)
        try:
            Course = Courses.objects.get(id=Id)
            print(Course)
            serializer = CourseSerailizer(Course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = "Course doesn't exist"
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class Student_detail(APIView):

    def get(self, request):

        # url = http://127.0.0.1:8000/Student?id=100 For get request
        info = request.GET
        ID = info['id']
        try:
            details = Custom_User.objects.get(id=ID)
        except:
            data = "No user Exist with this Id"
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        serailizer = StudentSerializer(details)
        return Response(serailizer.data, status=status.HTTP_200_OK)

    def put(self, request):
        '''
        url =  http://127.0.0.1:8000/Student
        Method = Put
        Body (JSon)
        {
            "id":"1",
            "link":"https://meet.google.com/skk-dyjq-bpp",
            "questionsallotted":"Kuanl Kumar",
            "scheduledclass":"6643545"
        }
        '''

        res = request.data
        Id = res['id']
        details = Custom_User.objects.get(id=Id)
        res['fullname'] = details.fullname
        res['phone'] = details.phone
        context = {
            'fullname': res['fullname'],
            'phone': res['phone'],
            'link': res['link'],
            'questionsallotted': res['questionsallotted'],
            'scheduledclass': res['scheduledclass']
        }
        serializer = StudentSerializer(details, data=context)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CourseAll(APIView):
    # http://127.0.0.1:8000/CourseAll
    def get(self, request):
        course = Courses.objects.all()
        data = {}
        for val, Course in enumerate(course):
            serializer = CouseIdSerializer(Course)
            data[val+1] = serializer.data
            print(data)

        return Response(data, status=status.HTTP_200_OK)


class BlogAll(APIView):
    # http://127.0.0.1:8000/BlogsAll
    def get(self, request):
        blogs = Blogs.objects.all()
        data = {}
        for val, Blog in enumerate(blogs):
            serializer = BlogSerailizerAll(Blog)
            data[val+1] = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class InterviewAll(APIView):
    # http://127.0.0.1:8000/InterviewsAll
    def get(self, request):
        interview = InterviewExperiences.objects.all()
        data = {}

        for val, Interview in enumerate(interview):
            serializer = IneterViewSeralizerAll(Interview)
            data[val+1] = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class Blogs_data(APIView):

    # http://127.0.0.1:8000/Blogs?id=1
    def get(self, request):
        info = request.GET
        Id = info['id']
        print(Id)
        try:
            Blog = Blogs.objects.get(id=Id)
            print(Blog)
            serializer = BlogSerailizer(Blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = "Blog doesn't exist"
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class Interview_data(APIView):

    # http://127.0.0.1:8000/Interviews?id=1
    def get(self, request):
        info = request.GET
        Id = info['id']
        print(Id)
        try:
            Interview = InterviewExperiences.objects.get(id=Id)
            print(Interview)
            serializer = IneterViewSeralizer(Interview)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = "Interview doesn't exist"
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class Group_detail(APIView):
    def get(self, request):

        # url = http://127.0.0.1:8000/Group?id=100 For get request
        info = request.GET
        ID = info['id']
        try:
            details = Groups_learn.objects.get(id=ID)
        except:
            data = "No Group Exist with this Id"
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        serailizer = GroupDetailSerializer(details)
        return Response(serailizer.data, status=status.HTTP_200_OK)

    def put(self, request):
        '''
        url =  http://127.0.0.1:8000/Group
        Method = Put
        Body (JSon)
        {
            "id":"1",
            "link":"https://meet.google.com/skk-dyjq-bpp",
            "questionsallotted":"Kuanl Kumar"
        }
        '''

        res = request.data
        Id = res['id']
        print("cool1")
        details = Groups_learn.objects.get(id=Id)
        for i in details.group_members.all():
            i.link = res['link']
            i.questionsallotted = res['questionsallotted']
            i.save()
        context = {
            'link': res['link'],
            'questionsallotted': res['questionsallotted'],
        }
        print("cool")
        serializer = GroupSerializer(details, data=context)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
