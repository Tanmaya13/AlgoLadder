from rest_framework import serializers
from myapp.models import Custom_User, Mentor_user, Courses,  InterviewExperiences, Blogs, Groups_learn


class BlogSerailizerAll(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['id', 'name', 'logo']


class IneterViewSeralizerAll(serializers.ModelSerializer):
    class Meta:
        model = InterviewExperiences
        fields = ['id', 'name', 'logo']


class BlogSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class IneterViewSeralizer(serializers.ModelSerializer):
    class Meta:
        model = InterviewExperiences
        fields = '__all__'


class CouseIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'logo']


class CourseSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        depth = 1


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'logo']
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ['fullname', 'phone', 'link', 'questionsallotted',
                  'scheduledclass', 'mentors_alloted']


class MentorSerializerIdFullname(serializers.ModelSerializer):
    class Meta:
        model = Mentor_user
        fields = ['id', 'user', 'fullname']


class CustomSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    mentors_alloted = MentorSerializerIdFullname(many=True)

    class Meta:
        model = Custom_User
        fields = ['user', 'method_type', 'fullname', 'email', 'created_date',  'university', 'universitystartyear', 'universityendyear', 'universitycgpa', 'points', 'achievements', 'phone',
                  'current_topic', 'image', 'points_earned', 'problems_solved', 'start_date', 'end_date', 'questionsallotted', 'scheduledclass', 'link', 'referral_code', 'mentors_alloted', 'courses']

    def get_courses(self, obj):
        courses = obj.courses_set.all()
        response = CoursesSerializer(courses, many=True).data
        return response
        # fields = '__all__'


class GroupDetailSerializer(serializers.ModelSerializer):
    group_members = CustomSerializer(many=True)

    class Meta:
        model = Groups_learn
        fields = ['id', 'name', 'link', 'questionsallotted',
                  'group_members']


class GroupNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups_learn
        fields = ['id', 'name', 'link', 'questionsallotted']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups_learn
        fields = ['link', 'questionsallotted']


class MentorSerializer(serializers.ModelSerializer):
    allotedstudents = CustomSerializer(many=True)
    groupalloted = GroupNameSerializer(many=True)

    class Meta:
        model = Mentor_user
        fields = ['user', 'fullname', 'email', 'created_date',
                  'allotedstudents', 'course_alloted', 'groupalloted']
