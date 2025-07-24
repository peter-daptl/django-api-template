from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.models.car import Car

class CarAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

        # Create a token for the user
        from rest_framework.authtoken.models import Token
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.car1 = Car.objects.create(make='Toyota', model='Camry', year=2020)
        self.car2 = Car.objects.create(make='Honda', model='Civic', year=2022)
        self.list_url = reverse('car-list')
        self.detail_url = reverse('car-detail', kwargs={'pk': self.car1.pk})

    def test_list_cars(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['make'], 'Toyota')

    def test_create_car(self):
        data = {'make': 'Ford', 'model': 'Focus', 'year': 2018}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 3)
        self.assertEqual(Car.objects.get(id=response.data['id']).make, 'Ford')

    def test_retrieve_car(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['make'], 'Toyota')

    def test_update_car(self):
        data = {'make': 'Toyota', 'model': 'Corolla', 'year': 2021}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.car1.refresh_from_db()
        self.assertEqual(self.car1.model, 'Corolla')

    def test_partial_update_car(self):
        data = {'year': 2023}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.car1.refresh_from_db()
        self.assertEqual(self.car1.year, 2023)

    def test_delete_car(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 1)
        self.assertFalse(Car.objects.filter(pk=self.car1.pk).exists())

    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None) # Remove authentication
        response = self.client.get(self.list_url)
        # Should be 403 Forbidden for writing/deleting, but 200 OK for read-only
        # as per IsAuthenticatedOrReadOnly.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(self.list_url, {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
