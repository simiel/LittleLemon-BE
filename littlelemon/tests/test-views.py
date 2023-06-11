from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup():
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="banana", price=78, inventory=101)
        
    def test_getall():
        item1 = Menu.objects.get(inventory=100)
        item2 = Menu.objects.get(inventory=101)
        self.assertEqual(item1, "IceCream: 80")
        self.assertEqual(item2, "banana: 78")
        
        

    