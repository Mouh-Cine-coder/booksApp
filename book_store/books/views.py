from django.shortcuts import render, redirect
from .models import Book
from django.http import JsonResponse



def index(request):      
    print(request.GET)  
    category = request.GET.get('category', '')
    best_seller_books = Book.objects.filter(is_best_seller=True)
    popular_books = Book.objects.filter(is_popular=True)
    if category:
        queryset = Book.objects.filter(categorie=category)
        context = {
            'books': queryset,
            'popular_books': popular_books,
            'best_seller_books': best_seller_books
        }
    else:    
        queryset = Book.objects.all()
        context = {
            'books': queryset,
            'popular_books': popular_books,
            'best_seller_books': best_seller_books
        }
    
    return render(request, "products.html", context)


# def products_api(request):
    
#     res = None
#     queryset = Book.objects.filter(categorie=category)
#     print(category)
#     print(queryset)
   
#     if queryset and category: 
#         data = []
#         for book in queryset:
#             # we need | title  | writer | price 
#             item = {
#                 'pk': book.pk,
#                 'title': book.title,
#                 'image': book.book_image.name,
#                 'author': book.author.all()[0].first_name,
#                 'price': book.price
#             }
#             data.append(item)
#         res = data
#     elif len(queryset) == 0:
#         res = 'No book found ...'
#     else: 
#         return JsonResponse({}, status = 400)
        
#     return JsonResponse({ 'data': res })
    
    
    
def admin_dashboard(request):
    # if request.user.is_authenticated:
    #     if request.user.is_superuser:
    #         return render(request, "layaout/dashboard_sideBar.html")
    # else:
    #     return redirect('index_page')
    
    return render(request, "layaout/dashboard_sideBar.html")
            
    


    