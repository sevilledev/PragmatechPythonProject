from django.db import models
from backend.models import User
from product.models import Product

# Create your models here.

class CartMeneger(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id) # self yerine super() yaza bilerdikmi?
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_id.id
        return cart_obj , new_obj
# burda hardan yoxlaya bilir ki, basqa hansisa cart item-larin birinde produclarinda burda
# secilen productlar eynidi ya ferqlidi?

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField(Product,related_name='cart_products')
    subtotal = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    object = CartMeneger()

    def __str__(self):
        return str(self.id)

