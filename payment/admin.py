from django.contrib import admin
from payment.models import PaidMember


class PaidMemberAdmin(admin.ModelAdmin):
    """ Premium User Admin """
    list_display = (
        'user',
        'start_date',
        'end_date',
        'subscription',
    )


admin.site.register(PaidMember, PaidMemberAdmin)
