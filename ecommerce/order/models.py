from django.db import models
from address.models import Address
from billing.models import BillingProfile
from backend.models import User
from cart.models import Cart
from datetime import datetime, timedelta
from django.utils import timezone
# Create your models here.

ORDER_STATUS_CHOICES=(
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)

class OrderQuerySet(models.QuerySet):

    def by_status(self,status='created'):
        return self.filter(status=status)


    def by_range(self, start_date, end_date=None):
        if end_date is None:
            return self.filter(update__gte=start_date)
        return self.filter(update__gte=start_date).filter(update__lte=end_date)


    def by_weeks_range(self,weeks_ago=2,number_of_weeks=3):
        if number_of_weeks > weeks_ago:
            number_of_weeks = weeks_ago
        day_ago_start = weeks_ago * 7
        print(day_ago_start)
        day_ago_end = day_ago_start - (number_of_weeks * 7)
        print(day_ago_end)
        start_date = timezone.now() - timedelta(days=day_ago_start)
        print(timedelta(days=day_ago_start))
        end_date = timezone.now() - timedelta(days=day_ago_end)
        print(end_date)
        print(start_date)
        return self.by_range(start_date,end_date=end_date)



    # def created_orders(self):
    #     return self.filter(status='created')
    #
    # def paid_orders(self):
    #     return self.filter(status='paid')
    #
    # def shipped_orders(self):
    #     return self.filter(status='shipped')
    #
    # def refunded_orders(self):
    #     return self.filter(status='refunded')
    #
    # def filter_for_days_orders(self, days):
    #     delta = timedelta(days=days)
    #     last_date = datetime.now() - delta
    #     return self.filter(timestamp__gte=last_date)

class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)
    def by_weeks_range(self):
        return self.get_queryset().by_weeks_range()
    def by_status(self,status='created'):
        return self.get_queryset().by_status(status=status)

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



