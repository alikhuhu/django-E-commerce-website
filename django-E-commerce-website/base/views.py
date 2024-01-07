from django.shortcuts import render , redirect
from . import models
from django.contrib.auth import login , logout , authenticate 
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import order_form , signup ,signup2
from django.contrib.auth import authenticate , login , logout



# Create your views here.

from django.db import connection
print(connection.queries)

def home(request):
    items= models.item.objects.filter(is_solde=False)
    deal = models.deal.objects.all()
    return render(request,'base/home.html',{'items':items,'deal':deal})




def item_pro(request,pk):
    mm=False
    pk = pk
    item = models.item.objects.get(pk=pk)
    iteml = models.item.objects.filter(item_type=item.item_type)[:3]
    form = order_form()
    order = None
    if request.user.is_authenticated:
        order = models.orders.objects.filter(user_ord=request.user , item_ord = item).first()

    isordert = False
    if order != None:
        isordert = True


    if request.method == "POST" and isordert == False:
        if request.user.is_authenticated:
            r = request.POST.copy()
            r['user_ord'] =request.user
            r['item_ord'] = item
            r['size'] = str(request.POST.get('size'))
            form = order_form(r)
            if form.is_valid():
                form.save()

                order = models.orders.objects.filter(user_ord=request.user , item_ord = item).first()

                isordert = False
                if order != None:
                    isordert = True



        elif isordert == False:
            messages.info(request,'you alrady ordert')
        else:
            messages.info(request,'you alrady ordert')
            return redirect(request,'login')


    return render(request,'base/item_pro.html',{'item':item,'iteml':iteml,'mm':mm ,'form':form , 'isordert':isordert})




def delet(request,pk):
    k=pk
    item = models.item.objects.get(pk=pk)
    itemo= models.orders.objects.get(user_ord=request.user , item_ord = item)
    itemo.delete()
    return redirect('item_pro',pk=k)





def saign_in(request):
    formm = signup()
    if request.method == 'POST':
        r = request.POST.copy()
        r['password'] =request.POST.get('password')
        r['username'] = str(request.POST.get('username'))
        form = signup(r)
        if form.is_valid():
            u = form.save()
            login(request,u)

            r2 = request.POST.copy()
            g = User.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
            r2['user']=g
            f=signup2(r2)
            if f.is_valid():
                f.save()
            

            return redirect('home')



    return render(request, 'base/singup.html',{'formm':formm})


def loginn (request):
    if request.method == 'POST':
        u = authenticate(username=request.POST.get('username')),request.POST.get('password')
        if u != None:
            login(request,u)
            return redirect('home')
    return render(request, 'base/login.html')

''' https://i.postimg.cc/SsC7D5WD/b2.jpg '''
def deal(request,pk):
    d = models.deal.objects.get(name=pk)
    items= models.item.objects.filter(item_deal=d.id)
    return render(request,'base/deal.html',{'deal':deal,'items':items})

def about(request):
    return render(request,'base/about.html')

