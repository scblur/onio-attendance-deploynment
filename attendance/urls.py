from django.conf.urls import url, include
from attendance import views
from datetime import datetime

app_name = 'attendance'

urlpatterns = [
    url(r'^mark/$',views.CreateSessionView.as_view(),name='create'),
    url(r'^list/$',views.DetailSessionView.as_view(),name='list'),
]


# S = str(datetime.now().time()).strip(':')
# A = [int(i) for i in S.replace('.', ':').split(':')]
# if (A[0] == 9 and A[1] in range(0,31)) | (A[0] in range(18,22) and A[1] in range(0,61)):
#     urlpatterns = [
#         url(r'^mark/$',views.CreateSessionView.as_view(),name='create'),
#     ] + urlpatterns
# else:
#     urlpatterns = [
#         url(r'^index/$',views.IndexPageView.as_view(),name='indexpage'),
#     ] + urlpa
