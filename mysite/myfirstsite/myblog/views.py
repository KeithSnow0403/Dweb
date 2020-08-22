from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from myblog.models import SiteInfo, Classes, Userinfo

# Create your views here.
def index(request):
    # 在这里写业务逻辑
    # 在这里访问数据库

    # 站点基础信息
    print('开始读取数据')
    siteinfo = SiteInfo.objects.all()[0]
    print(siteinfo) # 这里输出什么，由models中的__int__的返回值决定,也可以写__str__
    print(siteinfo.title)

    #菜单分类
    classes = Classes.objects.all()

    #全部用户
    userlist = Userinfo.objects.all()

    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist
    }

    return render(request, 'index.html', data)

def classes(request):
    # 站点基础信息
    siteinfo = SiteInfo.objects.all()[0]
    # 菜单分类
    classes = Classes.objects.all()
    # 当前用户列表
    try:
        # 以下为判断班级（id）是否存在，不存在直接甩回主页
        choosed_id = request.GET['id']
        print(choosed_id)
        choosed = Classes.objects.filter(id=choosed_id) # 之前删除过两次，所以从3开始
        print(choosed)
    except:
        return redirect('/')

    # 班级里无对象，则赋值[]
    if choosed:
        userlist = Userinfo.objects.filter(belong=choosed[0])
    else:
        userlist = []
    
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist
    }

    return render(request, 'classes.html', data)