import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from shorts.forms import SubmitURLForm
from shorts.models import ShortURL


def short_url_redirect(request, *args, **kwargs):
    obj = get_object_or_404(ShortURL, short=kwargs.get('slug'))
    obj.visited += 1
    obj.save(update_fields=('visited',))
    return HttpResponseRedirect(obj.url)


class HoveView(View):

    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        context = {
            'form': form
        }
        return render(request, 'main.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            return HttpResponse(json.dumps(
                {'new': request.get_host() + '/' + obj.short,
                 'short': obj.short
                 }
            ))
        return HttpResponse(json.dumps({'errors': form.errors}))
