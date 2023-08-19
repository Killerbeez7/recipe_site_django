from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'common/about.html'


class ContactsView(TemplateView):
    template_name = 'common/contacts.html'
