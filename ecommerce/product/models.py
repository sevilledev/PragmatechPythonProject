from django.db import models
from time import time
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from django.urls import reverse
from category.models import Category
from utils.genslug import gen_slug

# def gen_slug(s):
#     new_slug = slugify(s,allow_unicode=True)
#     return new_slug + '-' + str(int(time()))

class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True)
    product_name = models.CharField(max_length=50,blank=True,null=True)
    product_descrption = models.TextField(blank=True,null=True)
    product_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    product_discount = models.DecimalField(max_digits=9,decimal_places=1,blank=True,null=True)
    product_discount_price =  models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    product_image = models.ImageField(blank=True,null=True)
    product_stock = models.BooleanField(default=True)
    product_title = models.TextField(blank=True,null=True)
    product_vip = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.product_name
# save - new_slug generete & product_discount 0 olmadigi halda endirim qiymetini hesablayir
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.product_name)
        if self.product_discount >= 1:
            change = float(self.product_price) * float(self.product_discount) / 100
            self.product_discount_price = float(self.product_price) - change
        super().save(*args, **kwargs)
# productun bunun multiple filelarini yuklemek ucundu (self-sozu genen productdan )

    def get_downloads(self):
        qs = self.productfile_set.all()
        
        return qs

    @property
    def get_downloads2(self):
        qs = self.productfile_set.all()
        
        return qs

# productun ozune mexsus fillerini duzgun diretoriya yaratmagi ucundur
def upload_product_file_loc(instance,filename):
    slug = instance.product.slug
    id_  = instance.id
    if id_ is None:
        Klass = instance.__class__
        qs = Klass.objects.all().order_by('-pk')
        if qs.exists():
            id_ = qs.first().id + 1
        else:
            id_ = 0
    if not slug:
        slug = gen_slug(instance.product)
    location = "product/{slug}/{id}/".format(slug=slug, id=id_)
    return location + filename
    




class ProductFile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to=upload_product_file_loc,
        storage=FileSystemStorage(location=settings.PRODUCT_STOREGE)
    )#upload_to parametrine - upload_product_file_loc funkciyamizi veririk ve storage ise directoriyanin yerini gosterir.


