from django.urls import path
from accounts.views import SignUpView, CustomLoginView, UsersListView, UserCreateView, user_links

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'), name='login'),
    path('users/', UsersListView.as_view(), name='users'),
    path('users/create/', UserCreateView.as_view(), name='users_create'),
    path('user/<int:user_id>/links/', user_links, name='user_links_ajax'),
]
