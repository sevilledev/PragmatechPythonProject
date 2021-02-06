from django.db import models
from backend.models import User
from cart.models import Cart

# Create your models here.

ORDER_STATUS_CHOICES = [
    ['paid', 'Paid'],
    ['shipped', 'Shipped'],
    ['refunded', 'Refunded'],
]

class OrderManager(models.Manager):
    def new_order(self, request):
        order_obj = Order.objects.new(user=request.user)
        request.session['order_id'] = order_id.id
        return order_obj

    def filter_for_status(self, status):
        for i in ORDER_STATUS_CHOICES:
            if i == status:
                return self.get_queryset().filter(status=i)



def filter_for_time(self, user, start, end, *args, *kwargs):
    selected_orders = Cart.objects.filter_by(user=user)
    selected_orders.filter(timestamp__gte=start, timestamp__lte=end)

class Order(models.Model):
    ordered_user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    ordered_cart = models.ForeignKey(Cart, on_delete=models.CASCADE,blank=True,null=True)

    object = OrderManager()

    def __str__(self):
        return str(self.id)

