from django.contrib import admin
from django.conf.urls import url, include
from pawel import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^pawel/', views.IndexView.as_view(), name='index'),
	url(r'^wpisy/', views.PokazWpisy.as_view(), name='wpisy'),
	url(r'^forma/', views.forma, name='forma'),
	url(r'^$', views.PokazWpisy.as_view(), name='wpisy'),
    url(r'^test/', views.test, name='test'),
]
