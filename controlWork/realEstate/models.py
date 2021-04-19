from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify
from unidecode import unidecode


class AdCategory(models.Model):
    name = models.CharField(max_length = 50)


    def __str__(self):
        return self.name


class RealEstate(models.Model):

    ESTATE_TYPES = [
        ('appartment', 'квартира'),
        ('house', 'частный дом'),
        ('industry', 'производственное помещение'),
        ('warehouse', 'складское помещение'),
    ]

    title = models.CharField(max_length = 100)
    text = models.TextField()
    phone_number = PhoneNumberField()
    owner_name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField(default=0)
    estate_type = models.CharField(max_length = 10, choices = ESTATE_TYPES, default='appartment')
    rating = models.PositiveIntegerField(default=0)
    address = models.TextField()
    number_of_rooms = models.PositiveSmallIntegerField(default=1)
    area = models.DecimalField(decimal_places=1, max_digits=4)
    furnuture = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    category = models.ForeignKey(AdCategory,  on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)