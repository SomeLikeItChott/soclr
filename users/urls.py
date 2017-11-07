from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^([0-9]+)/$', views.profile, name='register'),

]


# ^login/$ [name='login']
# ^logout/$ [name='logout']
# ^password_change/$ [name='password_change']
# ^password_change/done/$ [name='password_change_done']
# ^password_reset/$ [name='password_reset']
# ^password_reset/done/$ [name='password_reset_done']
# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^reset/done/$ [name='password_reset_complete']