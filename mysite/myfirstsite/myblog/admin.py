from django.contrib import admin
from myblog.models import SiteInfo,Classes,Userinfo
# Register your models here.
admin.site.register(SiteInfo) # Django自带，用来看后台
admin.site.register(Classes)
admin.site.register(Userinfo)