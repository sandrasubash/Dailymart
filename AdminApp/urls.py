from django.urls import path
from.import views
urlpatterns = [
      path('',views.form_category,name='form_category'),
      path('admin_temp',views.Admin,name='Admin'),
      path('Add_category',views.Add_category,name='Add_category'),
      path('view_category',views.view_category,name='view_category'),
      path('Edit_category/<int:id>/',views.edit_category,name='edit_category'),
      path('update_category/<int:id>/',views.update_category,name='update_category'),
      path('delete_category/<int:id>/',views.delete_category,name='delete_category'),
      path('form_products',views.form_products,name='form_products'),
      path('add_products',views.add_products,name='add_products'),
      path('view_products',views.view_products,name='view_products'),
      path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
      path('update_products/<int:id>/',views.update_products,name='update_products'),
      path('delete_products/<int:id>/',views.delete_products,name='delete_products'),
      path('view_contact',views.view_contact,name='view_contact'),
      path('view_registrations',views.view_registrations,name='view_registrations'),
      path('view_orders',views.view_orders,name='view_orders'),
      path('adminindex',views.adminindex,name='adminindex'),
      path('order_delivered/<int:id>/',views.order_delivered,name='order_delivered'),
      path('order_not_delivered/<int:id>/',views.order_not_delivered,name='order_not_delivered')





]