from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Recipy, Product, Fridge

def home_page(request):
    return render(request, 'home.html', {
        "pages": Recipy.objects.all(),
    })

def fridge(request):
    error = False
    if request.method == "POST":
        if request.POST['action'] == 'DELETE':
            id = request.POST['fridge_id']
            f = Fridge.objects.get(pk=id)
            f.delete()
            return redirect("/fridge")
        name = request.POST["product_name"]
        if len(name)<3:
            error = "word must be longer than 2 letters"
        else:
            name = name[0].upper() + name[1:].lower()
            new_product, created = Product.objects.get_or_create(name = name)
            f, created = Fridge.objects.get_or_create(owner = request.user, product = new_product)
            if not created:
                error = 'Product %s is already in your fridge!' % name
            else:
                return redirect("/fridge")
    my_fridge = request.user.fridge_set.all()
    recipys = Recipy.objects.raw('''
        select * from frigerator_recipy where id not in (

            select recipy_id from frigerator_ingredient where product_id in (
                select id from frigerator_product where id not in (%s)
            )
        )
    ''' % ','.join(str(i.product.id) for i in my_fridge));

    return render(request, 'products.html', {
        "products": my_fridge,
        "username": request.user.username,
        "recipys": recipys,
        "error": error,
    })