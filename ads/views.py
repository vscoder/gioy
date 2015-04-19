from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

from django.http import HttpResponse
from django.utils import timezone

from .models import Ad
from .models import Category


class IndexView(generic.ListView):
    # template_name = 'ads/ad_list.html'
    context_object_name = 'latest_ads_list'

    def get_queryset(self):
        """Return last 5 ad's"""
        return Ad.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Ad
    # template_name = 'ads/ad_detail.html'


def category(request):
    return HttpResponse("Hello, world. You're at the categories index.")


def category_detail(request, category_id):
    return HttpResponse("You're looking at Category {}".format(category_id))
