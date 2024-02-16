from django.shortcuts import get_object_or_404, render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View

from shop.models import Star


class StarListView(ListView):
    queryset = Star.objects.filter(is_active=True)
    template_name = 'shop/star_home.html'


class StarDetailView(View):
    def get(self, request, year: int, month: int, day: int, slug: str):
        object = get_object_or_404(Star, created_at__year=year,
                                   created_at__month=month,
                                   created_at__day=day,
                                   slug=slug)
        context = {'star': object}
        return render(request, 'shop/star_detail.html', context)
