from django.shortcuts import render
from django.http import HttpResponse
from .models import DaZhong
# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listdazhong(request):
      daZhongs = DaZhong.objects.all()  #查询结果集
      paginator = Paginator(daZhongs, 10, 4)     #每页显示25条数据,少于2条则合并到上一页
      page = request.GET.get('page')    #获得前端查看数据的页码

      try:
          dazhongsye  = paginator.page(page)   #分页结果集
      except PageNotAnInteger:
          dazhongsye = paginator.page(1)  #如果用户请求的页码号不是整数，显示第一页
      except EmptyPage:
          dazhongsye = paginator.page(paginator.num_pages)    #如果用户请求的页码号超过了最大页码号，显示最后一页

      return render(request,'list2.html',{"DAZHONGS":dazhongsye})

#删除一条记录
def delete(request):
     id = request.GET.get("id")
     DaZhong.objects.get(pk=id).delete()
     return listdazhong(request)

#查询所有
def toadd(request):
    return render(request,'add.html')

#增加一条记录
def add(request):
    shop_name= request.POST.get("shop_name")
    shop_reviewcount = request.POST.get("shop_reviewcount")
    shop_avgpricetitle = request.POST.get("shop_avgpricetitle")
    shop_effect = request.POST.get("shop_effect")
    shop_service = request.POST.get("shop_service")
    shop_surroundings = request.POST.get("shop_surroundings")
    shop_address = request.POST.get("shop_address")
    shop_telephonenumber = request.POST.get("shop_telephonenumber")
    shop_businesshours = request.POST.get("shop_businesshours")
    shop_url = request.POST.get("shop_url")
    shop_star = request.POST.get("shop_star")
    DaZhong(shop_name=shop_name,shop_reviewcount=shop_reviewcount,shop_avgpricetitle=shop_avgpricetitle,shop_effect=shop_effect, shop_service=shop_service, shop_surroundings=shop_surroundings, shop_address=shop_address, shop_telephonenumber=shop_telephonenumber, shop_businesshours=shop_businesshours, shop_url=shop_url, shop_star=shop_star).save()
    return listdazhong(request)

#查看详情
def info(request):
    id = request.GET.get("id")
    dazhong = DaZhong.objects.get(pk=id)
    return render(request,'update.html',{"DAZHONG":dazhong})

#修改一条记录
def update(request):
        id = request.POST.get("id")
        dazhong = DaZhong.objects.get(pk=id)
        dazhong.projectName=request.POST.get("shop_name")
        dazhong.startDate=request.POST.get("shop_address")
        dazhong.endDate =request.POST.get("shop_telephonenumber")
        dazhong.status = request.POST.get("shop_businesshours")
        dazhong.save()
        return listdazhong(request)


def listlike(request):
    shop_address = request.POST.get("shop_address")
    shop_effect = request.POST.get("shop_effect")
    shop_service = request.POST.get("shop_service")
    shop_star = request.POST.get("shop_star")
    # print(projectName + "\t" + status)
    dazhongs = DaZhong.objects.filter(shop_address__contains=shop_address,shop_effect__contains=shop_effect, shop_service__contains=shop_service, shop_star__contains=shop_star)
    return render(request, 'list2.html', {"DAZHONGS": dazhongs})