#! -*- coding:utf8 -*-

from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from apps.home.models import Production, Dormintary, District, Category, Comment
from lib.customjson import render_json


def get_dorm_by_district(request):
    '''
    通过学部名获取宿舍楼
    '''

    if request.method == 'GET':

        dormintaries = str()
        latitude = float()
        longitude = float()
        data = list()
        if request.GET.has_key('dorm'):
            district_id = request.GET['dorm']
            try:
                district = District.objects.get(id=district_id)
            except:
                return Http404
            dormintaries = Dormintary.objects.filter(district=district)
        else:
            dormintaries = Dormintary.objects.all()
        for i in dormintaries:
            data.append({'latitude': i.coordinate.latitude, 'longitude': i.coordinate.longitude})
        return render_json(data)

    else:
        return Http404

def get_product_by_research(request):
    '''
    通过搜索关键词获取物品
    '''

    if request.method == 'GET':
        pass
    else:
        pass
