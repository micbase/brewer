
import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView,
    FormView,
)

from auth.views import LoginRequiredMixin
from brewer.forms import (
    CreateRecipeForm,
    IngredientForm,
    ProcedureForm,
    RecipeForm,
)

from brewer.models import (
    Ingredient,
    Procedure,
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
        return Procedure.objects.filter(recipe_id=recipe_id).order_by('id')

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
        context = {}
        context['note'] = self.get_note()
        return context


class IngredientNoteView(JSONResponseMixin, FormView):
    form_class = IngredientForm

    def form_valid(self, form):
        form.save()
        return self.render_to_response({'success': True})

    def get_ingredient(self):
        ingredient_id = self.kwargs['ingredient_id']
        return get_object_or_404(Ingredient, pk=ingredient_id)

    def get_note(self):
        ingredient = self.get_ingredient()
        return ingredient.note

    def get_form_kwargs(self):
        kwargs = super(IngredientNoteView, self).get_form_kwargs()
        kwargs['ingredient_id'] = self.kwargs['ingredient_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = {}
        context['note'] = self.get_note()
        return context


class ProcedureNoteView(JSONResponseMixin, FormView):
    form_class = ProcedureForm

    def form_valid(self, form):
        form.save()
        return self.render_to_response({'success': True})

    def get_procedure(self):
        procedure_id = self.kwargs['procedure_id']
        return get_object_or_404(Procedure, pk=procedure_id)

    def get_note(self):
        procedure = self.get_procedure()
        return procedure.note

    def get_form_kwargs(self):
        kwargs = super(ProcedureNoteView, self).get_form_kwargs()
        kwargs['procedure_id'] = self.kwargs['procedure_id']
        return kwargs

    def get_context_data(self, **kwargs):
        context = {}
        context['note'] = self.get_note()
        return context

class CreateRecipeView(FormView):
    template_name = 'brewer/create_recipe.html'
    form_class = CreateRecipeForm
    recipe_id = 0

    def form_valid(self, form):
        self.recipe_id = form.save()
        return super(CreateRecipeView, self).form_valid(form)

    def get_success_url(self):
       return '/recipe/' + str(self.recipe_id)

    def get_context_data(self, **kwargs):
        context = super(CreateRecipeView, self).get_context_data(**kwargs)
        #import pdb; pdb.trace();
        return context
