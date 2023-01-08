from random import choice, randint
from locust import HttpUser, task, between


class BasicUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def show_summary(self):
        self.client.get("/showSummary")

    @task
    def display_board(self):
        self.client.get("/displayBoard")

    @task
    def booking(self):
        self.client.get(f"/book/{choice(['Spring Festival', 'Fall Classic'])}")

    @task
    def purchase_places(self):
        self.client.post(
            "/purchasePlaces",
            {
                "club": self.club["name"],
                "competition": choice(["Spring Festival", "Fall Classic"]),
                "places": randint(0, 15),
            },
        )

    def on_start(self):
        self.client.get("/")
        self.club = choice(
            [
                {
                    "name": "Simply Lift",
                    "email": "john@simplylift.co",
                },
                {
                    "name": "Iron Temple",
                    "email": "admin@irontemple.com",
                },
                {
                    "name": "She Lifts",
                    "email": "kate@shelifts.co.uk",
                },
            ]
        )
        self.client.post("/login", {"email": self.club["email"]})

    def on_stop(self):
        self.client.get("/logout")
