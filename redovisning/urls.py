from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'redovisning'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('organizations/add/', login_required(views.AddOrganizationView), name='addorganization'),
    path('organizations/<int:pk>/', login_required(views.EditOrganizationView.as_view()), name='editorganization'),
    path('members/', login_required(views.MemberListView.as_view()), name='memberlist'),
    path('members/add/', login_required(views.AddMemberView.as_view()), name='addmember'),
    path('members/<int:pk>/', login_required(views.EditMemberView.as_view()), name='editmember'),
    path('members/thankyou/', views.ThankYouView.as_view(), name='thankyou'),
    path('boardmembers/add/', login_required(views.AddBoardmemberView.as_view()), name='addboardmember'),
    path('boardmembers/', login_required(views.BoardmemberListView.as_view()), name='boardmemberlist'),
    path('boardmembers/<int:pk>/', login_required(views.EditBoardmemberView.as_view()), name='editboardmember'),
    path('contacts/add/', login_required(views.AddContactView.as_view()), name='addcontact'),
    path('contacts/', login_required(views.ContactListView.as_view()), name='contactlist'),
    path('contacts/<int:pk>/', login_required(views.EditContactView.as_view()), name='editcontact'),
    path('meetings/add/', login_required(views.AddMeetingView.as_view()), name='addmeeting'),
    path('meetings/', login_required(views.MeetingListView.as_view()), name='meetinglist'),
    path('meetings/<int:pk>/', login_required(views.EditMeetingView.as_view()), name='editmeeting'),
    path('attestations/add/', login_required(views.AddAttestationView.as_view()), name='addattestation'),
    path('attestations/', login_required(views.AttestationListView.as_view()), name='attestationlist'),
    path('login/', auth_views.login, {'template_name': 'redovisning/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'redovisning/login.html'}, name='logout'),
]
