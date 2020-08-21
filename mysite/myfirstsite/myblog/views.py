from django.shortcuts import render
from myblog.models import SiteInfo

# Create your views here.
def index(request):
    # 在这里写业务逻辑
    # 在这里访问数据库
    print('开始读取数据')
    siteinfo = SiteInfo.objects.all()[0]
    print(siteinfo) # 这里输出什么，由models中的__int__的返回值决定,也可以写__str__
    print(siteinfo.title)

    data = {
        "siteinfo": siteinfo
    }

    return render(request, 'index.html', data)