from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

CATEGORY_CHOICES = {
    ('S', 'Shirt'),
    ('SW', 'SportWear'),
    ('OW', 'Outwear')
}

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
  title = models.CharField(max_length=200)
  price = models.IntegerField()
  discount_price = models.IntegerField(blank=True, null=True)
  slug = models.SlugField()
  status = models.CharField(max_length=200)
  category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
  label = models.CharField(choices=LABEL_CHOICES, max_length=2)
  description = models.TextField()
  image = models.ImageField(default='default.jpg', upload_to='static/images')

  def __str__(self):
    return self.title

  def get_add_to_cart_url(self):
    return reverse('add_to_cart', kwargs={'slug':self.slug})

  def get_remove_from_cart_url(self):
    return reverse('remove_from_cart', kwargs={'slug':self.slug})

class OrderItem(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  ordered = models.BooleanField(default=False)
  quantity = models.IntegerField(default=1)

  def __str__(self):
    return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  items = models.ManyToManyField(OrderItem)
  ordered = models.BooleanField(default=False)
  start_date = models.DateField(auto_now_add=True)
  ordered_date = models.DateField()

  def __str__(self):
    return self.user.username
