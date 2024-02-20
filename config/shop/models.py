from django.db import models
from PIL import Image


class Client(models.Model):
    """Stores client ifno"""

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    country = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    zip_code = models.SmallIntegerField()

    def __str__(self):
        return f"<client({self.user=})>"


class Categorie(models.Model):
    """Stores `Star` categories"""

    name = models.CharField(max_length=155)

    def __str__(self):
        return f"<categorie ({self.name=})>"


class Star(models.Model):
    """Stores product(stars) info"""

    name = models.CharField(max_length=155)
    slug = models.SlugField(unique_for_date="created_at", max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=None, null=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)

    class Meta:
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 300:
            img.thumbnail((400, 300))
            img.save(self.image.path)

    def get_absolute_url(self):
        return f'/{self.created_at.strftime("%Y/%m/%d")}/{self.slug}/'

    def __str__(self):
        return f"<star ({self.name=}, {self.categorie=}, {self.price=})>"


class Review(models.Model):
    """Stores product(stars) reviews"""

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"<comment ({self.text=}, {self.client=})>"
