from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Canvas


class CanvasDetailView(LoginRequiredMixin, DetailView):
    model = Canvas
    template_name = 'canvas_detail.html'
    context_object_name = 'canvas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['websocket_url'] = f"/ws/canvas/{self.object.id}/"
        return context


class CanvasCreateView(LoginRequiredMixin, CreateView):
    model = Canvas
    fields = []
    template_name = 'canvas_create.html'
    success_url = reverse_lazy('canvas_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
