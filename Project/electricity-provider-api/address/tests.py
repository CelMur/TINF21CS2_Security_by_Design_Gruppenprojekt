from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import serializers
from address.serializers import AddressSerializer
from address.models import Address
from django.contrib.auth import get_user_model



class AddressSerializerTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create(email='testuser@test.de', password='testpass121212')
        self.client.login(username='testuser@rest.dasd', password='123456789')

        factory = APIRequestFactory()
        self.request = factory.get('/')
        self.request.user = self.user


    def test_validate_street_number_empty__shoud_raise_ValidationError(self):
        serializer = AddressSerializer(data={'street_number': ''}, context={'request': self.request})
        self.assertRaises(serializers.ValidationError, serializer.is_valid, raise_exception=True)


    def test_validate_postal_code_empty__shoud_raise_ValidationError(self):
        serializer = AddressSerializer(data={'postal_code': ''}, context={'request': self.request})
        self.assertRaises(serializers.ValidationError, serializer.is_valid, raise_exception=True)

    def test_validate_city_empty__shoud_raise_ValidationError(self):
        serializer = AddressSerializer(data={'city': ''}, context={'request': self.request})
        self.assertRaises(serializers.ValidationError, serializer.is_valid, raise_exception=True)


    def test_create_existing_address(self):
        # First, create an address
        serializer = AddressSerializer(data={'street':'Magic City','street_number': '123', 'postal_code': '456', 'city': 'Test City'}, context={'request': self.request})
        self.assertTrue(serializer.is_valid())
        address:Address = serializer.save()

        # Then, try to create the same address again
        serializer2 = AddressSerializer(data={'street':'Magic City', 'street_number': '123', 'postal_code': '456', 'city': 'Test City'}, context={'request': self.request})
        self.assertTrue(serializer2.is_valid())
        address2:Address = serializer2.save()

        # Depending on your application's behavior, you might want to assert that an error was raised,
        # or that the second address was created successfully.
        # For example, if addresses must be unique, you could do:
        # self.assertRaises(ValidationError, serializer2.is_valid, raise_exception=True)
        # Or if addresses can be duplicated, you could do:
        self.assertIsNotNone(address)
        self.assertIsNotNone(address2)
        self.assertEqual(address2.id, address.id)
        