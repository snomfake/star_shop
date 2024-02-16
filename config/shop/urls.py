from django.urls import path

from shop.views import StarListView, StarDetailView

app_name = 'shop'

urlpatterns = [
    path('', StarListView.as_view(), name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         StarDetailView.as_view(), name='detail')
]

