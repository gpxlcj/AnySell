#! -*- coding:utf8 -*-

from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from apps.home.models import Production, Dormitory, District, Category, Comment, Label
from apps.sell.models import SellCart
from apps.account.models import DetailInfo

from django.contrib.auth import get_user_model

from lib.customjson import render_json

CustomUser = get_user_model()
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
                data = {
                    'status': 10102
                }
                return render_json(data)
            dormitories = Dormitory.objects.filter(district=district)
        else:
            dormitories = Dormitory.objects.all()
        for i in dormitories:
            data.append({'latitude': i.coordinate.latitude, 'longitude': i.coordinate.longitude, 'id': i.id_code})
        return render_json(data)

    else:
        return Http404


def get_production_filter_dormitory(dormitory=None):
    '''
    :param dormitory:宿舍类
    :return: production_list:商品列表
    :introduction: 通过宿舍过滤商品
    '''

    if dormitory:
        production_list = list()
        detail_infos = DetailInfo.objects.filter(dormitory=dormitory)
        for detail_info in detail_infos:
            user = CustomUser.objects.get(user_detail_info=detail_info)
            sellcart = SellCart.objects.get(user=user)
            production_list.append(sellcart.production.all())
        return production_list
    else:
        return None


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
        data = dict()
        productions = list()
        productions_list = list()

        if request.GET.has_key("dormitory"):
            temp = request.GET['dormitory']
            dormitory = Dormitory.objects.filter(id_code=int(temp))
            DetailInfo.objects.get()
            if dormitory:
                dormitory = dormitory[0]
                productions = get_production_filter_dormitory(dormitory)
                if productions:
                    productions_list = productions
                else:
                    data = {
                        'status': EMPTY_ANS,
                    }
                    return render_json(data)

        if request.GET.has_key("district"):
            temp = request.GET['district']
            district = District.objects.filter(id_code=int(temp))
            if not productions_list:

                if district:
                    district = district[0]
                    if not productions_list:
                        dormitories = Dormitory.objects.filter(district=district)
                        temp_productions = list()
                        for dormitory in dormitories:
                            temp_productions = get_production_filter_dormitory(dormitory)
                            if temp_productions:
                                productions_list += temp_productions
                else:
                    productions_list = list()
                    return render_json(data)
            else:
                pass
        if request.GET.has_key("keyword"):
            keyword = str(request.GET['keyword'])
            if keyword:
                labels = Label.objects.filter(name__contains=keyword)
                if labels:
                    temp_productions_list = list()
                    if productions_list:
                        for i_productions in productions_list:
                            for i_label in labels:
                                temp_productions = i_productions.filter(label=i_label)
                                if temp_productions:
                                    temp_productions_list.append(temp_productions)
                        productions_list = temp_productions_list
                    else:
                        productions_list = list()
                        for i_label in labels:
                            temp_productions = Production.objects.filter(label=i_label)
                            if temp_productions:
                                productions_list.append(temp_productions)
                else:
                    data = {
                        'status': EMPTY_ANS,
                    }
                    return render_json(data)
            else:
                pass

        if request.GET.has_key("category"):
            temp = str(request.GET['category'])
            category = Category.objects.filter(name__contains=temp)
            if category:
                category = category[0]
                if productions_list:
                    print productions_list
                    temp_productions_list = list()
                    for i_productions in productions_list:
                        temp_productions = i_productions.filter(category=category)
                        if temp_productions:
                            temp_productions_list.append(temp_productions)
                    productions_list = temp_productions_list
                else:
                    temp_productions = Production.objects.filter(category=category)
                    productions_list.append(temp_productions)
            else:
                data = {
                    'status': EMPTY_ANS,
                }
                return render_json(data)

        if productions_list:
            data_temp = dict()
            data_productions = list()
            for i_productions in productions_list:
                for i_item in i_productions:
                    sellcart = i_item.sell_production.all()[0]
                    data_temp = {
                        'title': i_item.title,
                        'price': i_item.price,
                        'number': i_item.number,
                        'time': str(i_item.publish_time),
                        'dormitory_id': sellcart.user.user_detail_info.dormitory.id_code,
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
