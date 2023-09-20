from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Workout, Exercise, Set
from django.contrib.auth.models import User
from .serializers import workoutSerializer, exerciseSerializer, setSerializer
from rest_framework.permissions import IsAuthenticated 

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint': '/',
            'method': 'GET',
            'body' : None,
            'description' : 'List of the endpoints'
        }
    ]

    return(routes)

########################################################
## Workout Views 
########################################################
class WorkoutView(APIView):
    #permission_classes = (IsAuthenticated,)
    # Endpoint - /workout/
    # Gets all of the workouts that are currently stored
    @api_view(['GET'])
    def getWorkouts(request):
        user_id = request.user
        workouts = Workout.objects.filter(user=user_id)

        serializer = workoutSerializer(workouts, many=True)
        return Response(serializer.data)

    # Endpoint - /workout/<str:pk>
    # Get a single workouts based on a specific value passed in through the URL
    @api_view(['GET'])
    def getWorkout(request,pk):
        user_id = request.user.id
        workout = Workout.objects.get(id=pk, user=user_id)

        serializer = workoutSerializer(workout, many=False)
        return Response(serializer.data)

    # Endpoint - '/workout/create'
    # Create a workout
    @api_view(['POST'])
    def createWorkout(request):
        data = request.data

        workout = Workout.objects.create(
            user = User.objects.get(request.user.id),
            focus = data['focus'],
            preworkout = data['preworkout'],
            totalWeight = data['totalWeight'],
        )

        serializer = workoutSerializer(workout, many=False)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/update'
    # Update a workout
    @api_view(['PUT'])
    def updateWorkout(request,pk):
        user_id = request.user.id
        workout = Workout.objects.get(id=pk, user=user_id)
        serializer = workoutSerializer(workout,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response("Update Failure: Fields are not valid")
        

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/delete'
    # Delete a workout
    @api_view(['DELETE'])
    def deleteWorkout(request,pk):
        user_id = request.user.id
        workout = Workout.objects.get(id=pk, user=user_id)
        workout.delete()

        return Response("Workout Deleted")

########################################################
## Exercise Views
########################################################
class ExerciseView(APIView):
    permission_classes = (IsAuthenticated,)

    # Endpoint - /exercise/<str:workoutId>
    # Gets all of the exercises that are currently stored for a given workout
    @api_view(['GET'])
    def getExercises(request,workoutId):
        user_id = request.user.id
        exercises = Exercise.objects.filter(workout_id=workoutId, user=user_id)

        serializer = exerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:pk>/'
    # Gets a specific exercise for an associated workout
    @api_view(['GET'])
    def getExercise(request,workoutId,pk):
        user_id = request.user.id
        exercise = Exercise.objects.get(id=pk,workout_id=workoutId, user = user_id)

        serializer = exerciseSerializer(exercise, many=False)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/exercise/create'
    # Create an exercise with the rep and weight value
    @api_view(['POST'])
    def createExercise(request,workoutId):
        data = request.data

        exercise = Exercise.objects.create(
            workout = Workout.objects.get(id=workoutId),
            name = data['name'],
            user = request.user.id,
            target = data['target'],
            repGoal = data['repGoal'],
            equipment = data['equipment'],
            notes = data['notes'],
        )

        serializer = exerciseSerializer(exercise, many=False)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/update'
    # Update a set with the rep and weight
    @api_view(['PUT'])
    def updateExercise(request,workoutId,pk):
        user_id = request.user.id

        exercise = Exercise.objects.get(id=pk,workout_id=workoutId, user=user_id)
        serializer = exerciseSerializer(exercise,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response("Update Failure: Fields are not valid")
        

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/delete'
    # Delete a set with the rep, weight and exercise association
    @api_view(['DELETE'])
    def deleteExercise(request,workoutId,pk):

        exercise = Exercise.objects.get(id=pk,workout_id=workoutId)
        exercise.delete()

        return Response("Exercise Deleted")

########################################################
## Set Views
########################################################
class SetView(APIView):
    permission_classes = (IsAuthenticated,)
    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/set/'
    # Gets all of the sets for an associated exercise
    @api_view(['GET'])
    def getSets(request, exerciseId,workoutId):
        user_id = request.user.id
        sets = Set.objects.filter(exercise_id=exerciseId, user=user_id)
        

        serializer = setSerializer(sets, many=True)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>'
    # Gets a specific set for an associated exercise
    @api_view(['GET'])
    def getSet(request,pk,exerciseId,workoutId):
        user_id = request.user.id
        set = Set.objects.get(id=pk,exercise_id=exerciseId, user=user_id)

        serializer = setSerializer(set, many=False)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/set/create'
    # Create a set with the rep and weight value
    @api_view(['POST'])
    def createSet(request,exerciseId,workoutId):
        data = request.data

        set = Set.objects.create(
            exercise = Exercise.objects.get(id=exerciseId,workout_id=workoutId),
            weight = data['weight'],
            reps = data['reps'],
        )

        serializer = setSerializer(set, many=False)
        return Response(serializer.data)

    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/update'
    # Update a set with the rep and weight
    @api_view(['PUT'])
    def updateSet(request,exerciseId,workoutId,pk):
        user_id = request.user.id

        set = Set.objects.get(id=pk,exercise_id=exerciseId,user=user_id)
        serializer = setSerializer(set,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response("Update Failure: Fields are not valid")


    # Endpoint - 'workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/delete'
    # Delete a set with the rep, weight and exercise association
    @api_view(['DELETE'])
    def deleteSet(request,exerciseId,workoutId,pk):

        set = Set.objects.get(id=pk,exercise_id=exerciseId)
        set.delete()

        return Response("Set Deleted")