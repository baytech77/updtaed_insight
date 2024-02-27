from django.urls import path
from  .views import CourseListApiView, CourseDetailApiView, DeleteApiView, CreateApiView, UpdateApiView

urlpatterns = [
    path('', CourseListApiView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailApiView.as_view(), name='course-detail'),
    path('delete/<int:pk>/', DeleteApiView.as_view(), name='course-delete'),
    path('create/', CreateApiView.as_view(), name='course-create'),
    path('update/<int:pk>/', UpdateApiView.as_view(), name='course-update'),
]
