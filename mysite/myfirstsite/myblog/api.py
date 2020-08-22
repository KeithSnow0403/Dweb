# 类似与view.py的功能
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def api_test(requset):
    if requset.method == 'POST':
        return Response('post')
    return Response('ok')