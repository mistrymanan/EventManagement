from django.test import TestCase
from .models import User
# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        User.objects.create(username="Manan",first_name="Manan",last_name="Mistry",email="mananmistry10@gmail.com")
    def test_user_str(self):
        user=User.objects.get(username="Manan")
        print(user.__str__())
        self.assertEqual(user.__str__(),'Manan [mananmistry10@gmail.com]')
