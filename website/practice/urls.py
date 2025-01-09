from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('toefl/', views.toefl_page, name='toefl_page'),
    path('toefl/reading/', views.toefl_reading, name='toefl_reading'),
    path('toefl/listening/', views.toefl_listening, name='toefl_listening'),
    path('toefl/writing/', views.toefl_writing, name='toefl_writing'),
    path('toefl/speaking/', views.toefl_speaking, name='toefl_speaking'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view,name='logout'),
    path('account/settings/', views.account_settings, name='account_settings'),

    # Quiz generation API
    path('quiz/api/reading/', views.quiz_api_view, name='quiz_api'),

]

