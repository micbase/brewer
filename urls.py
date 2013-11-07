from django.conf.urls import patterns, url
from django.conf import settings

import brewer.views
import auth.views

urlpatterns = patterns('',
    #url(r'^$', brewer.views.CourseView.as_view(), name='course_list'),
    #url(r'^user_profile$', brewer.views.UserProfileView.as_view(), name='user_profile'),

    url(r'^recipe/(?P<recipe_id>\d+)$', brewer.views.RecipeView.as_view(), name='recipe'),
    url(r'^recipe/(?P<ingredient_id>\d+)$', brewer.views.IngredientView.as_view(), name='ingredient'),
    url(r'^recipe/(?P<procedure_id>\d+)$', brewer.views.ProcedureView.as_view(), name='procedure'),
    #url(r'^create_topic/(?P<course_id>\d+)$', brewer.views.CreateTopicView.as_view(), name='create_topic'),

    url(r'^login$', auth.views.LoginView.as_view(), name='login'),
    url(r'^logout$', auth.views.LogoutView.as_view(), name='logout'),
    url(r'^register$', auth.views.RegisterView.as_view(), name='register'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
