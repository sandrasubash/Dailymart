from django.shortcuts import render,redirect
from.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Userapp.models import*
from django.db.models.aggregates import Sum

# Create your views here.
def Admin(request):
    return render(request,'admin.html')
def form_category(request):
    return render(request,'add_categories.html')
def Add_category(request):
    if request.method=='POST':
        Cat_name=request.POST['CATEGORY']
        Cat_description=request.POST['DESCRIPTION']
        Cat_image=request.FILES['image']
        data=Category(Category_name=Cat_name,Category_description=Cat_description,Category_Image=Cat_image)
        data.save()
        return redirect('view_category')
def view_category(request):
    data=Category.objects.all()
    return render(request,'view_categories.html',{'data':data})
def edit_category(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'Edit_category.html',{'data':data})
def update_category(request,id):
     if request.method=='POST':
        Cat_name=request.POST['CATEGORY']
        Cat_description=request.POST['DESCRIPTION']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).Category_Image
        Category.objects.filter(id=id).update(Category_name=Cat_name,Category_description=Cat_description,Category_Image=file)
        return redirect('view_category')
def delete_category(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('view_category')
def form_products(request):
    data=Category.objects.all()
    return render(request,'add_products.html',{'data':data})
def add_products(request):
      if request.method=='POST':
        Pro_name=request.POST['PRODUCT']
        Pro_category=request.POST['CATEGORY']
        Pro_description=request.POST['DESCRIPTION']
        Pro_price=request.POST['PRICE']
        Pro_image=request.FILES['IMAGE']
        data=Products(Product_name=Pro_name,Product_category=Pro_category,Product_description=Pro_description,Product_price=Pro_price,Image=Pro_image)
        data.save()
        return redirect('view_products')
def view_products(request):
    data=Products.objects.all()
    return render(request,'view_products.html',{'data':data})
def edit_product(request,id):
    data=Products.objects.filter(id=id)
    data1=Category.objects.all()
    return render(request,'edit_product.html',{'data':data,'data1':data1})
def update_products(request,id):
     if request.method=='POST':
        Pro_name=request.POST['PRODUCT']
        Pro_category=request.POST['CATEGORY']
        Pro_description=request.POST['DESCRIPTION']
        Pro_price=request.POST['PRICE']
        try:
            img_c = request.FILES['IMAGE']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=id).Image
        Products.objects.filter(id=id).update(Product_name=Pro_name,Product_category=Pro_category,Product_description=Pro_description,Product_price=Pro_price,Image=file)
        return redirect('view_products')
def delete_products(request,id):
    Products.objects.filter(id=id).delete()
    return redirect('view_products')
def view_contact(request):
    data=Contact.objects.all()
    return render(request,'view_contact.html',{'data':data})
def view_registrations(request):
    data=Registration.objects.all()
    return render(request,'view_registrations.html',{'data':data})
def view_orders(request):
     data_2=Order.objects.all()
     return render (request, 'view_orders.html',{'data_2':data_2})
def order_not_delivered(request,id):
    Order.objects.filter(id=id).update(status=2)
    return redirect('view_orders')
def order_delivered(request,id):
    data=Order.objects.filter(id=id).update(status=1)
    return redirect('view_orders')  

def adminindex(request):
    Categories = Category.objects.all().count()
    Product = Products.objects.all().count()
    Registrations = Registration.objects.all().count()
    Contacts = Contact.objects.all().count()
    Orders = Order.objects.all().count()
    Wishlist = Products.objects.filter(status=0).count()

    return render(request,'adminindex.html',{'Categories':Categories,'Product':Product,'Registrations':Registrations,'Contacts':Contacts,'Orders':Orders,'Wishlist':Wishlist})

    

