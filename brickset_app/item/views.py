from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse, HttpResponse
from django.views.decorators.http import require_POST

from .forms import ItemForm
from .models import Item, WishList


@login_required
def index(request):
    context = {'items': Item.objects.all()}
    return TemplateResponse(request, 'item/list.html', context=context)


def post(request, post_id):
    return HttpResponse('post_idは = {0}です'.format(post_id))


def news(request, slug):
    return HttpResponse('slugは = {}です'.format(slug))


@login_required
def edit(request, item_id):
    
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_index'))
    else:
        form = ItemForm(instance=item)

    context = {'form': form, 'item': item}
    return TemplateResponse(request, 'item/edit.html', context=context)


@login_required
@require_POST
def delete(request, item_id):
    
    item = get_object_or_404(Item, pk=item_id)
    item.delete()

    return HttpResponseRedirect(reverse('item_index'))


@login_required
@require_POST
def add_to_widh_list(request, item_id):
    
    item = get_object_or_404(Item, pk=item_id)

    wish_list, created = WishList.objects.get_or_create(user=request.user)

    wish_list.items.remove(item)

    return HttpResponseRedirect(reverse('wish_list_index'))

@login_required
def wish_list_index(request):
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    context = {'items': wish_list.items.all()}
    return TemplateResponse(request, 'wish_list/list.html', context=context)
