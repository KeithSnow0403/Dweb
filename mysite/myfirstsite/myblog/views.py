from django.shortcuts import render

# Create your views here.
def index(request):
    # 在这里写业务逻辑
    # 在这里访问数据库
    return render(request, 'index.html')