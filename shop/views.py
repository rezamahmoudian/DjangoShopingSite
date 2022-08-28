from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Category,Product

# Create your views here.

# class ProuductList(ListView):
#     model = Product
#     paginate_by = 5
#
#     def get_queryset(self):
#         global category
#         category = self.kwargs.get('category_slug')
#
#     def get_context_data(self, **kwargs):
#         category_slug = self.kwargs.get('category_slug')
#         category = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=category, available=True)
#
#         context = super(ProuductList, self).get_context_data(**kwargs)
#
#         return context


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(available=True, category=category)
        context = {
            'categories': categories,
            'category': category,
            'products': products
        }
        return render(request, 'templates/shop/product/list.html', context)


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, available=True, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'templates/shop/product/details.html', context)