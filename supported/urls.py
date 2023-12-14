from django.urls import path
from supported import views

urlpatterns = [
    path('supported/', views.SupporterList.as_view()),
    path('supported/<int:pk>/', views.SupporterDetail.as_view())
]
