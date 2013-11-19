from django.conf.urls import patterns, url
from django.conf import settings

import brewer.views
import auth.views

urlpatterns = patterns('',
    url(r'^$', brewer.views.RecipeListView.as_view(), name='recipes'),
    #url(r'^user_profile$', brewer.views.UserProfileView.as_view(), name='user_profile'),

    url(r'^recipe/(?P<recipe_id>\d+)$', brewer.views.RecipeView.as_view(), name='recipe'),
    url(r'^create_recipe$', brewer.views.CreateRecipeView.as_view(), name='create_recipe'),
    url(r'^recipe_note/(?P<recipe_id>\d+)$', brewer.views.RecipeNoteView.as_view(), name='recipe_note'),
    url(r'^ingredient_note/(?P<ingredient_id>\d+)$', brewer.views.IngredientNoteView.as_view(), name='ingredient_note'),
    url(r'^procedure_note/(?P<procedure_id>\d+)$', brewer.views.ProcedureNoteView.as_view(), name='procedure_note'),

    url(r'^login$', auth.views.LoginView.as_view(), name='login'),
    url(r'^logout$', auth.views.LogoutView.as_view(), name='logout'),
    url(r'^register$', auth.views.RegisterView.as_view(), name='register'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
