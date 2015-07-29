from django.conf.urls import patterns, include, url

urlpatterns = patterns('usermod.views',
	url(r'^register/$', 'user_register'),
	url(r'^reg_success/$', 'reg_success'),
	url(r'^user_update/$', 'user_update'),
	"""url(r'^asgmnt_update/$', 'asg_reg'),"""
	)
