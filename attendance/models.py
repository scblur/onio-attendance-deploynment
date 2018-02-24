from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.http import HttpResponse

# from django.conf import settings
# User = settings.AUTH_USER_MODEL


S = str(datetime.now().time()).strip(':')
A = [int(i) for i in S.replace('.', ':').split(':')]
if A[0] == 10 and A[1] in range(0,31):
    CHOICES=[('Morning','Morning')]
elif A[0] in range(18,22) and A[1] in range(0,61):
    CHOICES=[('Evening','Evening')]
else:
    CHOICES= [('','Please Come Back at the Specified Time. For more details, visit Home Page.')]

# CHOICES=[('Morning','Morning'),('Evening','Evening')]
class Session(models.Model):
    user = models.ForeignKey(User)
    session = models.CharField(max_length=25,choices=CHOICES, default="No Attendence")
    # session = models.CharField(max_length=25,choices=CHOICES, empty_label=None)
    t_date = models.DateTimeField(default=timezone.now,blank=True)
    only_date = models.DateField(default=timezone.now().today,blank=True)
    # ip_address = models.IPAddressField()

    def __str__(self):
        return "{} {} {}".format(self.user_id,self.session,str(self.t_date))

    def get_absolute_url(self):
        return reverse("attendance:create")

    def save(self, *args, **kwargs):

        # if self.session!= 'Morning' and self.session != 'Evening':
        #     return reverse("attendance:create")

        if self.session != '':
            conflicting_instance = Session.objects.filter(session=self.session, only_date=self.only_date, user=self.user_id)
            if self.id:
                # This instance has already been saved. So we need to filter out
                # this instance from our results.
                conflicting_instance = conflicting_instance.exclude(pk=self.id)

            if conflicting_instance.exists():
                return HttpResponse('Attendance already Marked!!!.')

        super(Session, self).save(*args, **kwargs)
