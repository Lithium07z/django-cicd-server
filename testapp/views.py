from django.http import JsonResponse
from django.views import View
from .models import Data
from django.shortcuts import render
from .serializers import DataSerializer
from .models import Data
from django.http import HttpResponse
import json

class index(View):
    def get(self, request):
        if request.GET.get('test'):
            return render(request, 'test.html', {'a': "따흐흑"})
        if request.GET.get('data'):
            d = str(request.GET.get('data'))
        else:
            d = "null"

        return JsonResponse({'foo': d})

class refresh(View):
    def get(self, request):
        data = Data.objects.all()
        a = DataSerializer(data, many=True).data
        result = {
            "msg":"ok",
            "data":a
        }
        return HttpResponse(json.dumps(result), content_type = "application/json")
    
class send(View):
    def get(self, request):
        name = request.GET.get('name')
        message = request.GET.get('message')
        x = Data.objects.create(username=name, data=message)
        data = Data.objects.all()
        a = DataSerializer(data, many=True).data
        result = {
            "msg":"ok",
            "data":a
        }
        return HttpResponse(json.dumps(result), content_type = "application/json")