from django.db.models import Window, F
from django.db.models.functions import RowNumber
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from user.models import CustomUser


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        rating = CustomUser.objects.annotate(
            rank=Window(
                expression=RowNumber(), order_by=F('pixels_colored').desc()
            )
        ).order_by('-pixels_colored')
        return render(request, self.template_name, {'rating': rating[:5]})
