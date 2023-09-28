from django.shortcuts import render, redirect
from .models import Book, Author
from django.http import JsonResponse



def index(request):      
    # print(request.GET)  
    # category = request.GET.get('category', '')
    # if category:
    #     queryset = Book.objects.filter(categorie=category)
    #     context = {
    #         'books': queryset,
    #         'popular_books': popular_books,
    #         'best_seller_books': best_seller_books
    #     }
    # else:
        
    best_seller_books = Book.objects.filter(is_best_seller=True)
    popular_books = Book.objects.filter(is_popular=True)
    queryset = Book.objects.all()
    context = {
        'books': queryset,
        'popular_books': popular_books,
        'best_seller_books': best_seller_books
    }
    
    return render(request, "categories.html", context)


def category(request, cats):

    
    queryset = Book.objects.filter(categorie=cats)
    best_seller_books = Book.objects.filter(is_best_seller=True)
    popular_books = Book.objects.filter(is_popular=True)
    context = {
        'books': queryset,
        'popular_books': popular_books,
        'best_seller_books': best_seller_books
    }
    return render(request, 'categories.html', context)
    
def admin_dashboard(request):
    # if request.user.is_authenticated:
    #     if request.user.is_superuser:
    #         return render(request, "layaout/dashboard_sideBar.html")
    # else:
    #     return redirect('index_page')
        
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books
    }
    
    if request.method == "POST":
        
        # non blank
        
        author_id = request.POST['author_id']
        title = request.POST['title']
        price = request.POST['price']
        
        # blank
        isbn13 = request.POST.get('isbn13', '')
        
        
        
        book_image = request.FILES['picture']
        resume = request.POST.get('resume', '')
        category = request.POST.get('category', '')

        
        is_popular = True if request.POST['is_popular'] == "on" else False
        is_best_seller = True if request.POST['is_best_seller'] == "on" else False
        
        author = Author.objects.get(id=author_id)
        
        new_book = Book.objects.create(
            title=title,
            isbn13=isbn13,
            description=resume,
            is_popular=is_popular,
            is_best_seller=is_best_seller,
            categorie=category,
            price=price,
            book_image=book_image,
            author=author
        )
        
        new_book.save()
        
        
        
    
    return render(request, "layout/dashboard_sideBar.html", context)
            
    


    