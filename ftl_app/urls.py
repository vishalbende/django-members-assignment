

from django.conf.urls import url
from ftl_app.views.user_data import FTLTestView


urlpatterns = [
    
    # url to get list of members along with its activity
    url(r'^members/$', FTLTestView.as_view({'get': 'list'})),
]
