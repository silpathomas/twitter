from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^tweet/(?P<pk>[0-9]+)$',
        views.get_delete_update_tweets,
        name='get_delete_update_tweets'
    ),
    url(
        r'^tweet/$',
        views.get_post_tweets,
        name='get_post_tweets'
    )
]