# 类似与view.py的功能
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Classes,Userinfo
from .tojson import Classes_data,Userinfo_data 

@api_view(['GET', 'POST'])
def api_test(requset):
    classes = Classes.objects.all()
    # classes_data = Classes_data(classes,many=True)

    # userinfo = Userinfo.objects.all()
    # userinfo_data = Userinfo_data(userinfo,many=True)

    # data = {
    #     "classes": classes_data.data,
    #     "userinfo": userinfo_data.data 
    # }

    data = {
        'classes':[]
    }
    for c in classes:
        data_item = {
            "id": c.id,
            "text": c.text,
            "userlist": []
        }
        userlist = c.userinfo_classes.all() # 外键，详见models.py
        for user in userlist:
            user_data = {
                "id": user.id,
                "nickName": user.nickname,
                "headImg": str(user.headImg)
            }
            data_item["userlist"].append(user_data)
        data["classes"].append(data_item)
    return Response(data)


@api_view(['GET'])
def getMenuList(requset):
    allClasses = Classes.objects.all()
    
    # 整理数据为json
    data = []
    for c in allClasses:
        # 设计单条数据的结构
        data_item = {
            'id':c.id,
            'text':c.text
        }
        data.append(data_item)
    return Response(data)


@api_view(['GET'])
def getUserList(request):
    menuId = request.GET['id']
    print(menuId)
    menu = Classes.objects.get(id=menuId)
    print(menu)
    userlist = Userinfo.objects.filter(belong=menu)
    print(userlist)
    
    # 开始整理数据列表
    data = []
    for user in userlist:
        data_item = {
            'id':user.id,
            'nickName':user.nickname,
            'headImg':str(user.headImg)
        }
        data.append(data_item)
    return Response(data)




@api_view(['POST'])
def toLogin(request):
    # print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    return Response('ok')