from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^routing/simple_route/$', views.simple_route),
    url(r'^routing/slug_route/[a-z0-9-_]{1,16}/$', views.slug_route),
    url(r'^routing/sum_route/-{0,1}\d/-{0,1}\d/$', views.sum_route),
    url(r'^routing/sum_get_method/', views.sum_get_method),
    url(r'^routing/sum_post_method/$', views.sum_post_method),
]