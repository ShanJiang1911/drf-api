from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Animal

class AnimalTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_animal = Animal.objects.create(
            keeper = testuser1,
            name = "Hippo",
            food = "I like chewing watermelon",
        )
        test_animal.save()

    def test_food(self):
        animal = Animal.objects.get(id=1)
        actual_keeper = str(animal.keeper)
        actual_name = str(animal.name)
        actual_food = str(animal.food)
        self.assertEqual(actual_keeper, 'testuser1')
        self.assertEqual(actual_name, 'Hippo')
        self.assertEqual(actual_food, 'I like chewing watermelon')

