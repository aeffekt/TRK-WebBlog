from .models import Item
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    context_object_name = "item"


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['items'] = context['items'].filter(title__contains=search_input)
        context['search_input'] = search_input
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item    
    fields = {'title', 'description', 'done_status'}
    success_url = reverse_lazy('todo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = {'title', 'description', 'done_status'}
    success_url = reverse_lazy('todo')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = "item"
    success_url = reverse_lazy('todo')