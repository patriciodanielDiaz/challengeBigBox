# Create your models here.
from django.db import models


class Common(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField()

    class Meta:
        abstract = True


class CommonInfo(Common):
    order = models.IntegerField(default=0, verbose_name='orden')
    class Meta:
        abstract = True


class Reason(CommonInfo):
    pass

    class Meta:
        verbose_name_plural = "Reasons"
    def __str__(self):
        return self.name


class Category(CommonInfo):
    description = models.TextField(verbose_name=u'descripción')
    color = models.CharField(max_length=8, default='FFFFFF')

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Image(models.Model):
    order = models.IntegerField(default=0, verbose_name='orden')
    upload = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name='imagen')

    class Meta:
        abstract = True

class Prodcut(Common):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    description = models.TextField(verbose_name=u'descripción')
    category = models.ForeignKey(Category, verbose_name='categoría', on_delete=models.CASCADE, null=True, blank=True)
    purchase_available = models.BooleanField(verbose_name='disponible venta individual', default=True)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True


class Activity(Prodcut):
    reasons = models.ManyToManyField(Reason, verbose_name='tags', blank=True)

    class Meta:
        verbose_name_plural = "Activities"
    def __str__(self):
        return self.name

class Box(Prodcut):
    activities = models.ManyToManyField(Activity)
    participant_number = models.IntegerField(default=1, verbose_name='numere de participantes')
    price = models.DecimalField(verbose_name='precio de venta', decimal_places=2, max_digits=6)

    class Meta:
        verbose_name_plural = "Boxes"
    def __str__(self):
        return self.name

class ActivityImage(Image):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Activity Images"
    def __str__(self):
        return str(self.upload) +' | '+ str(self.activity)

class BoxImage(Image):
    box = models.ForeignKey(Box,related_name='boximage_set', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Box Images"
    def __str__(self):
        return str(self.upload) +' | '+ str(self.box)
