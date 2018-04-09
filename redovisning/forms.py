from django import forms
from redovisning.models import Organization,Boardmember,Contact,Meeeting,Member,User,Attestation


class AddMemberForm(forms.ModelForm):
    first_name = forms.CharField(label='Förnamn/Ime')
    last_name = forms.CharField(label='Efternamn/Prezime')
    #date_of_birth = forms.CharField(label='Födelsedag/Datum rodjenja (yyyy-mm-dd)')
    year_of_birth = forms.CharField(label='Födelseår/Godiste (npr 2001)')
    phone = forms.CharField(label='Telefon')
    address = forms.CharField(label='Adress/Adresa')
    gender = forms.ChoiceField(label='Kön/Pol',choices=(('M','Man'),
                                                        ('K','Kvinna'),
                                                        ))
    city = forms.CharField(label='Stad/Grad')
    zipcode = forms.CharField(label='Postnummer/Postanski broj')
    date_added = forms.CharField(label='Datum')
    class Meta:
        model = Member
        exclude = ['org_id']

    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False


class AddOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class AddBoardmemberForm(forms.ModelForm):
    member_name = forms.CharField(label='Namn/Ime i prezime')
    post = forms.CharField(label='Vald till/Izabran za')
    date_of_birth = forms.CharField(label='Födelsedag/Dan rodjenja')
    phone = forms.CharField(label='Telefon')
    gender = forms.CharField(label='Kön/Pol')
    class Meta:
        model = Boardmember
        exclude = ['org_id']

class AddContactForm(forms.ModelForm):
    contact_name = forms.CharField(label='Namn/Ime')
    contact_type = forms.CharField(label='Befattning/Uloga u udruzenju')
    address = forms.CharField(label='Adress/Adresa')
    phone = forms.CharField(label='Telefon')
    city = forms.CharField(label='Stad/Grad')
    zipcode = forms.CharField(label='Postnummer/Postanski broj')
    class Meta:
        model = Contact
        exclude = ['org_id']

class AddMeetingForm(forms.ModelForm):
    no_of_meetings = forms.CharField(label='Antal styrelsemöten under verksamhetsåret/Broj sastanaka upravnog odbora u toku godine')
    annual_meeting_date = forms.CharField(label='Datum då årsmötet hölls/Datum odrzavanja godisnje skupstine')
    current_statuses_attached = forms.BooleanField(label='Vi bifogar föreningens/sektionens gällande stadgar/Poslacemo vazeci statut za udruzenje/sekciju')
    statutes_not_attached = forms.BooleanField(label='Stadgarna bifogas ej, då dessa ej ändrats av årsmötet (vid ändring måste stadgarna bifogas)')
    activity = forms.CharField(label='Bedriven verksamhet/Djelatnost u toku godine', widget=forms.Textarea())
    collaboration_with_others = forms.BooleanField(label='Föreningen/sektionen har samarbetat med andra föreningar/sektioner i sin verksamhet/Udruzenje/sekcija je saradjivalo sa drugim udruzenjima/sekcijama')
    bhuf_activity = forms.BooleanField(label='Föreningens/sektionens medlemmar ha deltagit i aktiviteter anordnade av BHUF/Udruzenje/sekcija je ucestvovalo u BHUF aktivnostima')
    year = forms.CharField(label='År/Godina')
    class Meta:
        model = Meeeting
        exclude = ['org_id']

    def __init__(self, *args, **kwargs):
        super(AddMeetingForm, self).__init__(*args, **kwargs)
        self.fields['statutes_not_attached'].required = False
        self.fields['current_statuses_attached'].required = False
        self.fields['collaboration_with_others'].required = False
        self.fields['bhuf_activity'].required = False

class AddAttestationForm(forms.ModelForm):
    printed_name = forms.CharField(label='Attesteras av/Potpisnik')
    date_signed = forms.DateField(label='Datum för attest/Datum potpisivanja')
    class Meta:
        model = Attestation
        exclude = ['org_id']

