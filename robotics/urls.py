from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'robotics'
# handler404 = 'show_404'

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="robotics/base.html"), name='home'),
    url(r'^about-us/$', TemplateView.as_view(template_name="robotics/about-us.html"), name='about-us'),
    url(r'^contact-us/$', TemplateView.as_view(template_name="robotics/contact-us.html"), name='contact-us'),
        
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)