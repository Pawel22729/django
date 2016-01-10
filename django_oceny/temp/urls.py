from django.contrib import admin
from django.conf.urls import url, include
from pawel import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^pawel/', views.IndexView.as_view(), name='index'),
]
