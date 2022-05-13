import unittest
import requests

class ApiTest(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/"
    BUY_URL = f"{BASE_URL}/buy"

    def test_1_get_all_products(self):
        response = requests.get(ApiTest.BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_2_buy_product(self):
        id = 3
        data = {"buy_amount": 5}
        response = requests.patch(ApiTest.BUY_URL + f"/{id}", json=data)
        response_status = list(response.json().keys())[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_status, "success")

if __name__ == "__main__":
    unittest.main()