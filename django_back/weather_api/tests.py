from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Location


class CreateLocationTest(APITestCase):

    def setUp(self):
        self.url = reverse('create_location')
        self.data = {'name': 'Algiers'}

    def test_create_location(self):
        # Send a POST request to create a new location
        response = self.client.post(self.url, self.data, format='json')

        # Check that the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the response data contains the location data
        self.assertEqual(response.data['name'], self.data['name'])

        # Check that the location was actually created in the database
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(Location.objects.get().name, self.data['name'])

    def test_create_location_invalid(self):
        # Send a POST request with invalid data
        response = self.client.post(self.url, {}, format='json')

        # Check that the response status code is 400 BAD REQUEST
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that no location was created
        self.assertEqual(Location.objects.count(), 0)