from django.db import models
from address.models import Address
from billing.models import BillingProfile
from backend.models import User
from cart.models import Cart

# Create your models here.

ORDER_STATUS_CHOICES=(
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)

class OrderQuerySet(models.query.QuerySet):
    def created_orders(self):
        return self.filter(status='created')

    def paid_orders(self):
        return self.filter(status='paid')

    def shipped_orders(self):
        return self.filter(status='shipped')

    def refunded_orders(self):
        return self.filter(status='refunded')

class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)


class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE,related_name='billing_profile',blank=True,null=True)
    order_id = models.CharField(max_length=100,blank=True)
    shipping_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='shipping_address',blank=True,null=True)
    billing_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='billing_address',blank=True,null=True)
    shipping_address_final = models.TextField(blank=True,null=True)
    billing_address_final = models.TextField(blank=True,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,default='created',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=1.00,max_digits=60,decimal_places=2)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = OrderManager()



