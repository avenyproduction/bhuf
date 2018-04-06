from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView
from redovisning.models import Member,Organization,Boardmember,Contact,Meeeting,Attestation
from redovisning.forms import AddOrganizationForm,AddBoardmemberForm,AddContactForm,AddMeetingForm,AddMemberForm,AddAttestationForm
from redovisning.forms import EditMemberForm,EditMeetingForm,EditBoardmemberForm,EditContactForm,EditOrganizationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from datetime import date
from django.db.models import DateTimeField, F




# Create your views here.
class IndexView(TemplateView):
    template_name = 'redovisning/index.html'

    # def get_how_old(self,getttt):
    #     today = date.today()
    #     return Member.objects.filter(org_id=self.request.user.org_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_list'] = Member.objects.filter(org_id=self.request.user.org_id)
        context['man_members'] = Member.objects.all().filter(org_id=self.request.user.org_id).filter(gender='M')
        #context['today'] = self.get_how_old('444')
        context['test'] = Member.objects.filter(org_id=self.request.user.org_id).filter(gender='M').filter(date_of_birth__gt=F(5))
        return context


class MemberListView(ListView):
    model = Member
    context_object_name = 'member_list'
    template_name = 'redovisning/list_members.html'

    def get_queryset(self):
        return Member.objects.filter(org_id=self.request.user.org_id)

class BoardmemberListView(ListView):
    model = Boardmember
    context_object_name = 'boardmember_list'
    template_name = 'redovisning/list_by_boardmember.html'

    def get_queryset(self):
        return Boardmember.objects.filter(org_id=self.request.user.org_id)

class MeetingListView(ListView):
    model = Meeeting
    context_object_name = 'meeting_list'
    template_name = 'redovisning/list_by_meeting.html'

    def get_queryset(self):
        return Meeeting.objects.filter(org_id=self.request.user.org_id)

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contact_list'
    template_name = 'redovisning/list_contacts.html'

    def get_queryset(self):
        return Contact.objects.filter(org_id=self.request.user.org_id)

class AttestationListView(ListView):
    model = Attestation
    context_object_name = 'attestation_list'
    template_name = 'redovisning/list_attestations.html'

    def get_queryset(self):
        return Attestation.objects.filter(org_id=self.request.user.org_id)

class AddMemberView(CreateView):
    model = Member
    form_class = AddMemberForm
    success_url = reverse_lazy('redovisning:memberlist')
    template_name = 'redovisning/add_member.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        form.instance.org_id = self.request.user.org_id
        return super().form_valid(form)

class ThankYouView(TemplateView):
    template_name = 'redovisning/add_member_thankyou.html'


def AddOrganizationView(request):
    if request.method == "POST":
        form = AddOrganizationForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('redovisning:thankyou')
    else:
        form = AddOrganizationForm()
    return render(request, 'redovisning/add_organization.html', {'form': form})


class AddBoardmemberView(CreateView):
    model = Boardmember
    form_class = AddBoardmemberForm
    success_url = reverse_lazy('redovisning:boardmemberlist')
    template_name = 'redovisning/add_boardmember.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        form.instance.org_id = self.request.user.org_id
        return super().form_valid(form)


class AddContactView(CreateView):
    model = Contact
    form_class = AddContactForm
    success_url = reverse_lazy('redovisning:contactlist')
    template_name = 'redovisning/add_contact.html'

    def form_valid(self, form):
        form.instance.org_id = self.request.user.org_id
        return super().form_valid(form)


class AddMeetingView(CreateView):
    model = Meeeting
    form_class = AddMeetingForm
    success_url = reverse_lazy('redovisning:meetinglist')
    template_name = 'redovisning/add_meeting.html'

    def form_valid(self, form):
        form.instance.org_id = self.request.user.org_id
        return super().form_valid(form)

class AddAttestationView(CreateView):
    model = Attestation
    form_class = AddAttestationForm
    success_url = reverse_lazy('redovisning:attestationlist')
    template_name = 'redovisning/add_attestation.html'

    def form_valid(self, form):
        form.instance.org_id = self.request.user.org_id
        return super().form_valid(form)

class EditOrganizationView(UpdateView):
    model = Organization
    form_class = EditOrganizationForm
    success_url = '/redovisning/'
    template_name = 'redovisning/edit_organization.html'


class EditMemberView(UpdateView):
    model = Member
    form_class = EditMemberForm
    success_url = "/redovisning/members/"
    template_name = 'redovisning/edit_member.html'


class EditMeetingView(UpdateView):
    model = Meeeting
    form_class = EditMeetingForm
    success_url = '/redovisning/meetings/'
    template_name = 'redovisning/edit_meeting.html'

class EditBoardmemberView(UpdateView):
    model = Boardmember
    form_class = EditBoardmemberForm
    success_url = '/redovisning/boardmembers/'
    template_name = 'redovisning/edit_boardmember.html'

class EditContactView(UpdateView):
    model = Contact
    form_class = EditContactForm
    success_url = '/redovisning/contacts/'
    template_name = 'redovisning/edit_contact.html'

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('redovisning:thankyou')
    else:
        # Return an 'invalid login' error message.
        return redirect('redovisning:thankyou')

def logout(request):
    logout(request)
    return redirect('redovisning:index')
