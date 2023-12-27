from django.shortcuts import render,redirect
from AdminApp.models import*
from.models import*
from django.db.models.aggregates import Sum
import stripe
from django.conf import settings
# Create your views here.
def user(request):
    u = request.session.get('u_id')
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    data2=Category.objects.all()
    return render(request,'user.html',{'data2':data2,'cart':cart,'Wishlist':Wishlist})
def card_category(request):
    u = request.session.get('u_id')
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    data=Category.objects.all()
    return render(request,'card_category.html',{'data':data,'cart':cart,'Wishlist':Wishlist})
def categories(request):
    u = request.session.get('u_id')
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    data=Category.objects.all()
    return render(request,'categories.html',{'data':data,'cart':cart,'Wishlist':Wishlist})
def card_products(request,category):
    u = request.session.get('u_id')
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    if (category=="all"):
        data=Products.objects.all()
    else:
        data=Products.objects.filter(Product_category=category)
    data2=Category.objects.all()
    return render(request,'card_product.html',{'data':data,'data2':data2,'cart':cart,'Wishlist':Wishlist})
def contact(request):
    u = request.session.get('u_id')
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    return render(request,'contact.html',{'cart':cart,'Wishlist':Wishlist})
def feedback(request):
     if request.method=='POST':
        Name=request.POST['NAME']
        Email=request.POST['EMAIL']
        Message=request.POST['MESSAGE']
        data=Contact(Name=Name,Email=Email,Message=Message)
        data.save()
        return redirect ('view_contact')
def about (request):
      u = request.session.get('u_id')
      cart = Cart.objects.filter(user_id=u,status=0).count()
      Wishlist = Products.objects.filter(status=1).count()
      data2=Category.objects.all()
      return render(request,'about.html',{'data2':data2,'cart':cart,'Wishlist':Wishlist})
def register(request):
     return render(request,'register.html')
def registration(request):
     if request.method=='POST':
        Name=request.POST['NAME']
        Email=request.POST['EMAIL']
        Phone=request.POST['PHONE']
        Password=request.POST['PASSWORD']
        data=Registration(Name=Name,Email=Email,Phone=Phone,Password=Password)
        data.save()
        return redirect ('view_registrations')
def login(request):
     return render(request,'login.html')
def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('NAME')
        password=request.POST.get('PASSWORD')
        if Registration.objects.filter(Name=username,Password=password).exists():
           data = Registration.objects.filter(Name=username,Password=password).values('id','Phone','Email').first()
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['Phone'] 
           request.session['email_u'] = data['Email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('card_category') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('user')

def logout(request):
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')

def single_view(request,id):
    u = request.session.get('u_id')
    data=Products.objects.filter(id=id)
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    return render(request,'Product_singleview.html',{'data':data,'cart':cart,'Wishlist':Wishlist})
def myorders(request):
    u = request.session.get('u_id')
    data = Order.objects.filter(user_id=u)
    s=Cart.objects.filter(user_id=u,status=0).aggregate(Sum('total_amt'))
    cart = Cart.objects.filter(user_id=u,status=0).count()
    return render (request, 'myorders.html',{'data':data,'s':s,'cart':cart})

def success(request):
    return render (request,'success.html')
########################################################
def cart(request):
    u = request.session.get('u_id')
    data = Cart.objects.filter(user_id=u,status=0)
    s=Cart.objects.filter(user_id=u,status=0).aggregate(Sum('total_amt'))
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    return render (request, 'cart.html',{'data':data,'s':s,'cart':cart,'Wishlist':Wishlist})

def add_to_cart(request,id):
    user_id = request.session.get('u_id')
    if request.method == "POST":
        try:
            quantity = request.POST['product_quantity']
            product_total = request.POST['product_total']
        # total_amt = request. POST['product_total']
            data = Cart(
                user_id = Registration.objects.get(id=user_id),
                product_id = Products.objects.get(id = id),
                total_amt = product_total,
                quantity=quantity
                )
            data.save()
        except:
            return render(request,'register.html',{'msg':'Please Register to Continue'})
        return redirect ('cart')
def delete_cart(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')
def orders(request):
    u = request.session.get('u_id')
    data = Cart.objects.filter(user_id=u,status=0)
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    s=Cart.objects.filter(user_id=u,status=0).aggregate(Sum('total_amt'))
    return render (request, 'orders.html',{'data':data ,'s':s,'cart':cart,'Wishlist':Wishlist})
stripe.api_key=settings.STRIPE_SECRET_KEY
def Checkout(request):
    if request.method=="POST":
        user_id=request.session.get('u_id')
        Address=request.POST['ADDRESS']
        town=request.POST['TOWN']
        pin=request.POST['PIN']
        orders = Cart.objects.filter(user_id=user_id,status=0)
        total_amount=0
        for i in orders:
            total_amount+=i.total_amt
        session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[{
                    'price_data':{
                        'currency': 'inr',
                        'product_data':{
                            'name': 'product.name,'
                        },
                        'unit_amount':int(total_amount)*100,
                    
                    },
                    'quantity':1,
            }],
            mode='payment',
            success_url = "http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url = "http://127.0.0.1:8000/pay_cancel",
            # client_reference_id=product_id,
        )
        return redirect(session.url, code=303)
            # data=Order(Address=Address,
           #        town=town,
            #        Pincode=pin,
            #        user_id = Registration.objects.get(id=user_id),
            #        cart_id= Cart.objects.get(id=i.id)
            #        )
            # data.save()
            # Cart.objects.filter(id=i.id).update(status=1)
    return redirect('success')

# def delete_order(request,id):
#     Cart.objects.filter(id=id).delete()
#     return redirect('myorders')
def wishlist(request):
    u = request.session.get('u_id')
    data = Products.objects.filter(status=1)
    cart = Cart.objects.filter(user_id=u,status=0).count()
    Wishlist = Products.objects.filter(status=1).count()
    return render (request, 'wishlist.html',{'data':data,'cart':cart,'Wishlist':Wishlist})
def add_to_wishlist(request,id):
    data=Products.objects.filter(id=id).update(status=1)
    return redirect('wishlist')  
def product(request,id):
     data=Products.objects.filter(id=id)
     Wishlist = Products.objects.filter(status=1).count()
     return render(request,'singleview.html',{'data':data,'Wishlist':Wishlist})
