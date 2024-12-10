from locust import HttpUser, task, between


class PerformanceTest(HttpUser):
    # Define the endpoint to be tested
    host = "https://vgp7iv9bmm.us-east-1.awsapprunner.com"

    # Simulate wait time between user actions
    wait_time = between(1, 5)

    @task
    def test_endpoint(self):
        self.client.get("/")  # Sends a GET request to the root endpoint


# Run for 500 requests/second
# [bash] locust -f locustfile.py --headless -u 500 -r 500 --run-time 1m
