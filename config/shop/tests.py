from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time

from shop.models import Categorie, Star


@freeze_time("2024-02-20")
class ShopTestCase(TestCase):
    """Testing `shop` app"""

    def setUp(self):
        self.categorie = Categorie.objects.create(name="Test Categorie")
        self.img = "/home/darwin/code/star_shop/config/assets/images/1.jpeg"
        self.star1 = Star.objects.create(
            name="Sun",
            slug="sun",
            description="The only star in the solar system",
            image=self.img,
            price="1000.25",
            discount=None,
            created_at="2024-02-20",
            updated_at="2024-02-20",
            is_active=True,
            categorie=self.categorie,
        )
        self.star2 = Star.objects.create(
            name="Moon",
            slug="moon",
            description="Earth's only natural satellite.",
            image=self.img,
            price="500.75",
            discount=None,
            created_at="2024-02-20",
            updated_at="2024-02-20",
            is_active=True,
            categorie=self.categorie,
        )

    def test_get_all_star(self):
        url = reverse("shop:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_one_star(self):
        url = reverse("shop:detail", args=["2024", "02", "20", "sun"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
