from rest_framework.test import APITestCase
from authentication.models import *

class TestModel(APITestCase):    
    def test_creates_user(self):
        user = User.objects.create_user('david', 'innocentcyusa2@gmail.com', 'mazimpaka123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'innocentcyusa2@gmail.com')