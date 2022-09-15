from django.urls import path, include
from .views import Custom_Login , Mentor_Login , Course_data , Student_detail , CourseAll , BlogAll , InterviewAll
from .views import Blogs_data , Interview_data,Group_detail

urlpatterns = [

    path('Customlogin',Custom_Login.as_view()),
    path('Mentorlogin',Mentor_Login.as_view()),
    path('Course',Course_data.as_view()),
    path('Student',Student_detail.as_view()),
    path('CourseAll',CourseAll.as_view()),
    path('BlogsAll',BlogAll.as_view()),
    path('InterviewsAll',InterviewAll.as_view()),
    path('Blogs',Blogs_data.as_view()),
    path('Interviews',Interview_data.as_view()),
    path('Group',Group_detail.as_view()),


]