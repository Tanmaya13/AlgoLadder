from django.urls import path
from . import views



urlpatterns = [

    path('all_contest', views.all_contests, name='all_contests'),
    path('contestshow/<str:id>', views.contestshow, name='contestshow'),
    path('submissionshow/<str:id>', views.submissionshow, name='submissionshow'),
    path('all_contest/<str:contest_name>', views.single_contest, name='single_contest'),
    path('contestcomplete/<str:contest_name>', views.contestcomplete, name='contestcomplete'),
    path('all_contest/<str:contest_name>/active', views.active_contest, name='active_contest'),
    path('all_contest/<str:contest_name>/active/<str:problem_name>', views.single_problem, name='problem'),
    path('contest_problem_success', views.contest_problem_success, name='contest_problem_success'),
    path('leaderboard/<str:contest_name>', views.leaderboard, name='leaderboard'),
    path('showleaderboard/<str:contest_name>', views.showleaderboard, name='showleaderboard'),
    path('paticipantshow/<str:id>/<str:id_cont>', views.paticipantshow, name='paticipantshow'),


]
