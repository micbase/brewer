
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    View,
)

from auth.views import LoginRequiredMixin
import brewer as brewer_constants
from brewer.forms import (
    CreateTopicForm,CreatePostForm,
)
from brewer.models import (
    Course,
    CourseSchedule,
    Membership,
    Post,
    Topic,
)


class CourseView(ListView):
    template_name = 'brewer/courses.html'
    paginate_by = 20

    def get_queryset(self):
        course_name = self.request.GET.get("course_name", "")
        return Course.objects.filter(
            name__icontains=course_name,
        )

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        context['course_name'] = self.request.GET.get("course_name", "")
        return context


class UserProfileView(LoginRequiredMixin, ListView):
    template_name = 'brewer/user_profile.html'
    paginate_by = 20

    def get_queryset(self):
        users=self.request.user
        return Course.objects.filter(
            students=users
        )
    def get_membership(self):
        users=self.request.user
        return Membership.objects.filter(
            member=users
        )


class JoinClassView(LoginRequiredMixin, View):

    def post(self, request, **kwargs):
        user = self.request.user
        course_id = request.POST.get('course_id', "")
        membership, created = Membership.objects.get_or_create(
            member=user,
            course_id=course_id,
        )
        membership.status = brewer_constants.ENROLL_COURSE
        membership.save()
        return HttpResponseRedirect('/topics/' + course_id)


class CreateTopicView(LoginRequiredMixin, CreateView):
    template_name = 'brewer/create_topic.html'
    model = Topic
    form_class = CreateTopicForm

    def get_success_url(self):
        return '/topics/' + self.kwargs['course_id']

    def get_form_kwargs(self):
        kwargs = super(CreateTopicView, self).get_form_kwargs()
        course_id = self.kwargs['course_id']
        kwargs['course'] = get_object_or_404(Course, pk=course_id)
        kwargs['author'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateTopicView, self).get_context_data(**kwargs)
        context['course_id'] = self.kwargs['course_id']
        return context


class TopicsView(ListView):
    template_name = 'brewer/topics.html'
    paginate_by = 20
    context_object_name = 'topics'

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Topic.objects.filter(
            course_id=course_id,
        )

    def get_course(self):
        course_id = self.kwargs['course_id']
        return get_object_or_404(Course, pk=course_id)

    def is_course_joined(self):
        course_id = self.kwargs['course_id']
        user = self.request.user
        if user.is_authenticated():
            count = Membership.objects.filter(
                member=user,
                course_id=course_id,
                status=brewer_constants.ENROLL_COURSE
            ).count()
            return count >= 1
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super(TopicsView, self).get_context_data(**kwargs)
        context['course'] = self.get_course()
        context['course_joined'] = self.is_course_joined()
        return context
