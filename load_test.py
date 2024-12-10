from locust import HttpUser, task, between

class FlaskAppLoadTest(HttpUser):
    # Simulate user wait time between tasks (1 to 3 seconds)
    wait_time = between(1, 3)

    @task
    def home_page(self):
        # Test the homepage
        self.client.get("/")

    @task
    def project_page(self):
        # Test the project page
        self.client.get("/project")

    @task
    def submit_query(self):
        # Test the submit route with a POST request
        self.client.post(
            "/submit",
            data={"userInput": "Ernest Hemingway", "options": "Author"}
        )
