from django.db import models
from utils.genslug import gen_slug
from django.urls import reverse
from brand.models import *

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    cat_slug = models.SlugField(blank=True)
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_subcategories", kwargs={"cat_slug":self.cat_slug})

    def save(self, *args, **kwargs):
        if not self.cat_slug:
            self.cat_slug = gen_slug(self.name)
        super().save(*args, **kwargs)

<<<<<<< HEAD
    def products_in_category(slug):
        category = Category.objects.get(slug=slug)
        return category.product_set.all()

class SubCategory(models.Model):
    sub_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='q')
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
=======
    # def products_in_category(slug):
    #     category = Category.objects.get(slug=slug)
    #     return category.product_set.all()

    def subcategories_in_category(cat_slug):
        category = Category.objects.get(cat_slug=cat_slug)
        return category.subcategory_set.all()
    

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    subcat_slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    brands = models.ManyToManyField(Brand,related_name='subcategory_brands')
>>>>>>> c440e2c153e5286d497f9eb4be5b48029f9a9fba

    def __str__(self):
        return self.name

<<<<<<< HEAD
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)
=======
    def get_absolute_url(self):
        return reverse("subcategory_brands", kwargs={"cat_slug":self.category.cat_slug,"subcat_slug": self.subcat_slug})

    def save(self, *args, **kwargs):
        if not self.subcat_slug:
            self.subcat_slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    # def products_in_subcategory(slug):
    #     subcategory = SubCategory.objects.get(slug=slug)
    #     return subcategory.product_set.all()

    def brands_in_subcategory(subcat_slug):
        subcategory = SubCategory.objects.get(subcat_slug=subcat_slug)
        return subcategory.brands.all()
>>>>>>> c440e2c153e5286d497f9eb4be5b48029f9a9fba
