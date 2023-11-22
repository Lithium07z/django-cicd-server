from django.http import JsonResponse
from django.views import View
from .models import Data
from django.shortcuts import render


class index(View):
    def get(self, request):
        if request.GET.get('test'):
            return render(request, 'test.html', {'a': "따흐흑"})
        if request.GET.get('data'):
            d = str(request.GET.get('data'))
        else:
            d = "null"

        Data.objects.create(data=d)
        x = Data.objects.all()
        print(list(x))
        return JsonResponse({'foo': d})
