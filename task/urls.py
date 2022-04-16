from django.urls import path
from .views import task, task_detail_view

app_name = "task"
urlpatterns = [
    path('task_list/', task, name="task-list"),
    path('task-detail-view/<str:pk>', task_detail_view, name="task-detail-view"),
]


