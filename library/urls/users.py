from library.views.users import UserListView, UserRetrieveView

from django.urls import path


urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>', UserRetrieveView.as_view(), name='user-detail'),
]