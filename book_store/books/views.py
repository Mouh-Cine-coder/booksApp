from django.shortcuts import render, redirect
from .models import Book, Author
from account.models import Customer



def index(request):      
        
    best_seller_books = Book.objects.filter(is_best_seller=True)
    popular_books = Book.objects.filter(is_popular=True)
    queryset = Book.objects.all()
    context = {
        'books': queryset,
        'popular_books': popular_books,
        'best_seller_books': best_seller_books
    }
    
    return render(request, "categories.html", context)

def handler404(request, exception):
    
    return render(request, '404.html')

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
    
def manageBook(request):
    
    
    if request.user.is_authenticated:
        if request.user.is_staff:
            authors = Author.objects.all()
            books = Book.objects.all()
            context = {
                'authors': authors,
                'books': books
            }
        
            
            if request.method == "POST":
                
                if 'delete-conf' in request.POST:     
                    delete_id = request.POST['delete-conf']
                    if delete_id:
                        delete_book = Book.objects.get(pk=delete_id)
                        delete_book.delete()
                        return render(request, "layout/manage_book.html", context)
                
                # non blank
                
                author_id = request.POST['author_id']
                title = request.POST['title']
                price = request.POST['price']
                
                # blank
                isbn13 = request.POST.get('isbn13', '')
                
                
                
                book_image = request.FILES['picture']
                resume = request.POST.get('resume', '')
                category = request.POST.get('category', '')

                
                is_popular = True if 'is_popular' in request.POST  else False
                is_best_seller = True if 'is_best_seller' in request.POST else False
                
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
                
            return render(request, "layout/manage_book.html", context)
        else:
            return render(request, "404.html")
    else:
        return redirect("index_page")

def edit_book(request, pk):
    
    if request.user.is_authenticated:
        if request.user.is_staff:
            book = Book.objects.get(pk=pk)
            authors = Author.objects.all()
            
            context = {
                'authors': authors,
                'book': book
            }
            if request.method == "POST":
                is_popular = False
                is_best_seller = False
                # non blank
                title = request.POST['title']
                price = request.POST['price']
                author_id = request.POST['author_id']
                resume = request.POST.get('resume', '')
                category = request.POST.get('category', '')
                isbn13 = request.POST.get('isbn13', '') 
                new_author = Author.objects.get(id=author_id)
                
                book.title = title
                book.price = price
                book.author = new_author
                book.description = resume
                book.categorie = category
                book.isbn13 = isbn13
                
                
                if 'picture'  in  request.FILES:
                    book_image = request.FILES['picture']
                    book.book_image = book_image
                    
                    
                if 'is_popular' in request.POST:
                    if request.POST['is_popular'] == 'on':
                        is_popular = True
                
                if 'is_best_seller' in request.POST:
                    if request.POST['is_best_seller'] == 'on':
                        is_best_seller = True
                
                book.is_popular = is_popular
                book.is_best_seller = is_best_seller
                        
                
                book.save()
                
            return render(request, "layout/edit_book.html", context)
        else:
            return render(request, "404.html")
    else:
        return redirect("index_page")
            
def profile(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = request.user
            if request.method == 'POST':
                first_name = request.POST.get('first_name', '')
                last_name = request.POST.get('last_name', '')
                
                if 'user-picture' in request.FILES:
                    user.user_image =  request.FILES['user-picture']
                
                if 'username' in request.POST and 'email' in request.POST:
                    username = request.POST.get('username')
                    email = request.POST.get('email')
                    
                    user.first_name=first_name.strip()
                    user.last_name=last_name.strip()
                    user.username=username.strip()
                    user.email=email.strip()
            
                else:
                    # change context
                    pass
                
                user.save()
                    
            return render(request, 'layout/profile.html')
        
        else:
            return render(request, "404.html")
    else:
        return redirect("index_page")
        
        
        
    
    

def manage_users(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            
            users = Customer.objects.all().exclude(pk=request.user.id)
            
            context = {
                'users': users
            }
            return render(request, 'layout/manage_users.html', context)
        else:
            return render(request, "404.html")
    else:
        return redirect("index_page")
    
    
def edit_user(request, pk):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            staff = Customer.objects.get(pk=pk)
            
            if request.method == 'POST':
                if 'delete-conf-user' in request.POST:
                    
                    staff.delete()
                    return redirect("manage_users")
                    
            if request.method == 'POST':
                is_staff = False
                is_superuser = False
                
                
                
                first_name = request.POST.get('first_name', '')
                last_name = request.POST.get('last_name', '')
            
                if 'user-picture' in request.FILES:
                    staff.user_image =  request.FILES['user-picture']
                
                if 'username' in request.POST and 'email' in request.POST:
                    username = request.POST.get('username')
                    email = request.POST.get('email')
                    
                    staff.first_name=first_name.strip()
                    staff.last_name=last_name.strip()
                    staff.username=username.strip()
                    staff.email=email.strip()

                else:
                    # change context
                    pass
                

                        
                if 'is_staff' in request.POST:
                    if request.POST['is_staff'] == 'on':
                        is_staff = True
                
                if 'is_superuser' in request.POST:
                    if request.POST['is_superuser'] == 'on':
                        is_superuser = True
                
                staff.is_staff = is_staff
                staff.is_superuser = is_superuser
            
                staff.save()
                
            context = {
                'staff': staff
            }
            return render(request, 'layout/view_edit_user.html', context)
        else:
            return render(request, "404.html")
    else:
        redirect("index_page")
        
def add_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                user_image = None
                is_staff = False
                is_superuser = False
                
                first_name = request.POST.get('first_name', '').strip()
                last_name = request.POST.get('last_name', '').strip()
            
                if 'add_user_picture' in request.FILES:
                    user_image =  request.FILES['add_user_picture']
                
                if 'password' in request.POST:
                    password = request.POST.get('password')
                
                if 'confirm_password' in request.POST:
                    confirm_password = request.POST.get('confirm_password')
                
                
                        
                if 'is_staff' in request.POST:
                    if request.POST['is_staff'] == 'on':
                        is_staff = True
                
                if 'is_superuser' in request.POST:
                    if request.POST['is_superuser'] == 'on':
                        is_superuser = True
                
                
                if 'username' in request.POST and 'email' in request.POST:
                    username = request.POST.get('username').strip()
                    email = request.POST.get('email').strip()
                    if Customer.objects.filter(username=username) or  Customer.objects.filter(email=email):
                        
                        
                        return render(request, 'layout/add_user.html', {'res': 'username or email already exist'})
                    elif confirm_password != password:
                        return render(request, 'layout/add_user.html', {'res': 'password doesnt match'})
                    else:
                        Customer.objects.create_user(
                            username=username,
                            email=email,
                            first_name=first_name,
                            last_name=last_name,
                            user_image=user_image,
                            is_staff=is_staff,
                            is_superuser=is_superuser
                        )
                        return redirect("manage_users")
                        
            return render(request, 'layout/add_user.html')
        else:
            return render(request, "404.html")
    else:
        redirect("index_page")
            
        
        