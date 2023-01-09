from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
# from django.http import request
# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView
from django.db.models import Q

from requestApp.forms import *
from requestApp.models import *
from userprofile.models import *


def get_default_req_code(user):
    return str(user)[:5].replace(".", "") + (timezone.now()).strftime("%y%m%d%H%M%S")


class CustomLoginView(LoginView):
    # template_name = 'requestApp/login.html'
    # fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('req-list')


class ReqList(LoginRequiredMixin, ListView):
    # model = Req
    # queryset = Req.objects.all()
    paginate_by = 8

    # template_name = 'requestApp/req_list.html'
    # context_object_name = 'req_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Перелік заявок РДС'
        return context

    def get_queryset(self):  # возвращает значение атрибута queryset

        signed = self.request.GET.get('signed')
        if signed is None:
            signed = True
        my_userprofile = UserProfile.objects.select_related().get(user=self.request.user)

        try:

            u = User.objects.select_related().get(id=self.request.user.id)
            user_role = u.userprofile.role

            if user_role == Role.DIRECTOR:
                return Req.objects.select_related().filter(
                    (Q(user=self.request.user) | Q(is_ready=True))
                    & (Q(is_agreed=False) | Q(is_agreed=signed)))
        except ObjectDoesNotExist:
            pass

        return Req.objects.select_related().filter(
            (Q(user=self.request.user) | Q(user__userprofile__supervisor=my_userprofile))
            & (Q(is_agreed=False) | Q(is_agreed=signed)))


# class ReqCreate(LoginRequiredMixin, CreateView):
#     model = Req
#     form_class = ReqCreateForm
#     template_name = 'requestApp/req_create.html'
#     context_object_name = 'req'
#     success_url = reverse_lazy('req-list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Нова ЗаявкаРДС'
#         return context
#
#     def get_default_req_code(self):
#         return str(self.request.user)[:5] + (timezone.now()).strftime("%y%m%d%H%M%S")
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.req_code = self.get_default_req_code()
#         return super(ReqCreate, self).form_valid(form)


class MessageCreate(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'requestApp/message_create.html'
    context_object_name = 'message'
    success_url = reverse_lazy('req-list')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        print("=========>", self.request)
        # form.instance.req = self.request.req.id
        return super(MessageCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Створення повідомлення'
        return context


def req_create_view(request):
    # TODO обмежити можливість редагувати вже підписані т.я. можна зайти по строці адресній
    form_req = ReqCreateForm(request.POST or None)
    context = {
        "form_req": form_req,
        'title': 'Нова ЗаявкаРДС',
    }
    if request.method == 'POST':
        if form_req.is_valid():
            form_req.instance.user = request.user
            form_req.instance.req_code = get_default_req_code(request.user)
            form_req.save()
            if form_req.instance.is_ready:
                return redirect('agreed-add', form_req.instance.id)
            return redirect('req-list')

    return render(request, "requestApp/req_create.html", context)


def req_update_view(request, id=None):
    # TODO обмежити можливість редагувати вже підписані т.я. можна зайти по строці адресній
    req = get_object_or_404(Req, pk=id)
    form_req = ReqUpdateForm(request.POST or None, instance=req)
    messages = req.message_set.all()  # = Message.objects.filter(req=req)

    context = {
        "form_req": form_req,
        "req": req,
        "messages": messages,
    }

    if request.method == 'POST':
        if form_req.is_valid():
            form_req.save()
            #TODO заборонити таке відкриття сторінки для редагування вже підписаних
            if form_req.instance.is_ready:
                return redirect('agreed-add', form_req.instance.id)

            return redirect('req-list')

    return render(request, "requestApp/req_update.html", context)


def req_detail_view(request, req_id=None):
    try:
        req = Req.objects.get(id=req_id)

        is_agreed = Agreed.objects.filter(user=request.user, req=req).exists()

        messages = req.message_set.all().order_by('-date')
        form_add_message = MessageCreateForm

        context = {
            "form_add_message": form_add_message,
            "req": req,
            "messages": messages,
            "is_agreed": is_agreed,
        }
    except:
        raise Http404("Заявки такої немає")

    return render(request, 'requestApp/req_detail.html', context)


def req_message_add_view(request, req_id):
    try:
        req = Req.objects.get(id=req_id)
    except:
        raise Http404("Заявки такої немає")

    if request.method == 'POST':
        message_text = request.POST['message_text']
        if len(message_text) > 0:
            req.message_set.create(
                user=request.user,
                req=req,
                message_text=request.POST['message_text'],
            )
            try:
                send_mail(
                    subject="Додано нове повідомлення",
                    message=message_text,
                    from_email="v.torishnyak@pharmasco.com",
                    recipient_list=("v.torishnyak@pharmasco.com",)
                )
            except:
                pass
    return HttpResponseRedirect(reverse('req-detail', args=(req.id,)))


def req_agreed_add_view(request, req_id):
    try:
        req = Req.objects.get(id=req_id)
    except:
        raise Http404("Заявки такої немає")

    req.agreed_set.create(
        user=request.user,
        req=req
    )
    req.message_set.create(
        user=request.user,
        req=req,
        message_text="(ПІДПИСАНО)",
    )

    return HttpResponseRedirect(reverse('req-detail', args=(req.id,)))


class ReqDelete(LoginRequiredMixin, DeleteView):
    model = Req
    fields = '__all__'
    success_url = reverse_lazy('req-list')
    context_object_name = 'req'

    def get_queryset(self):
        return Req.objects.filter(user=self.request.user)
