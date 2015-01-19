#! -*- coding:utf8 -*-
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from apps.home.models import Production, Dormitory, District, Category, Comment, Label

from lib.customjson import render_json

INDEX_HTML = 'index.html'
EMPTY_ANS = 10101
DATA_ANS = 11101

class DormitoryListByDistrict:
    dormitory = list()
    dormitories = list()
    district = str()

def index(request):

    '''
    访问首页
    :param request: class django Request
    :return: class django Response
    '''
    if request.method=='GET':

        username = str()
        user = request.user
        if user.is_anonymous():
            print 'ok'
            username = ""
        else:
            username = user.username
        districts = District.objects.all()
        dormitaries = Dormitory.objects.all()
        latitudes = list()
        longitudes = list()

        total = 0
        for i in dormitaries:
            latitudes.append(i.coordinate.latitude)
            longitudes.append(i.coordinate.longitude)
            total += 1

        for i in districts:
            pass

        return render_to_response(INDEX_HTML, locals())

    elif request.method=='POST':

        if request.POST.has_key('q'):
            pass
        else:
            return render_to_response(INDEX_HTML, locals())
        
        return render_to_response(INDEX_HTML, locals())

    else:
        return Http404
def publish(request):

    if request.method == 'GET':
        user = request.user
        if user.is_anonymous():
            return HttpResponseRedirect("/account/login/")
        else:
            if not user.user_detail_info.phone and user.user_detail_info.dormitory:
                return HttpResponseRedirect("/account/usercenter/")
            else:
                pass
        categories = Category.objects.all()
        districts = District.objects.all()
        return render_to_response('publishgoods.html', locals())
    elif request.method == 'POST':
        pass
    else:
        return Http404

def research(request):

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

def product_info(request, pro):

#    try:
    if request.method == 'GET':
        product = Production.objects.filter(id=int(pro))
        if product:
            product = product[0]
        else:
            HttpResponse('No product like this')

        return render_to_response('goodmodel.html', locals())
    else:
        return Http404
#    except:
    return HttpResponse('Server error')

def production_list(request):

    if request.method == 'GET':
        try:
            production_list_by_hit = Production.objects.order_by('hit_num')
            production_list_by_time = Production.objects.order_by('publish_time')
            if len(production_list_by_hit)>3:
                production_list_by_hit = production_list_by_hit[4]
                production_list_by_time = production_list_by_time[4]
            else:
                pass
        except:
            return Http404
    else:
        return HttpResponse("Don't support this kind request method")
    return render_to_response('production_list', locals())