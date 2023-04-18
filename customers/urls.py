from django.urls import path
from django.conf.urls import include
from django.urls import path
from . import views



app_name = 'customers'
urlpatterns = [  
    path('<str:username>/customers/<int:id>/update', views.updateCustomer),
    path('<str:username>/customers/<int:id>/delete', views.deleteCustomer),
    path('<str:username>/customers/<int:id>', views.customerDetail),
    path('<str:username>/customers/add', views.addCustomer),
    path('<str:username>/customers', views.customerList),

]
