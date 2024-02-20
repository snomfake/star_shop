from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from shop.models import Star


class StarListView(View):
    def get(self, request) -> HttpResponse:
        stars: Star = Star.objects.filter(is_active=True)
        context = {"stars": stars}
        return render(request, "shop/star_home.html", context)


class StarDetailView(View):
    def get(self, request, year: int, month: int, day: int, slug: str) -> HttpResponse:
        star: Star = get_object_or_404(
            Star,
            created_at__year=year,
            created_at__month=month,
            created_at__day=day,
            slug=slug,
        )
        context = {"star": star}
        return render(request, "shop/star_detail.html", context)
