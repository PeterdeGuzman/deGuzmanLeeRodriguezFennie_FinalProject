from locust import HttpUser, task, between


class PerformanceTest(HttpUser):
    # Define the endpoint to be tested
    host = "https://vgp7iv9bmm.us-east-1.awsapprunner.com"

    # Simulate wait time between user actions
    wait_time = between(1, 5)

    @task
    def test_endpoint(self):
        self.client.get("/")  # Sends a GET request to the root endpoint


# Run for 100 requests/second
# locust -f locustfile.py --headless -u 100 -r 100 --run-time 1m --csv=locust_results_100

# Run for 500 requests/second
# locust -f locustfile.py --headless -u 500 -r 500 --run-time 1m --csv=locust_results_500

# Run for 1000 requests/second
# locust -f locustfile.py --headless -u 1000 -r 1000 --run-time 1m --csv=locust_results_1000

