from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from django.contrib.auth.models import User
from qr_code.qrcode.utils import ContactDetail


@login_required
def members(request):
    """ A view to return the index page """
    if not request.user.is_authenticated:
        return redirect(reverse('home'))

        try:
            get_user = get_object_or_404(User, username=user)

            user_profile = get_object_or_404(UserProfile, user=get_user)

            context = {
                    'user_profile': user_profile,
                    'user': user,
                }

            return render(request, 'members/members.html', context)
        except Exception as e:
            return render(request, 'members/members.html', context)
    return render(request, 'members/members.html')

# def application_qr_code_demo(request):
#     # Use a ContactDetail instance to encapsulate the detail of the contact.
#     contact_detail = ContactDetail(
#         first_name='John',
#         last_name='Doe',
#         first_name_reading='jAAn',
#         last_name_reading='dOH',
#         tel='+41769998877',
#         email='j.doe@company.com',
#         url='http://www.company.com',
#         birthday=date(year=1985, month=10, day=2),
#         address='Cras des Fourches 987, 2800 Delémont, Jura, Switzerland',
#         memo='Development Manager',
#         org='Company Ltd',
#     )
#         # Build context for rendering QR codes.
#     context = dict(
#         contact_detail=contact_detail,
#     )

#     # Render the index page.
#     return render(request, 'members/members.html', context=context)