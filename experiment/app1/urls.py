from django.urls import path
from.import views

urlpatterns = [
   path('',views.index,name="home"),
   path('searchp',views.searchpage,name="searchp"),
   path('regcod',views.regcod,name="regcod"),
   path('searchpage',views.searchpage,name="searchpage"),
   path('fillname',views.fillname,name="fillname"),
   path('searchcontent',views.searchcontent,name="searchcontent"),
   path('updatecontent',views.updatecontent,name="updatecontent"),  
]
