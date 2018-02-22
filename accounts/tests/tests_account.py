from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.hashers import make_password
from accounts import models as accounts_models


data = {
    "username": "solrac",
    "first_name": "carlos",
    "last_name": "olivero",
    "email": "carlosolivero2@gmail.com",
    "password": "1234qwer",
    "dni": "20379739",
    "direction": "18 de octubre",
    "phone": "+584146419077"
}


class LoginTestCase(APITestCase):

    def setUp(self):
        country = accounts_models.Country.objects.create(name="venezuela")
        self.c = APIClient()
        user = accounts_models.User.objects.create(
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            password=make_password(data.get('password')),
            dni=data.get('dni'),
            direction=data.get('direction'),
            phone=data.get('phone'),
            country_id=country.id,
        )
        self.user = user

    def test_login(self):
        #data = self.user
        #client.force_authenticate(user=userData)
        data = {"username": "solrac", "password": "1234qwer"}
        response = self.c.post('/v1/login/', data, format='json')
        self.assertEqual(response.status_code, 200, "fail login")
        self.assertEqual(response.data.get('username'), data.get('username'), "not equal")
        print(response.data)

    def test_login_email(self):
        #data = self.user
        #client.force_authenticate(user=userData)
        data = {"username": "carlosolivero2@gmail.com", "password": "1234qwer"}
        response = self.c.post('/v1/login/', data, format='json')
        self.assertEqual(response.status_code, 200, "fail login")
        #self.assertEqual(response.data.get('username'), data.get('username'), "not equal")
        print(response.data)


    def test_fail_username(self):
        #data = self.user
        #client.force_authenticate(user=userData)
        data = {"username": "carlos", "password": "1234qwer"}
        response = self.c.post('/v1/login/', data, format='json')
        self.assertEqual(response.status_code, 404, "no debe devolver 200")
        #self.assertEqual(response.data.get('username'), data.get('username'), "not equal")
        print(response.data)

    def test_fail_username_email(self):
        #data = self.user
        #client.force_authenticate(user=userData)
        data = {"username": "carlosoliveros@gmail.com", "password": "1234qwer"}
        response = self.c.post('/v1/login/', data, format='json')
        self.assertEqual(response.status_code, 404, "fail login")
        #self.assertEqual(response.data.get('username'), data.get('username'), "not equal")
        print(response.data)

    def test_fail_password(self):
        #data = self.user
        #client.force_authenticate(user=userData)
        data = {"username": "solrac", "password": "1234"}
        response = self.c.post('/v1/login/', data, format='json')
        self.assertEqual(response.status_code, 400, "no debe devolver 200")
        #self.assertEqual(response.data.get('username'), data.get('username'), "not equal")
        print(response.data)