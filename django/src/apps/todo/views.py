from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .models import Item


class HomeView(TemplateView):

    template_name = 'index.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['items'] = Item.objects.all()
        return ctx

    def post(self, request):
        Item.objects.create(text=request.POST['item_text'])
        data = {'items': Item.objects.all()}
        return render_to_response(self.template_name, data)
