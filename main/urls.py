from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name = 'main'),
    path('news/', views.MainPage.as_view(), name = 'main'),
    path('newest/', views.NewestView.as_view(), name = 'newest'),
    path('front/', views.FrontView.as_view(), name= 'front'),
    path('newcomments/', views.NewCommentsView.as_view(), name = 'newcomments'),
    path('ask/', views.AskView.as_view(), name = 'ask'),
    path('show/', views.ShowView.as_view(), name = 'show'),
    path('jobs/', views.JobsView.as_view(), name = 'jobs'),
    path('submit/', views.SubmitView.as_view(), name = 'submit'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('item/', views.ItemView.as_view(), name = 'item'),
    path('user/', views.UserView.as_view(), name = 'user'),
    path('context/', views.ContextView.as_view(), name = 'context'),
]