import json
#from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
#from django.views.decorators.http import require_http_methods
#from django.views.decorators.csrf import csrf_exempt
from item.models import (
    Item,
    WishList,
)


def item_list(request):
    item_json_list = []
    for item in Item.objects.all():
        item_json_list.append(item.to_dict())
    return JsonResponse(item_json_list, safe=False)


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse(item.to_dict())


