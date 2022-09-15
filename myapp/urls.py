from django.urls import path, include
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('about-us', views.About_Us),
    # path('signup_submit',views.Signup_Submit),
    # path('login_submit',views.Login_Submit),
    # path('signup',views.Signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('activate/<str:uidb64>/<str:token>', views.activate, name = 'activate'),
    path('submit-code/', views.Submit_Code),
    path('submit-code-problem', views.Submit_Code_Problem),
    # path('get-leaderboard', views.Get_Leaderboard),
    path('logintodashboard', views.logintodashboard),
    path('profile/<str:username>', views.Profile),
    # path('get-profile', views.Get_Profile),
    # path('get-note-content', views.Get_Note, name='getnote'),
    # path('get-all-notes', views.Get_All_Notes),
    # path('get-problems', views.Get_Problems),
    # path('get-domain-problems-list', views.Get_Domain_Problems_List),
    #
    # path('linkedlistquestions', views.linkedlistquestions),
    # path('notes/<str:note_name>', views.Notes),
    # path('<str:note_name>/problems/<str:problem_name>', views.Problems),
    # path('<str:note_name>/problems', views.Problems_List),

    path('', views.home, name='home'),
    path('mylogin', views.Login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.Logout, name='logout'),
    path('algoedge', views.algoedge, name='algoedge'),
    path('practice', views.practice, name='practice'),
    path('courses', views.courses, name='courses'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('courses_detail/<int:course_id>',
         views.courses_detail, name='courses_detail'),
    path('courses_promo/<int:course_id>',
         views.courses_promo, name='courses_promo'),
    path('ide', views.Ide, name='ide'),
    path('blogs', views.blogs, name='blogs'),
    path('ambassador_form', views.ambassador_form, name='ambassador_form'),
    path('blogs/<str:blogs_name>', views.single_blogs, name='single_blogs'),
    path('free_trial', views.free_trial, name='free_trial'),
    path('ambassador', views.ambassador, name='ambassador'),
    path('enroll_now', views.enroll_now, name='enroll_now'),
    path('analyse', views.analyse, name='analyse'),
    path('eg/<str:rid>', views.eg, name='eg'),
    path('about', views.about, name='about'),
    path('ambassdordashboard', views.ambassdordashboard, name='ambassdordashboard'),
    path('problem_list', views.problem_list, name='problem_list'),
    path('problem_list/<str:problem_name>',
         views.single_problem, name='single_problem'),
    path('problem_submit_success', views.problem_submit_success,
         name='problem_submit_success'),

    path('payment_confirmation', views.payment_confirmation,
         name='payment_confirmation'),

    path('facultydashboard', views.facultydashboard, name='facultydashboard'),

    path('note_list', views.note_list, name='note_list'),
    path('ambassador', views.ambassador, name='ambassador'),
    path('note_list/<str:label>/<str:note_name>/<int:course_id>',
         views.single_note, name='single_note'),
    path('note_mentor/<str:label>/<str:note_name>/<int:course_id>',
         views.single_note_mentor, name='single_note_mentor'),
    path('onotes_list/<int:course_id>', views.onotes_list, name='onotes_list'),
    path('applyCoupon/<int:course_id>', views.applyCoupon, name='applyCoupon'),

    path('video_list', views.video_list, name='video_list'),


    path('contest_list', views.contest_list, name='contest_list'),
    path('contests/<str:contest_name>', views.contest, name='contest'),
    path('accounts/login/', views.Login, name='Login'),


    path('profile', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),

    path('generateCode', views.generateCode, name='generateCode'),

    path('interview_experiences', views.interview_experiences,
         name='interview_experiences'),
    path('interview_experiences/<str:experience_name>',
         views.single_experience, name='single_experience'),
    path('couponapply', views.couponapply, name='couponapply'),
    path('validate_coupon_code/', views.validate_coupon_code,
         name='validate_coupon_code'),
    path('mylearning', views.mylearning, name='mylearning'),
    path('myreferral', views.myreferral, name='myreferral'),
    path('myteaching', views.mentordashbord, name='mentordashbord'),
    path('ide2', views.Idementor, name='Idementor'),
    path('coursementor', views.coursementor, name='coursementor'),
    path('home', views.home, name='home'),
    path('single_group/<int:stu_id>', views.single_group, name='singlegroup'),
    path('student/<int:stu_id>', views.student, name='student'),
    path('studentsave/<int:stu_id>', views.studentsave, name='studentsave'),
    path('groupsave/<int:stu_id>', views.groupsave, name='groupsave'),

    path('mentor_form', views.mentor_form, name='mentor_form'),
    path('time_slot', views.time_slot, name='time_slot'),
    path('groupsmentor', views.groups_mentor, name='groupsmentor'),
     path('doubt',views.doubt,name='doubt'),



    # path('contestone', views.contestone, name='contestone'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
