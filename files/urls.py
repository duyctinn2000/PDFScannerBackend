from django.urls import path
from .views import FileList,FileDetaiView

urlpatterns = [
    path('',FileList.as_view()),
    path('<int:id>',FileDetaiView.as_view()),
]
