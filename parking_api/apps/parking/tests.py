from rest_framework import status
from rest_framework.test import APITestCase


class ParkingTestCase(APITestCase):
    def test_parking_history(self):
        response = self.client.get("/parking/ABC-1234")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_parking_with_wrong_plate(self):
        data = {"plate": "A1C-1234"}
        response = self.client.post("/parking", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_parking(self):
        data = {"plate": "ABC-1234"}
        response = self.client.post("/parking", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_parking_out_with_payment(self):
        data = {"plate": "ABC-1234"}
        self.client.post("/parking", data)

        response = self.client.get("/parking/2/pay")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get("/parking/2/out")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_parking_out_without_payment(self):
        data = {"plate": "ABC-1234"}
        self.client.post("/parking", data)

        response = self.client.get("/parking/3/out")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_payment(self):
        data = {"plate": "ABC-1234"}
        self.client.post("/parking", data)

        response = self.client.get("/parking/4/pay")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
