from django.urls import path
from blog import views

urlpatterns = [
    path('', views.NewestPostsListAPIView.as_view()),
    path('most_viewed/', views.MostViewedPostsListAPIView.as_view()),
    path('weekly/',views.WeeklyPopularPostsListAPIView.as_view()),
    path('monthly/', views.MonthlyPopularPostsListAPIView.as_view()),
    path('recommended/', views.RecommendedPostsListAPIView.as_view()),
    path('create_post/', views.PostCreateAPIView.as_view()),
]