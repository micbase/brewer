
import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    FormView,
)

from auth.views import LoginRequiredMixin
import brewer as brewer_constants
from brewer.forms import (
    IngredientForm,
    ProcedureForm,
    RecipeForm,
)

from brewer.models import (
    Ingredient,
    Procedure,
    Source,
    Recipe,
)


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)


class RecipeView(TemplateView):
    template_name = 'brewer/recipe.html'

    def get_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, pk=recipe_id)

    def get_ingredient(self):
        recipe_id = self.kwargs['recipe_id']
        return Ingredient.objects.filter(recipe_id=recipe_id)

    def get_procedure(self):
        recipe_id = self.kwargs['recipe_id']
        return Procedure.objects.filter(recipe_id=recipe_id)

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        context['recipe'] = self.get_recipe()
        context['ingredient'] = self.get_ingredient()
        context['procedure'] = self.get_procedure()
        return context

class RecipeNoteView(JSONResponseMixin, FormView):
    form_class = RecipeForm

    def form_valid(self, form):
        form.save()
        return self.render_to_response({'success': True})

    def get_recipe(self):
        recipe_id = self.kwargs['recipe_id']
        return get_object_or_404(Recipe, pk=recipe_id)

    def get_note(self):
        recipe = self.get_recipe()
        return recipe.note

    def get_form_kwargs(self):
        kwargs = super(RecipeNoteView, self).get_form_kwargs()
        kwargs['recipe_id'] = self.kwargs['recipe_id']
        return kwargs

    def get_context_data(self, **kwargs):
        #context = super(RecipeNoteView, self).get_context_data(**kwargs)
        context = {}
        context['note'] = self.get_note()
        return context

class IngredientNoteView(FormView):
    template_name = 'brewer/recipe.html'
    form_class = IngredientForm

    def get_ingredient(self):
        ingredient_id = self.kwargs['ingredient_id']
        return get_object_or_404(Ingredient, pk=ingredient_id)

    def get_note(self):
        ingredient = self.get_ingredient()
        return ingredient.note

    def get_success_url(self):
        return '/recipe/' + self.kwargs['recipe_id']

    def get_form_kwargs(self):
        kwargs = super(IngredientView, self).get_form_kwargs()
        kwargs['ingredient_id'] = self.kwargs['ingredient_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(IngredientView, self).get_context_data(**kwargs)
        context['ingredient'] = Ingredient.objects.get(pk=self.kwargs['ingredient_id'])
        context['note'] = self.get_note()
        return context

class ProcedureNoteView(FormView):
    template_name = 'brewer/recipe.html'
    form_class = ProcedureForm

    def get_procedure(self):
        procedure_id = self.kwargs['procedure_id']
        return get_object_or_404(Procedure, pk=procedure_id)

    def get_note(self):
        procedure = self.get_procedure()
        return procedure.note

    def get_success_url(self):
        return '/recipe/' + self.kwargs['recipe_id']

    def get_form_kwargs(self):
        kwargs = super(IngredientView, self).get_form_kwargs()
        kwargs['procedure_id'] = self.kwargs['procedure_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ProcedureView, self).get_context_data(**kwargs)
        context['procedure'] = Procedure.objects.get(pk=self.kwargs['procedure_id'])
        context['note'] = self.get_note()
        return context


