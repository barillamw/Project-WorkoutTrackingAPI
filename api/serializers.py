from rest_framework.serializers import ModelSerializer
from .models import Workout, Exercise, Set

class workoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class exerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class setSerializer(ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
