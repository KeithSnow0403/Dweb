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