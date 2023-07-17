from django.shortcuts import render
from .models import Book,Category
from django.views.generic.list import ListView 

  
# def all_books(request):
#     books=Book.objects.all()
#     category=Category.objects.all()
#     return render(request,'app/all_books.html',{'books':books,'categories':category})

def category_books(request,id):
    category=Category.objects.get(id=id)
    category_book=category.book_set.all()
    return render(request,'app/category_books.html',{'category_books':category_book})

def view_book(request,id):
    book=Book.objects.get(id=id)
    return render(request,'app/view_book.html',{'book':book})

class SearchView(ListView):
    model=Book
    template_name='app/search_form.html'
    context_object_name='posts'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['posts'] = context['posts'].order_by('-create_at')
        
        search=self.request.GET.get('search') or ''
        if search:
            context['posts'] = context['posts'].filter(book_name__startswith=search)
            context['search'] = search
        return context        
    
