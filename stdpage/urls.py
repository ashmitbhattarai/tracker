from django.conf.urls import patterns, include, url

urlpatterns = patterns('stdpage.views',
	url(r'^all', 'stdpages'),
	url(r'^get/(?P<stdpage_id>\d+)', 'stdlist'), #?P<stdpage_id>\d gives id
	url(r'^create', 'create'),
	url(r'^add_comment/(?P<status1_id>\d+)', 'add_comment'),
	url(r'^asgmnt_update', 'asg1_reg'),
	url(r'^show','show_asgmnt'),
	url(r'^delete/(?P<asgmnt1_id>\d+)','not_show'),
	
)
