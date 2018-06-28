"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from 






urlpatterns = [
    url(r'^admin/', admin.site.urls),
#   url(r'^index/$', views.index),                       //映射

#    url(r'^host/(\d+)$', views.host),                   //按照顺序放置的动态路由     
#    相对应的url是： ”http://127.0.0.1/host/2“ (\d+)是匹配任意的数字，在分页时灵活运用。
#    在views.host中需要指定一个形式参数来接受(\d+)\$ 的值
#     def user_list(request,id):
#     return HttpResponse(id)

#    \^host_list/(\d+)/(\d+)$
#    相对应的url是： ”http://127.0.0.1/host/8/9“，匹配到的数字会以参数的形式按照顺序传递给views里面相对应的函数
#    在views.host_list中需要指定两个形式参数,注意：此参数的顺序严格按照url中匹配的顺序
#     def user_list(request,hid,hid2): 
#     return HttpResponse(hid+hid2


#利用正则表达式的分组方法，将url以参数的形式传递到函数，可以不按顺序排列
#urlpatterns = [ 
#     url(r'^user_list/(?P<v1>\d+)/(?P<v2>\d+)$',views.user_list),     //传形式参数的路由
# ]
#(?P<v1>\d+)
#正则表达式的分组，相当于一个字典， key=v1, value=\d+。 {"v1":"\d+"}
#然后将此参数传递到views里对应的函数，可以不按照顺序
#def user_list(request,v2,v1):
#     return HttpResponse(v1+v2)
#参数v1 = (?P<v1>\d+)
#参数v2 = (?P<v2>\d+)
 
 
    ('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))/(?P<id>(\d+))/$',process),
    ('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\d+))/$',process),
    ('^(?P<app>(\w+))/(?P<function>(\w+))/$',process),
    ('^(?P<app>(\w+))/$',process,{'function':'index'}),
 
 
 
 
#根据不同的app来分类不同的url请求
    url(r'^blog/', include("blog.urls")),  
]
