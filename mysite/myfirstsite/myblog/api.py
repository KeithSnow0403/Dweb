# 类似与view.py的功能
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password,make_password

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
    # 查询用户数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        # auth_user = authenticate(username=username,password=password)
        # print(auth_user)
        # if auth_user:
        #     return Response('登陆成功')
        # else:
        #     return Response('密码错误')
        user_pwd = user[0].password
        auth_pwd = check_password(password,user_pwd)
        print(auth_pwd)
        if auth_pwd:
            token = Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
            print(token.key)
            data = {
                'token':token.key,
            }
            return Response(data)
        else:
            return Response('pwd_err')
    else:
        return Response('none')



@api_view(['POST'])
# @api_view(['GET','POST'])  好像之前没写上
def toRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username,password,password2)
    # 用户是否存在
    user = User.objects.filter(username=username)
    if user:
        return Response('exist')
    else:
        newPwd = make_password(password,username)
        print(newPwd)
        newUser = User(username=username, password=newPwd)
        newUser.save()
    return Response('ok') 



@api_view(['POST'])
def uploadLogo(request):
    img = request.FILES['logo']
    print(img)
    return Response('ok')