from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model


class TestUser(TestCase):

    def setUp(self):
        self.User = get_user_model()
        User = self.User
        self.user1 = User.objects.create_user(username='user1', password='password', phone_number='1234567890',
                                              address='1234 Main St')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_user_info(self):
        User = self.User
        user1 = self.user1
        user2 = self.user2
        self.assertEqual(user1.phone_number, '1234567890')
        self.assertEqual(user1.address, '1234 Main St')

    def test_user_object(self):
        User = self.User
        user1 = self.user1
        user2 = self.user2
        self.assertEqual(user1.username, 'user1')
        self.assertEqual(user2.username, 'user2')
        self.assertTrue(user1.check_password('password'))
        self.assertFalse(user2.check_password('wrongpassword'))
        self.assertTrue(user1.is_authenticated)
        self.assertTrue(user1.is_active)
        self.assertFalse(user1.is_staff)
        self.assertFalse(user1.is_superuser)
        self.assertEqual(user1.__str__(), 'user1')
        self.assertEqual(user2.__str__(), 'user2')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.filter(username='user1').count(), 1)
        self.assertEqual(User.objects.filter(username='user1', phone_number='1234567890').count(), 1)
        self.assertEqual(User.objects.filter(username='user1', phone_number='1234567891').count(), 0)
        self.assertEqual(User.objects.filter(username='user1', address='1234 Main St').count(), 1)
        self.assertEqual(User.objects.filter(username='user1', address='1234 Main St 2').count(), 0)
        self.assertEqual(User.objects.filter(username='user2', phone_number='1234567890').count(), 0)
        self.assertEqual(User.objects.filter(username='user2', address='1234 Main St').count(), 0)


    def test_update_user(self):
        User = self.User
        user1 = self.user1
        user1.phone_number = '1234567891'
        user1.save()

        user1 = User.objects.get(username='user1')
        self.assertEqual(user1.phone_number, '1234567891')


