from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
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


def categories(request):
    return render_to_response("ads/categories.html",
                    {'nodes': Category.objects.all()},
                    context_instance=RequestContext(request))

def category_detail(request, category_id):
    #context = {}
    return HttpResponse("You're looking at Category {}".format(category_id))
