#! -*- coding:utf8 -*-

from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from apps.home.models import Production, Dormitory, District, Category, Comment, Label

from lib.customjson import render_json


EMPTY_ANS = 10101
DATA_ANS = 11101

def get_dormitory(request):
    '''
    通过学部名获取宿舍楼
    '''

    if request.method == 'GET':

        dormitories = str()
        latitude = float()
        longitude = float()
        data = list()
        if request.GET.has_key('district'):
            district_id = int(request.GET['district'])
            try:
                district = District.objects.get(id_code=district_id)
            except:
                return Http404
            dormitories = Dormitory.objects.filter(district=district)
        else:
            dormitories = Dormitory.objects.all()
        for i in dormitories:
            data.append({'latitude': i.coordinate.latitude, 'longitude': i.coordinate.longitude, 'id': i.id_code})
        return render_json(data)

    else:
        return Http404

def get_production_by_research(request):
    '''
    通过搜索关键词获取物品
    '''

    '''
    :param request:
    :return render_json:
    '''
    if request.method == 'GET':

        temp = str()
        keyword = str()
        dormitory = str()
        distrct = str()
        category = str()
        label = str()
        data = str()
        productions = list()
        productions_list = list()

        if request.GET.has_key("dormitory"):
            temp = request.GET['dormitory']
            dormitory = Dormitory.objects.filter()
            if dormitory:
                dormitory = dormitory[0]
                productions = Production.objects.filter(dormitory=dormitory)
                productions_list.append(productions)

        if request.GET.has_key("district"):
            temp = request.GET['district']
            district = District.objects.filter(name=temp)
            if district:
                district = district[0]
                if not productions:
                    dormitories = Dormitory.objects.filter(district=district)
                    temp_productions = list()
                    for i in dormitories:
                        temp_productions = Production.objects.filter(dormitory=i)
                        if temp_productions:
                            productions_list.append(temp_productions)
            else:
                productions_list = list()
                return render_json(data)

        if request.GET.has_key("keyword"):
            keyword = request.GET['keyword']
            labels = Label.objects.filter(name__icontains=keyword)
            if labels:
                if productions_list:
                    for i_productions in productions_list:
                        for i_label in labels:
                            temp_productions = i_productions.objects.filter(label=i_label)
                            if temp_productions:
                                productions_list.append(temp_productions)
                else:
                    productions_list = list()
                    for i_label in labels:
                        temp_productions = Production.objects.filter(label=i_label)
                        if temp_productions:
                            productions_list.append(temp_productions)
            else:
                productions_list = list()
                return render_json(data)

        if request.GET.has_key("category"):
            temp = request.GET['category']
            category = Category.objects.filter(name=temp)
            if category:
                category = category[0]
                if productions_list:
                    for i_productions in productions:
                        temp_productions = i_productions.objects.filter(category=category)
                        if temp_productions:
                            productions_list.append(temp_productions)
                else:
                    temp_productions = Production.objects.filter(category=category)
                    productions_list.append(temp_productions)
            else:
                productions_list = list()

        if productions_list:
            data_temp = dict()
            data_productions = list()
            for i_productions in productions_list:
                for i_item in i_productions:
                    data_temp = {
                        'title': i_item.title,
                        'price': i_item.price,
                        'number': i_item.number,
                        'time': i_item.publish_time,
                        'dormitory_id': i_item.sell_cart.user.user_detail_info.dormitory.id_code,
                    }
                    data_productions.append(data_temp)
            data = {
                'status': DATA_ANS,
                'productions': data_productions
            }

        else:
            data = {
                'status': EMPTY_ANS,
            }


        return render_json(data)

    else:
        return Http404