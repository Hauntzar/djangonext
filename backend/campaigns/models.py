from django.db import models
from django.db.models.fields import DateTimeField, TextField
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.
class Campaign(models.Model):

    title=models.CharField(max_length=200, null=False, blank=True)
    description=models.TextField(null=False, blank=True)
    slug=models.SlugField(max_length=255, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    logo=CloudinaryField('logo',overwrite=True,format="jpg")

    class Meta:
        ordering=('-created_at',)


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        to_assign=slugify(self.title)

        if Campaign.objects.filter(slug=to_assign).exists():
            to_assign=to_assign+str(Campaign.objects.filter(slug=to_assign).count())

        self.slug=to_assign

        super().save(*args,**kwargs)

class Subscriber(models.Model):

    campaign=models.ForeignKey(Campaign, on_delete=models.DO_NOTHING) # on_delete=models.DO_NOTHING
    email = models.EmailField(max_length=254)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email