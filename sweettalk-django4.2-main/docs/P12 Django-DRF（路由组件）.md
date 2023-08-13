---
title: P12 Django-DRF（路由组件）
date: 2023-06-28T17:10:42Z
lastmod: 2023-06-30T20:20:55Z
---

# P12 Django-DRF（路由组件）

## 是什么？

　　​`DefaultRouter`​是Django REST framework中提供的一个路由器类，用于自动生成URL路由。

　　路由器是将URL与视图函数或视图集关联起来的一种机制。Django REST framework的路由器通过简单的配置可以自动生成标准的URL路由，从而减少了手动编写URL路由的工作量。

## DefaultRouter的使用方法

**urls.py**

```python
from django.contrib import admin
from django.urls import path
from apps.erp_test.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('GoodsCategory', GoodsCategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filtergoodscategory/', FilterGoodsCategory),
    path('insertGoodsCategory/', InsertGoodsCategory),
    path('filtergoodscategoryapi/', FilterGoodsCategoryAPI.as_view()),
    path('getgoods/', GetGoods.as_view()),
]
urlpatterns += router.urls
```

　　使用`routers.DefaultRouter()`​创建了一个默认的路由器对象，并使用`router.register()`​方法注册了两个视图集，分别是`TestModelViewSet`​和`CategoryModelViewSet`​。这样可以自动为这两个视图集生成对应的URL路由，并将其添加到`urlpatterns`​中。
