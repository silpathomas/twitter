from django.urls import path
from account.views import RegisterView
from . import views as account
# from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # Your URLs...
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login', account.login_user, name="login"),
    path('logout', account.logout_user, name="logout"),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
