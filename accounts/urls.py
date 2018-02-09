from django.urls import path, re_path, include
from accounts import views as accounts_view
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('login/', accounts_view.LoginView.as_view()),
    path('logout/', refresh_jwt_token),
    path('user/', accounts_view.UserView.as_view()),
]
