from django.urls import path
from . import views
from .views import ProfileListView, remove_from_friend, send_invitations, ProfileDetailView

app_name="profiles"

urlpatterns = [
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path("myprofile/", views.my_profile_view, name="my-profile-view"),
    path("my-invites/", views.invite_received, name="my-invites-view"),#someone send me invitations
    path('my-invites/acctept/', views.accept_invitaions, name='accept-invite'),
    path('my-invites/reject/', views.reject_invitations, name='reject-invite'),
    path("send-invite/", views.send_invitations, name="send-invite"),
    path('invited-profiles/', views.invite_profile_list_view, name='invited-profiles-view'),#invited by me
    path("remove-friend/", views.remove_from_friend, name="remove-friend"),
    path("<slug>/", ProfileDetailView.as_view(), name="profile-detail-view"),
    # path('all-profiles/', views.profile_list_view,name='all-profiles-view'),
    
]