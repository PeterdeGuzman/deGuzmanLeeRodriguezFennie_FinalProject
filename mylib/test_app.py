import unittest
import requests
import subprocess
import time


class Test_Flask(unittest.TestCase):
    base_url = "http://127.0.0.1:5000"

    @classmethod
    def setUpClass(cls):
        # open a subprocess for the Flask app
        cls.flask_process = subprocess.Popen(
            ["python", "workspace/app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(5)  # wait for server to start

    @classmethod
    def tearDownClass(cls):
        # Use terminate on the subprocess for the Flask app
        cls.flask_process.terminate()
        cls.flask_process.wait()

    def test_flask_homepage(self):
        """Test the home page of the app."""
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200, "Home page should return HTTP 200")
        self.assertIn(
            "text/html", response.headers["Content-Type"], "Response should be HTML"
        )


if __name__ == "__main__":
    unittest.main()
