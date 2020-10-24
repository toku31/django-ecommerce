from django.db import models
from django.contrib.auth.models import User

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

  def _str_(self):
    return self.title


class OrderItem(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  ordered = models.BooleanField(default=False)
  quantity = models.IntegerField(default=1)

  def _str_(self):
    return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  items = models.ManyToManyField(OrderItem)
  ordered = models.BooleanField(default=False)
  start_date = models.DateField(auto_now_add=True)
  ordered_date = models.DateField()

  def _str_(self):
    return self.user.username
