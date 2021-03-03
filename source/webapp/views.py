from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from webapp.models import News


class IndexView(ListView):
    model = News
    template_name = 'index1.html'
    context_object_name = 'news'
    paginate_by = 15
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last'] = News.objects.first()
        return context


class SearchView(ListView):
    model = News
    template_name = 'index1.html'
    context_object_name = 'news'
    paginate_by = 15
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        search_value = self.request.GET.get('search')

        if search_value:  # Есть ли серч вэлйу (в результате поиска)
            query = Q(title__icontains=search_value) | Q(text__icontains=search_value)
            context['news'] = News.objects.filter(query)
            context['last'] = News.objects.filter(query).first()
            context['search_value'] = search_value
        return context

