from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
# from django.http import request
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

import userprofile.models
from requestApp.forms import *
from requestApp.models import *
from userprofile.models import Role


class CustomLoginView(LoginView):
    template_name = 'requestApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('req-list')


class ReqList(LoginRequiredMixin, ListView):
    is_signed = False
    model = Req
    paginate_by = 8
    template_name = 'requestApp/req-list.html'
    context_object_name = 'reqs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Перелік заявок'
        return context

    def get_queryset(self):

        signed = self.request.GET.get('signed')
        if signed is None: signed = True

        try:
            u = User.objects.get(id=self.request.user.id)
            user_role = u.userprofile.role

            if user_role == Role.DIRECTOR:
                return Req.objects.filter(
                    (Q(user=self.request.user) | Q(is_ready=True))
                    & (Q(is_agreed=False) | Q(is_agreed=signed)))
            else:
                my_userprofile = UserProfile.objects.get(user=self.request.user)
                return Req.objects.filter(
                    (Q(user=self.request.user) | Q(user__userprofile__supervisor=my_userprofile))
                    & (Q(is_agreed=False) | Q(is_agreed=signed)))
        except ObjectDoesNotExist:
            pass
        return None



class ReqCreate(LoginRequiredMixin, CreateView):
    model = Req
    form_class = ReqUpdateForm

    success_url = reverse_lazy('req-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReqCreate, self).form_valid(form)


class ReqUpdate(LoginRequiredMixin, UpdateView):
    model = Req

    form_class = ReqUpdateForm
    # template_name = 'finances/transaction_update.html'
    success_url = reverse_lazy('req-list')

    # def get_queryset(self):
    #     if self.request.user.role == Role.DIRECTOR:
    #         return Req.objects.filter(Q(user=self.request.user) | Q(is_ready=True))
    #     else:
    #         return Req.objects.filter(user=self.request.user)


class ReqDelete(LoginRequiredMixin, DeleteView):
    model = Req
    fields = '__all__'
    success_url = reverse_lazy('req-list')

    def get_queryset(self):
        return Req.objects.filter(user=self.request.user)


class ReqSign(LoginRequiredMixin, CreateView):
    model = Agreed
    form_class = ReqAgreeForm
    success_url = reverse_lazy('req-list')
    template_name = 'requestApp/req-agree.html'
