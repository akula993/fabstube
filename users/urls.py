from django.urls import path, include

from users.views import Register, AccountView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('accounts/profile/<slug:slug>/', AccountView.as_view(), name='profile')

]
