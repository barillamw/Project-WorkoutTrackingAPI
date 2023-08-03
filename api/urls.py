from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('workout',views.WorkoutView.getWorkouts),
    path('workout/create/',views.WorkoutView.createWorkout),
    path('workout/<str:pk>/',views.WorkoutView.getWorkout),
    path('workout/<str:pk>/update/',views.WorkoutView.updateWorkout),
    path('workout/<str:pk>/delete/',views.WorkoutView.deleteWorkout),
    path('workout/<str:workoutId>/exercise', views.getExercises),
    path('workout/<str:workoutId>/exercise/create', views.createExercise),
    path('workout/<str:workoutId>/exercise/<str:pk>/',views.getExercise),
    path('workout/<str:workoutId>/exercise/<str:pk>/update',views.updateExercise),
    path('workout/<str:workoutId>/exercise/<str:pk>/delete',views.deleteExercise),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/', views.getSets),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/create', views.createSet),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/', views.getSet),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/update', views.updateSet),
    path('workout/<str:workoutId>/exercise/<str:exerciseId>/set/<str:pk>/delete', views.deleteSet),
]