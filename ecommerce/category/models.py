from django.db import models
from utils.genslug import gen_slug
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def category_in_products(slug):
        category = Category.objects.get(slug=slug)
        return category.product_set.all()
    