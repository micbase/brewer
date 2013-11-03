from django.conf.urls import patterns, url
from django.conf import settings

import brewer.views
import auth.views

urlpatterns = patterns('',
    url(r'^$', brewer.views.CourseView.as_view(), name='course_list'),
    url(r'^user_profile$', brewer.views.UserProfileView.as_view(), name='user_profile'),

    url(r'^topics/(?P<course_id>\d+)$', brewer.views.TopicsView.as_view(), name='topics'),
    url(r'^create_topic/(?P<course_id>\d+)$', brewer.views.CreateTopicView.as_view(), name='create_topic'),

    url(r'^posts/(?P<topic_id>\d+)$', brewer.views.CreatePostView.as_view(), name='group-info'),
    url(r'^post_content/(?P<topic_id>\d+)$', brewer.views.CreatePostView.as_view(), name='group-info'),
    url(r'^join_course$', brewer.views.JoinClassView.as_view(), name='join_course'),
    url(r'^login$', auth.views.LoginView.as_view(), name='login'),
    url(r'^logout$', auth.views.LogoutView.as_view(), name='logout'),
    url(r'^register$', auth.views.RegisterView.as_view(), name='register'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