class EditMemberForm(forms.ModelForm):
    first_name = forms.CharField(label='Förnamn/Ime')
    last_name = forms.CharField(label='Efternamn/Prezime')
    #date_of_birth = forms.CharField(label='Födelsedag/Datum rodjenja (yyyy-mm-dd)')
    year_of_birth = forms.CharField(label='Födelseår/Godiste (npr 2001)')
    phone = forms.CharField(label='Telefon')
    address = forms.CharField(label='Adress/Adresa')
    gender = forms.ChoiceField(label='Kön/Pol',choices=(('M','Man'),('K','Kvinna'),))
    city = forms.CharField(label='Stad/Grad')
    zipcode = forms.CharField(label='Postnummer/Postanski broj')
    date_added = forms.CharField(label='Datum')
    class Meta:
        model = Member
        exclude = ['org_id']

    def __init__(self, *args, **kwargs):
        super(EditMemberForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False

class EditMeetingForm(forms.ModelForm):
    no_of_meetings = forms.CharField(label='Antal styrelsemöten under verksamhetsåret/Broj sastanaka upravnog odbora u toku godine')
    annual_meeting_date = forms.CharField(label='Datum då årsmötet hölls/Datum odrzavanja godisnje skupstine')
    current_statuses_attached = forms.BooleanField(label='Vi bifogar föreningens/sektionens gällande stadgar/Poslacemo vazeci statut za udruzenje/sekciju')
    statutes_not_attached = forms.BooleanField(label='Stadgarna bifogas ej, då dessa ej ändrats av årsmötet (vid ändring måste stadgarna bifogas)')
    activity = forms.CharField(label='Bedriven verksamhet/Djelatnost u toku godine', widget=forms.Textarea())
    collaboration_with_others = forms.BooleanField(label='Föreningen/sektionen har samarbetat med andra föreningar/sektioner i sin verksamhet/Udruzenje/sekcija je saradjivalo sa drugim udruzenjima/sekcijama')
    bhuf_activity = forms.BooleanField(label='Föreningens/sektionens medlemmar ha deltagit i aktiviteter anordnade av BHUF/Udruzenje/sekcija je ucestvovalo u BHUF aktivnostima')
    year = forms.CharField(label='År/Godina')
    class Meta:
        model = Meeeting
        exclude = ['org_id']

    def __init__(self, *args, **kwargs):
        super(EditMeetingForm, self).__init__(*args, **kwargs)
        self.fields['statutes_not_attached'].required = False
        self.fields['current_statuses_attached'].required = False
        self.fields['collaboration_with_others'].required = False
        self.fields['bhuf_activity'].required = False

class EditBoardmemberForm(forms.ModelForm):
    member_name = forms.CharField(label='Namn/Ime i prezime')
    post = forms.CharField(label='Vald till/Izabran za')
    date_of_birth = forms.CharField(label='Födelsedag/Dan rodjenja')
    phone = forms.CharField(label='Telefon')
    gender = forms.CharField(label='Kön/Pol')
    class Meta:
        model = Boardmember
        exclude = ['org_id']

class EditContactForm(forms.ModelForm):
    contact_name = forms.CharField(label='Namn/Ime')
    contact_type = forms.CharField(label='Befattning/Uloga u udruzenju')
    address = forms.CharField(label='Adress/Adresa')
    phone = forms.CharField(label='Telefon')
    city = forms.CharField(label='Stad/Grad')
    zipcode = forms.CharField(label='Postnummer/Postanski broj')
    class Meta:
        model = Contact
        exclude = ['org_id']

class EditOrganizationForm(forms.ModelForm):
    org_name = forms.CharField(label='Förening/Udruzenje')
    association = forms.CharField(label='Sektion/sekcija')
    corporate = forms.CharField(label='Organisationsnummer/Registarski broj')
    national_organization = forms.CharField(label='Riksorganisation/Krovna organizacija')
    no_of_members = forms.CharField(label='Antal medlemmar/Broj clanova')
    address = forms.CharField(label='Adress/Adresa', widget=forms.Textarea())
    phone = forms.CharField(label='Telefon')
    account_no = forms.CharField(label='Konto/giro- nr:')
    clr_no = forms.CharField(label='Clr-nr')
    agree_send_info = forms.BooleanField(label='Styrelsen önskar att all post från BHUF skickas till någon av kontaktpersonerna som skickar vidare')
    website = forms.CharField(label='Hemsida/Internet stranica')
    social_link = forms.CharField(label='Sociala medier/Socijalni mediji')

    class Meta:
        model = Organization
        exclude = ['org_id']
