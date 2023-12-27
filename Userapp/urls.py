from django.urls import path
from.import views
urlpatterns = [
      path('user',views.user,name='user'),
      path('card_category',views.card_category,name='card_category'),
      path('categories',views.categories,name='categories'),
      path('card_products/<str:category>/',views.card_products,name='card_products'),
      path('contact',views.contact,name='contact'),
      path('feedback',views.feedback,name='feedback'),
      path('about',views.about,name='about'),
      path('register',views.register,name='register'),
      path('registration',views.registration,name='registration'),
      path('login',views.login,name='login'),
      path('publicdata',views.publicdata,name='publicdata'),
      path('logout',views.logout,name='logout'),
      path('cart',views.cart,name='cart'),
      path('orders',views.orders,name='orders'),
      path('single_view/<int:id>/',views.single_view,name='single_view'),
      path('myorders',views.myorders,name='myorders'),
      path('success',views.success,name='success'),
      path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
      path('delete_cart/<int:id>/',views.delete_cart,name='delete_cart'),
      path('Checkout',views.Checkout,name='Checkout'),
      # path('delete_order/<int:id>/',views.delete_order,name='delete_order')
      path('wishlist',views.wishlist,name='wishlist'),
      path('add_to_wishlist/<int:id>/',views.add_to_wishlist,name='add_to_wishlist'),
      path('product/<int:id>/',views.product,name='product'),
     


]