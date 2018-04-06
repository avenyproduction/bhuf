from django.contrib import admin
from redovisning.models import Member,Organization,Boardmember,Contact,Meeeting,User,Attestation
from django.contrib.auth.admin import UserAdmin,Group


# Register your models here.
admin.site.register(Member)
admin.site.register(Organization)
admin.site.register(Boardmember)
admin.site.register(Contact)
admin.site.register(Meeeting)
admin.site.register(Attestation)

class UserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'org_id',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name',
                        'last_name', 'org_id', 'password1', 'password2')}
        ),
    )

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
