from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from home_app.models import Courses
from .serializers import CourseSerializer
# Create your views here.


class CourseListApiView(ListAPIView): # get request to read only the  data in the models
  queryset = Courses.objects.all()
  serializer_class = CourseSerializer
  
  
class CourseDetailApiView(RetrieveAPIView) :# getting individual course details
  queryset = Courses.objects.all()
  serializer_class = CourseSerializer
  
  
class DeleteApiView(RetrieveDestroyAPIView) :# deleting individual course
  queryset = Courses.objects.all()
  serializer_class = CourseSerializer
  
  
class CreateApiView(ListCreateAPIView):
  queryset = Courses.objects.all()
  serializer_class = CourseSerializer
  
  
class UpdateApiView(RetrieveUpdateAPIView):
  queryset = Courses.objects.all()
  serializer_class = CourseSerializer  