from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('instructor', views.InstructorAPI,)
router.register('course', views.CourseAPI,)

urlpatterns = [
    path('', include(router.urls)),
]