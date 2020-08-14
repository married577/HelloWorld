import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from App.models import Desk, Reader


def add_desk(request):
    # for i in range(10):
    #     desk = Desk()
    #     desk.d_height = 60 + random.randrange(30)
    #     desk.save()

    Desk.objects.create(d_height=909)  # 这种写法直接存数据不用调用save()

    # Desk.create(d_height=2000)

    return HttpResponse("添加成功！")


def get_desks(request):
    # desks = Desk.objects.filter(d_height__gt=65).filter(d_height__lt=100)  # 取出大于65并小于80的
    # desks = Desk.objects.filter(d_height=75)  # 取出等于75的
    # desks = Desk.objects.exclude(d_height__gt=74)  # 不要大于74的
    # desks = Desk.objects.all()  # 取出全部

    page = int(request.GET.get("page"))
    per_page = 5
    a = Desk.objects.count()
    if page < a:
        desks = Desk.objects.order_by('id')[(page - 1) * per_page:page * per_page]  # id排序
    else:
        return HttpResponse("不存在")



    print(type(desks))
    print(desks.values())

    data = {
        "desks": desks
    }
    return render(request, 'DeskList.html', context=data)


def get_desk(request):
    # desk = Desk.objects.get(pk=2)  # pk为primary
    # desk = Desk.objects.get(d_height=99)  # 只支持找一个数据
    # desk = Desk.objects.exists()  # 如果有数据返回True
    desk = Desk.objects.count()  # 返回数据结果数
    print(desk)

    return HttpResponse("获取某本书")


def add_reader(request):
    reader = Reader()
    reader.r_name = "jack"
    reader.r_pwd = "123@abc"
    reader.save()

    return HttpResponse("注册成功")


def check_reader(request):
    if Reader.objects.filter(r_name="jack1").exists():
        return HttpResponse("用户已存在")
    return HttpResponse("该用户未注册")
