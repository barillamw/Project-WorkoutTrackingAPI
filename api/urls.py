from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('workout',views.WorkoutView.getWorkouts),
    path('workout/create/',views.WorkoutView.createWorkout),
    path('workout/<str:pk>/',views.WorkoutView.getWorkout),
    path('workout/<str:pk>/update/',views.WorkoutView.updateWorkout),
    path('workout/<str:pk>/delete/',views.WorkoutView.deleteWorkout),
    path('workout/<str:workoutId>/exercise', views.ExerciseView.getExercises),
    path('workout/<str:workoutId>/exercise/create', views.ExerciseView.createExercise),
    path('workout/<str:workoutId>/exercise/<str:pk>/',views.ExerciseView.getExercise),
    path('workout/<str:workoutId>/exercise/<str:pk>/update',views.ExerciseView.updateExercise),
    path('workout/<str:workoutId>/exercise/<str:pk>/delete',views.ExerciseView.deleteExercise),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/', views.SetView.getSets),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/create', views.SetView.createSet),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/', views.SetView.getSet),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/update', views.SetView.updateSet),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/delete', views.SetView.deleteSet),
]