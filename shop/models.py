from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db import models
import uuid

from taggit.managers import TaggableManager


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title
    

class Image(models.Model):
    img_slug = AutoSlugField(populate_from='Product.name',unique=True)
    image = models.ImageField(upload_to='products/',null=True,blank=True,)
    def __str__(self):
        return self.image


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################


STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('published', 'Published'),
)
offer = (
    ('today_deal', "today's Deal"),
    ('savings', 'Great Saving'),
    ('by1get1', 'Bye 1 Get 1'),
    ('by2get1', 'Buy 2 Get 1'),
)
TYPE = (
    ('physical', 'Physical'),
    ('digital', 'Digital'),
)

Tax_Type = (
    ('flat', 'Flat'),
    ('percent', 'Percent'),
)

Discount_Type = (
    ('flat', 'Flat'),
    ('percent', 'Percent'),
)

Unit = (
    ('kg', 'kg'),
    ('gm', 'gm'),
    ('liter', 'liter'),
    ('ml','ml'),
    ('pkt', 'pkt'),
    ('bunch', 'bunch'),
    ('dozen', 'dozen'),
    ('box', 'box'),
    ('piece', 'piece'),
    ('inch','Inches'),
    ('cm','cm'),
    ('meter','meter'),
    ('km','km'),
)
STATUS_CHOICE = (
    ('pending', 'pending'),
    ('in_review', 'In Review'),
    ('confirmed', 'Confirmed'),
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)

Offer = (
    ('today_deal', "Today's Deal"),
    ('Savings', 'Great Saving'),
    ('buy1get1', 'Buy 1 Get 1')
)


class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="brand/", blank=True, null=True)

    def brand_image(self):
        return mark_safe('<img src="%s" width="100" height="50">' % self.image.url)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', null=True, blank=True, default=None,unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, related_name='brand')
    vendor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vd')

    unit = models.CharField(choices=Unit, max_length=100, blank=True,default='kg')
    min_qty = models.PositiveIntegerField(default=1,null=True, blank = True)
    # tags = TaggableManager(blank=True)

    type = models.CharField(choices=TYPE, max_length=10, default='physical', null=True, blank=True)
    barcode = models.CharField(max_length=30, blank=True, null=True, default=None)

    image = models.ImageField(upload_to='products/', null=True, blank=True,default='defaults/default.jpg')
    image1 = models.ImageField(upload_to='products1/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products2/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products3/', null=True, blank=True)
    hover_image = models.ImageField(upload_to='products_hover_image/', null=True, blank=True)

    price = models.PositiveIntegerField(null=True, blank = True)
    old_price = models.PositiveIntegerField(null=True, blank = True)

    pack_size = models.DecimalField(decimal_places=2,max_digits=5, null=True)
    discount = models.CharField(choices=Discount_Type, max_length=10, blank=True, null=True)

    tax = models.IntegerField(blank=True, null=True, default=5)
    tax_type = models.CharField(choices=Tax_Type, max_length=10, default='percent')
    description = models.TextField(null=True, blank=True)

    qty = models.PositiveIntegerField(null=True, blank = True)
    sku = models.CharField(max_length=30, null=True, blank=True, default=None)
    offer = models.CharField(choices=Offer, max_length=10, default=None, null=True, blank=True)
    featured = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default='in_review', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def tax_amount(self):
        tax_price = self.price
        if self.tax_type == 'percent' and self.tax >= 0:
            tax_price = self.price * self.tax /100
        return tax_price
    
    def discount_percent(self):
        discount = 0
        if self.old_price:
            flat = self.old_price - self.price
            discount = flat / self.price *100
            discount = round(discount, 2)
        return discount
    
    def tax_price(self):
        if self.tax >=0 and Tax_Type == 'percent':
            tax_price = self.price * self.tax /100
        return tax_price
    def CatLen(self):
        Catlen=0
        for i in self.category.title:
            Catlen +=1
        return Catlen

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return self.user.username
    def sub_total(self):
        subtotal = 0
        for i in self.product:
            subtotal += i.price * self.quantity
        return subtotal
    def cart_len(self,user):
        cart_lenth=0
        if self.user==user:
            for cart in self.product:
                cart_lenth +=1
        cart_lenth= self.product
        return cart_lenth
    



