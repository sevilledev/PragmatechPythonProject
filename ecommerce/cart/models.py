from django.db import models
from product.models import Product
from backend.models import User
from django.db.models.signals import m2m_changed,post_save,pre_save
from django.dispatch import receiver
from django.conf import settings
from decimal import Decimal

# Cart modeli ucun custom queryset yazmisig, ve Cart modelin manageridi
class CartMeneger(models.Manager):
    # new_or_get funkciyasi django orm deki get_or_create custom versiyasidi
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None) # sessiyadan gotururuk
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_id.id # sessiyaya elave edirik
        return cart_obj , new_obj
    # new -funkciyasi cart modelindeki user field create edir
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated(): # login olmush user demekdir
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product = models.ManyToManyField(Product, related_name='cart_product')
    subtotal = models.DecimalField(max_digits=100,decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    object = CartMeneger() # Cart modele menegeri tanidirig


    def __str__(self):
        return str(self.id)



@receiver(m2m_changed, sender=Cart.product.through)
def m2m_changed_cart_reciver(sender,instance,action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        product = instance.product.all()
        total = 0
        for x in product:
            total += x.product_price
        if instance.subtotal != total:
            instance.subtotal = total
            # run functions pre_save_cart_receiver
            instance.save()
        
    
@receiver(pre_save,sender=Cart)
def pre_save_cart_receiver(sender,instance,*args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(settings.SUB_TOTAL_PERCENTAGE)
    else:
        instance.total = 0.00






