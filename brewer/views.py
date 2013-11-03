
import datetime

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    View,
)

from auth.views import LoginRequiredMixin
import dashboard as dashboard_constants
from dashboard.forms import (
    CreateTopicForm,CreatePostForm,
)
from dashboard.models import (
    Course,
    CourseSchedule,
    Membership,
    Post,
    Topic,
)


class CourseView(ListView):
    template_name = 'dashboard/courses.html'
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
    template_name = 'dashboard/user_profile.html'
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
        membership.status = dashboard_constants.ENROLL_COURSE
        membership.save()
        return HttpResponseRedirect('/topics/' + course_id)


class CreateTopicView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/create_topic.html'
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

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/posts.html'
    model = Post
    form_class = CreatePostForm

    def get_success_url(self):
        return '/posts/' + self.kwargs['topic_id']

    def get_form_kwargs(self):
        kwargs = super(CreatePostView, self).get_form_kwargs()
        kwargs['topic_id'] = self.kwargs['topic_id']
        kwargs['author'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        context['topic_id'] = self.kwargs['topic_id']
        context['topic'] = Topic.objects.get(pk=self.kwargs['topic_id'])
        context['reply'] = Post.objects.filter(topic_id=self.kwargs['topic_id'])
        return context

class TopicsView(ListView):
    template_name = 'dashboard/topics.html'
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
                status=dashboard_constants.ENROLL_COURSE
            ).count()
            return count >= 1
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super(TopicsView, self).get_context_data(**kwargs)
        context['course'] = self.get_course()
        context['course_joined'] = self.is_course_joined()
        return context


class PostsView(ListView):
    template_name = 'dashboard/posts.html'
    paginate_by = 20
    context_object_name = 'reply'

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        return Post.objects.filter(
            topic_id=topic_id,
        )

    def get_topic(self):
        topic_id = self.kwargs['topic_id']
        return Topic.objects.get(pk=topic_id)

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['topic'] = self.get_topic()
        return context


class NotificationView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        token = request.POST.get("token", "")
        if token == "0lI3#5atxifYmbjuVm#0":

            weekday = datetime.datetime.today().weekday() + 1
            current = datetime.datetime.now()
            #weekday = 2
            #current = datetime.datetime(2012, 11, 22, 12, 20, 00)
            time_window_left = current + datetime.timedelta(minutes=-2)
            time_window_right = current + datetime.timedelta(minutes=2)

            course_list = CourseSchedule.objects.filter(
                end_time__gte=time_window_left,
                end_time__lte=time_window_right,
                weekday=weekday,
            )

            admin = User.objects.get(username='admin')

            for course in course_list:
                memberships = Membership.objects.filter(
                    course=course.course,
                    status=dashboard_constants.ENROLL_COURSE,
                )
                recipient_list = [membership.member.email for membership in memberships]

                new_topic = Topic(
                    title="How is today's class?",
                    content="Have some discussions about today's class!",
                    author=admin,
                    course=course.course,
                )
                new_topic.save()

                email = EmailMessage(
                    "How is today's class?",
                    'Discuss at http://192.168.42.2/posts/' + str(new_topic.id),
                    'Study Together <noreply@micbase.com>',
                    recipient_list,
                    bcc=['394purple@googlegroups.com', ],
                )
                email.send()

            return HttpResponse("OK")
        else:
            return HttpResponse("ERROR")
