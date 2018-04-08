from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Organization(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=200)
    association = models.CharField(max_length=200)
    corporate = models.CharField(max_length=200)
    national_organization = models.CharField(max_length=200)
    no_of_members = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=64)
    account_no = models.CharField(max_length=64)
    clr_no = models.CharField(max_length=32)
    agree_send_info = models.BooleanField()
    website = models.CharField(max_length=200)
    social_link = models.CharField(max_length=200)

    def __str__(self):
        return self.org_name

class User(AbstractUser):
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)

class Boardmember(models.Model):
    board_member_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)
    member_name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=64)
    gender = models.CharField(max_length=16)

    def __str__(self):
        return self.member_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)
    contact_name = models.CharField(max_length=200)
    contact_type = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=64)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=16)

    def __str__(self):
        return self.contact_name

class Meeeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)
    no_of_meetings = models.IntegerField()
    annual_meeting_date = models.DateField()
    #Vi bifogar föreningens/sektionens gällande stadgar
    current_statuses_attached = models.BooleanField()
    #Stadgarna bifogas ej, då dessa ej ändrats av årsmötet
    #(vid ändring måste stadgar bifogas)
    statutes_not_attached = models.BooleanField()
    #bedriven verksamhet
    activity = models.TextField()
    #Har föreningen/sektionen samarbetar med andra förening/sektioner i sin verksamhet
    collaboration_with_others = models.BooleanField()
    #Har föreningen/sektionens medlemmar deltagit i aktiviteter anordnade av bhuf
    bhuf_activity = models.BooleanField()

    year = models.CharField(max_length=4)

    def __str__(self):
       return str(self.annual_meeting_date)


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #date_of_birth = models.DateField()
    year_of_birth = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=64)
    address = models.TextField()
    gender = models.CharField(max_length=16)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=16)
    date_added = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Attestation(models.Model):
    attest_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)
    printed_name = models.CharField(max_length=200)
    date_signed = models.DateField()

    def __str__(self):
        return self.printed_name
