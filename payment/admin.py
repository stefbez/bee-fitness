from django.contrib import admin
from payment.models import PaidMember, UserInfo


class PaidMemberAdmin(admin.ModelAdmin):
    """ Premium User Admin """
    list_display = (
        'user',
        'start_date',
        'end_date',
        'subscription',
    )


admin.site.register(PaidMember, PaidMemberAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    """ User Info Admin """
    list_display = (
        'user',
        'first_name',
        'last_name',
        'first_line_address',
        'postcode',
    )


admin.site.register(UserInfo, UserInfoAdmin)
