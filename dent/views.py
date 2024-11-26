from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy


class BaseView(ListView, FormView):
    form_class = BaseContactForm
    model = Descriptions
    template_name = 'dent/base.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.send_message(
            form.cleaned_data['name'],
            form.cleaned_data['email'],
            form.cleaned_data['message'],
        )
        self.response(
            form.cleaned_data['name'],
            form.cleaned_data['email']
        )
        messages.success(self.request, 'Thank you for your message!')
        return super().form_valid(form)

    def send_message(self, name, email, message):
        text_template = get_template('dent/base_message.html')
        html_template = get_template('dent/base_message.html')
        context = {'name': name, 'email': email, 'message': message}
        subject = "Message from user"
        from_email = email
        text_content = text_template.render(context)
        html_content = html_template.render(context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, ['ikdental306@gmail.com'])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    def response(self, name, email):
        text_template = get_template('dent/response.html')
        html_template = get_template('dent/response.html')
        subject = "Thank you for contacting us!"
        from_email = 'ikdental306@gmail.com'
        context = {'name': name, 'email': email}
        text_content = text_template.render(context)
        html_content = html_template.render(context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


class HomeView(BaseView, ListView, FormView):
    model = Descriptions
    form_class = BaseContactForm
    template_name = 'dent/index.html'
    extra_context = {'title': 'IKDENTAL'}
    success_url = reverse_lazy('home')


class AboutView(BaseView, ListView, FormView):
    model = Team
    form_class = BaseContactForm
    template_name = 'dent/about_us.html'
    extra_context = {'title': 'About Us'}
    success_url = reverse_lazy('home')

class PricesView(BaseView, ListView, FormView):
    model = Prices
    form_class = BaseContactForm
    template_name = 'dent/prices.html'
    extra_context = {'title': 'Price List'}
    success_url = reverse_lazy('home')

class ContactPageView(FormView, ListView):
    model = Descriptions
    form_class = ContactForm
    template_name = 'dent/contact.html'
    success_url = '/contact/'
    extra_context = {'title': 'Contact Page'}




    def form_valid(self, form):
        self.send_message(
            form.cleaned_data['name'],
            form.cleaned_data['surname'],
            form.cleaned_data['email'],
            form.cleaned_data['phone'],
            form.cleaned_data['message'],
        )
        self.response(
            form.cleaned_data['name'],
            form.cleaned_data['surname'],
            form.cleaned_data['email']
        )
        messages.success(self.request, 'Thank you for your message!')
        return super().form_valid(form)

    def send_message(self, name, surname, email, phone, message):
        text_template = get_template('dent/message.html')
        html_template = get_template('dent/message.html')
        context = {'name': name, 'surname': surname, 'email': email, 'phone': phone, 'message': message}
        subject = "Message from user"
        from_email = email
        text_content = text_template.render(context)
        html_content = html_template.render(context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, ['ikdental306@gmail.com'])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


    def response(self, name, surname, email):
        text_template = get_template('dent/response.html')
        html_template = get_template('dent/response.html')
        subject = "Thank you for contacting us!"
        from_email = 'ikdental306@gmail.com'
        context = {'name': name, 'surname': surname, 'email': email}


        text_content = text_template.render(context)
        html_content = html_template.render(context)


        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

