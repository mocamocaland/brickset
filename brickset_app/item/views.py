#from django.shortcuts import render
#from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime



def hello(request):
    #name = request.POST['name']
    #return HttpResponse('nameは {0) です'.format(name))

    context = {
        'message': 'メッセージ',
        'today': datetime.date.today(),
        }

    return TemplateResponse(request, 'item/message.html', context=context)
'''
def post(request, post_id):
    return HttpResponse('post_idは = {0}です'.format(post_id))

def news(request, slug='test'):
    return HttpResponse('slugは = {}です'.format(slug))
'''