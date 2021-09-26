from django.shortcuts import render



def product_view(request, pk):
    if request.method == "GET":
        return render(request, 'templates/product.html')
