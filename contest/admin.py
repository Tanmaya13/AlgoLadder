from django.contrib import admin
from contest.models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Contests)
admin.site.register(CodingProblems)
admin.site.register(CodingSubmissions)
admin.site.register(McqProblems)
admin.site.register(McqSubmissions)
admin.site.register(LeaderBoard)