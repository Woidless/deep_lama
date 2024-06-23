from django.urls import path, re_path
from .views import login_view, logout_view

urlpatterns = [
    # path('register/', views.RegistrationView.as_view()),
    # path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('forgot/', views.ForgotPasswordView.as_view()),
    # path('restore/', views.RestoreView.as_view()),
    # path('list/', views.UserListViewSet.as_view({'get': 'list'})),
]