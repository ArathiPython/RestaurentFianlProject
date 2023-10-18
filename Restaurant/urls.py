"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('log/',views.log1),
    path('gouser/',views.gouser1),
    path('create/',views.create1),
    path('createe1/',views.create2),
    path('addres/',views.addres1),
    path('fillres/',views.rest1),
    path('addfeed/',views.feed),
    path('fillfeed/',views.fill1),
    path('menu/',views.menu1),
    path('fillmenu/',views.menu2),
    path('offers/',views.offer),
    path('filloffer/',views.offer1),
    path('viewoffer/',views.viewoff),
    path('viewres/',views.viewrest),
    path('view/',views.offer2),
    path('view1/',views.viewres2),
    path('vfeedbk/',views.vfed),
    path('viewmn/',views.vwmenu),
    path('resadmin/',views.admin1),
    path('up_res/<int:id>',views.update),
    path('up_res1/<int:id>',views.update1),
    path('item1/',views.item_1),
    path('item2/',views.item_2),
    path('up_menu/',views.updatemenu),
    path('up_menu1/<int:id>',views.up_menu11),
    path('up_menu2/<int:id',views.up_menu22),
    path('delmenu/<int:id>',views.del1),
    path('update_item/',views.up_item1),
    path('up_item/<int:id>',views.up1),
    path('update_item2/<int:id>',views.up3),
    path('vfd/',views.v_fd),
    path('v_item/',views.v_item1),
    path('v_feedback/',views.v_fdbk),
    path('v_res/',views.v_res1),
   path('v_fbk/',views.view_fbk),
   path('fd_itm/',views.fditm),
   path('fd_mn/',views.fd_mn1),
   path('v_ofr/',views.offr2),
   path('v_retn/',views.res2),
   path('v_fbk1/',views.fbk1),
   path('up_off/',views.offer3),
   path('updt_of/',views.up_off1),
   path('up_offr2/<int:id>',views.updt_off3),
   path('logout/',views.logout),
   path('u_home/',views.u_home),
   path('a_home/',views.a_home),
   path('out/',views.out),
   path('r_home/',views.r_home),
   path('homee/',views.homee),
   path('delt_res/<int:id>',views.delt_res),
   path('v_w/',views.v_w),
   path('vi_ew/<int:id>',views.vi_ew),
   path('addtocart/<int:id>',views.addtocart),
   path('add_cart/',views.add_cart),
   path('v_cart/',views.v_cart),
   path('or_der/<int:id>',views.or_der),
   path('order/<int:id>',views.order),
   path('vieworder/',views.vieworder),
   path('order1/',views.order1),
   path('change0/<int:id>',views.change0),
   path('change1/<int:id>',views.change1),

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)