from django.shortcuts import render, redirect
from django.views import View
from .models import (Product,
                     Images,
                     Categories,
                     ShoppingCart,
                     ShoppingHistory,
                     DeliveryAddresOfUser,
                     UserBlogComments,
                     BlogPhotos)
from django.db.models import Q
from django.contrib import messages
from django.http.response import JsonResponse
import json
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):

        products = Product.objects.order_by('id').all()[0:4]
        products_data = []

        for product in products:
            image = Images.objects.filter(product=product).first()  # select * from image where product id = product_id
            product.image = image
            products_data.append(image)

        products2 = Product.objects.order_by('id').all()[4:9]
        products_data2 = []
        for product in products2:
            image = Images.objects.filter(product=product).first()  # select * from image where product id = product_id
            product.image = image
            products_data2.append(image)

        products_data3 = []
        products3 = Product.objects.order_by('id').all()[9:12]
        for product in products3:
            image = Images.objects.filter(product=product).first()  # select * from image where product id = product_id
            product.image = image
            products_data3.append(image)
        self.context = ({'products': products,
                                'products2': products2,
                                'products3': products3})


        return render(request, self.template_name, self.context)

    def post(self, request):
        product_id = request.POST.get('product_id')
        if request.user is None:
            return redirect('/accounts/login')
        user =request.user
        if not ShoppingCart.objects.filter(Q(user=user) & Q(product_id=product_id)).exists():
            shopping_cart = ShoppingCart.objects.create(
                user=user,
                product_id=product_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added to cart')
            return redirect(f'/#product_{product_id}')

        messages.error(request, 'This product already exists in cart! ')
        return redirect(f'/#product_{product_id}')


class CategoryView(View):
    template_name = "category.html"
    context = {}

    def get(self, request):
        products4 = Product.objects.order_by('id').all()[12:21]
        product_data4 = []
        for product in products4:
            image = Images.objects.filter(product=product).first()
            category = Categories.objects.filter(product=product).first()
            product.image = image
            product.category = category
            data = {
                'product.image':image,
                'product.category': category
            }
            product_data4.append(data)

        products5 = Product.objects.order_by('id').all()[21:29]
        product_data5 = []
        for product in products5:
            image = Images.objects.filter(product=product).first()
            product.image = image
            product_data5.append(image)
        self.context = {'products4': products4,
                        'products5': products5
                        }
        return render(request, self.template_name, self.context)


    def post(self, request):
        product_id = request.POST.get('product_id')
        if request.user is None:
            return redirect('/accounts/login')
        user =request.user
        if not ShoppingCart.objects.filter(Q(user=user) & Q(product_id=product_id)).exists():
            shopping_cart = ShoppingCart.objects.create(
                user=user,
                product_id=product_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added to cart')
            return redirect('/category')

        messages.error(request, 'This product already exists in cart! ')
        return redirect(f'/category#product_{product_id}')


class ProductDetailView(View):
    template_name = "single-product.html"
    context ={}
    def get(self, request):

        products5 = Product.objects.all()[21:29]
        product_data5 = []

        for product in products5:
            image = Images.objects.filter(product=product).first()
            product.image = image
            product_data5.append(image)


        products6 = Product.objects.all()[30:31]
        product_data6 = []

        for product in products6:
            image = Images.objects.filter(product=product).first()
            category = Categories.objects.filter(product=product).first()
            product.image = image
            product.category = category
            data = {
                'product.image': image,
                'product.category': category
            }
            product_data6.append(data)
            self.context = {'products5': products5,
                            'products6': products6
                            }

        return render(request, self.template_name, self.context)

    def post(self, request):
        product_id = request.POST.get('product_id')
        if request.user is None:
            return redirect('/accounts/login')
        user = request.user
        if not ShoppingCart.objects.filter(Q(user=user) & Q(product_id=product_id)).exists():
            shopping_cart = ShoppingCart.objects.create(
                user=user,
                product_id=product_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added to cart')
            return redirect('/single-product')

        messages.error(request, 'This product already exists in cart! ')
        return redirect('/single-product')




class CheckoutView(View):
    template_name = 'checkout.html'
    context = {}

    def get(self, request):
        shoping_cart_products = ShoppingCart.objects.all()
        shoping_cart_products_data = []
        for product in shoping_cart_products:
            name = product.product.name
            count = product.count
            price = product.product.price
            summa = (float(price) * count)
            summa = round(summa,2)
            shipping = 50
            total=summa+shipping
            data = {
                'name': name,
                'count':count,
                'price':price,
                'total':total,
                'summa':summa,
                'shipping':shipping
            }

            shoping_cart_products_data.append(data)
        self.context.update({'shoping_cart_products_data': shoping_cart_products_data})
        return render(request, self.template_name, self.context)


def confirmation(request):
    return render(request, 'confirmation.html')


class ShoppingCartView(View):
    temlate_name = 'cart.html'
    context = {}
    def get(self, request):
        if request.user.id is None:
            return redirect ('/accounts/login')
        shopping_cart = ShoppingCart.objects.filter(user = request.user)
        data = []
        summa = 0
        for index, value in enumerate(shopping_cart):
            image = Images.objects.filter(product = value.product).first()
            value.img = image
            value.index = index+1
            summa += float(value.product.price * value.count)
            summa = round(summa, 2)
            total = summa + 50
            data.append(value)
        self.context.update({'shopping_cart_products':data})
        self.context.update({'summa': summa})
        return render(request,self.temlate_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        ShoppingCart.objects.get(pk = shopping_cart_id).delete()
        return redirect('/cart')



class BlogView(View):
    template_name = "blog.html"
    context = {}
    def get(self, request):
        comments = UserBlogComments.objects.all()
        comment_data1 = []
        for comment in comments:
            image = BlogPhotos.objects.filter(author=comment).first()
            comment.image = image
            comment_data1.append(comment)
        self.context.update({'comment_data1': comment_data1})

        return render(request, self.template_name, self.context)


def single_blog(request):
    return render(request, 'single-blog.html')







def contact(request):
    return render(request, 'contact.html')


class ShoppingHistoryView(View):
    template_name = "history.html"
    context = {}
    def get(self, request):
        products = ShoppingHistory.objects.select_related('product').order_by('upload_at').filter(user=request.user)
        service_data = []
        summa=0
        for product in products:
            image = Images.objects.filter(product=product.product).first()
            product.image = image
            summa += float(product.count * product.product.price)
            summa = round(summa,2)

            service_data.append(product)
        self.context.update({'products_history': service_data,
                             'summa':summa})
        return render(request, self.template_name, self.context)



    def post(self, request):
        data = request.data['']
        products = ShoppingCart.objects.select_related('product').filter(user=request.user)

        for product in products:
            order = ShoppingHistory.objects.create(
                product=product.product,
                user=request.user,
                status=1,
                count=product.count

            )
            order.save()
            ShoppingCart.objects.get(pk=product.id).delete()
        return redirect('/confirmation')

class IncrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            shopping_cart.count += 1
            shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class DecrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if shopping_cart.count > 0:
                shopping_cart.count -= 1
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class ChangeCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            product_count = json_data.get('product_count')

            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if product_count is not None:
                shopping_cart.count = product_count
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class AddPhotosView(View):
    template_name="addproduct.html"
    context = {}
    def get(self, request):
        comments = UserBlogComments.objects.all()
        comment_data=[]
        for comment in comments:
            image = BlogPhotos.objects.filter(author=comment).first()
            comment.image = image
            comment_data.append(image)
        self.context.update({'comment_data':comment_data})

        return render(request, self.template_name, self.context)


    def post(self, request):
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        images = request.FILES.getlist('images')

        service = UserBlogComments.objects.create(
            title=title,
            comment=comment,
            author = request.user
        )
        service.save()
        for image in images:
            img = BlogPhotos.objects.create(
                photo=image,
                author=service
            )
            img.save()
        return redirect('/blog')




class UserAddresView(View):
    template_name = 'checkout.html'
    context = {}
    def get(self, request):
        return render(request, self.template_name, self.context)
    def post(self, request):

        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        CompanyName =request.POST.get('companyname')
        PhoneNumber =request.POST.get('phonenumber')
        EmailAddres =request.POST.get('emailaddress')
        Country = request.POST.get('country')
        AddressLine1 =request.POST.get('addresline1')
        AddressLine2 =request.POST.get('addressline2')
        City =request.POST.get('city')
        District =request.POST.get('district')
        Postcode =request.POST.get('postcode')
        ShippingDetails=request.POST.get('details')

        user = DeliveryAddresOfUser.objects.create(
            name=name,
            lastname=lastname,
            CompanyName=CompanyName,
            PhoneNumber=PhoneNumber,
            EmailAddres=EmailAddres,
            Country=Country,
            AddressLine1=AddressLine1,
            AddressLine2=AddressLine2,
            City=City,
            District=District,
            Postcode=Postcode,
            ShippingDetails=ShippingDetails

        )
        user.save()
        return redirect('/confirmation')