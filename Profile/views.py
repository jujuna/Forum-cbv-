from django.views.generic import TemplateView,FormView
from  django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

class ProfileHome(TemplateView):
    template_name = "profile/home.html"
