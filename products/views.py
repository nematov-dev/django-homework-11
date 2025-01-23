from django.shortcuts import render
from django.views.generic import ListView,DetailView


from products import models


class ProductListView(ListView):
    template_name = 'products/product.html'
    model = models.ProductModel
    context_object_name = 'products'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colors"] = self.make_color_groups()
        context["categories"] = models.ProductCategoryModel.objects.all()
        context["tags"] = models.ProductTagModel.objects.all()
        context["brands"] = models.ProductManufactureModel.objects.all()
        context["sizes"] = models.ProductSizeModel.objects.all()
        return context
    
    @staticmethod
    def make_color_groups():
        colors = models.ProductColorModel.objects.all()
        result = list()
        temp_list = list()
        for color in colors:
            temp_list.append(color)
            if len(temp_list) == 2:
                result.append(temp_list)
                temp_list = []

        if len(temp_list) >= 1:
            result.append(temp_list)

        return result

class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = models.ProductModel
    context_object_name = 'product'
