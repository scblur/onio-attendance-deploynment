from django.shortcuts import render
from django.core.urlresolvers import reverse
from . import models
from attendance.models import Session
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.utils import timezone
from django.views.generic import TemplateView


# Create your views here.

class CreateSessionView(LoginRequiredMixin,CreateView):
    fields = ('session',)
    # fields = ('',)
    model = Session
    template_name = "attendance/attendance.html"
    # unique_together = ('session', 'only_date')
    readonly_fields = ("session",)


    def form_valid(self,form):
        zz = form.save(commit=False)
        zz.user = self.request.user
        # zz.t_date = timezone.localtime()
        return super(CreateSessionView, self).form_valid(form)

    def get_success_url(self):
        return reverse('attendance:list')

class DetailSessionView(LoginRequiredMixin,ListView):

    model = Session
    template_name = 'attendance/view_attendance.html'

    def get_queryset(self):
        return Session.objects.filter(user_id=self.request.user).order_by('-t_date')
#
# class IndexPageView(TemplateView):
#     template_name = 'index.html'
