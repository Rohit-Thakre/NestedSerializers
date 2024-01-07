from  api import models
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    # instructor = serializers.SlugRelatedField(read_only=True,slug_field='name')
    ##<instructor> name must be equal to model's instructor field.
    ## since this is Course ---> Instructor (Many to one relationship) 
   ##-------------------------------------------------------------------
    
    # instructor = serializers.StringRelatedField()
    class Meta: 
        model = models.Course
        fields = ['id','name','rating','instructor']
        # depth = 1

class InstructorSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True)
    
    courses = serializers.StringRelatedField(many=True,)
    ## here Instructor table don't have course field, but since we have defined in 
    ## related_name in Instructor table  as courses, if we change the name courses in table then also have to rename it over here too. 

    # courses = serializers.SlugRelatedField(many=True,read_only=True, slug_field='rating')
    # courses = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    # change the value at slug_field as in course table's fields which want to fetch

    class Meta: 
        model = models.Instructor
        fields = ['id', 'name','courses']
        # depth = 1

## depth is user when we want to fetch all the data
## serializers.StingRelatedField() is used when want to fetch the names insted of id
## serializers.SlugRelatedField(slug_field = 'field_name') is used when want to fetch specific field unlike StringRelated field which returns __str__ method

