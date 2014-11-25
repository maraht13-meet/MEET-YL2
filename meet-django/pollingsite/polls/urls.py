from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	# ex. //polls/meet
	url(r'^meet/$',views.index,name="meet"),
)
