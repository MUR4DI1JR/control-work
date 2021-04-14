from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify

class RealEstate(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    phone_number = PhoneNumberField()
    owner_name = models.CharField(max_length = 100)
    rating = models.PositiveIntegerField(default=0)
    address = models.TextField()
    number_of_rooms = models.PositiveSmallIntegerField(default=1)
    area = models.DecimalField(decimal_places=1, max_digits=4)
    furnuture = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)