from django.conf.urls import url
from multipliers.views import or_view

urlpatterns = [
    url(r'^$', or_view, name='or')
]