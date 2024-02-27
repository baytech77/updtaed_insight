from rest_framework.serializers import ModelSerializer
from home_app.models import Courses


class CourseSerializer(ModelSerializer):
  class Meta:
    model = Courses
    fields = ('id','title', 'description','noOfStudent', 'language','image', 'created_by' )