from locust import FastHttpUser, task, between

class UserBehavior(FastHttpUser):
    wait_time = between(1, 3)  # Waktu tunggu antara permintaan

    @task(3)
    def get_users(self):
        response = self.client.get("/users")
        print("GET /users", response.status_code)

    @task(2)
    def get_user(self):
        user_id = 1  # Ganti dengan ID pengguna yang ingin diuji
        response = self.client.get(f"/users/{user_id}")
        print(f"GET /users/{user_id}", response.status_code)

    @task(1)
    def create_user(self):
        response = self.client.post("/users", json={"id": 3, "name": "Charlie", "email": "charlie@example.com"})
        print("POST /users", response.status_code)

    @task(1)
    def update_user(self):
        user_id = 1  # Ganti dengan ID pengguna yang ingin diperbarui
        response = self.client.put(f"/users/{user_id}", json={"id": user_id, "name": "Alice Updated", "email": "alice_updated@example.com"})
        print(f"PUT /users/{user_id}", response.status_code)

    @task(1)
    def delete_user(self):
        user_id = 2  # Ganti dengan ID pengguna yang ingin dihapus
        response = self.client.delete(f"/users/{user_id}")
        print(f"DELETE /users/{user_id}", response.status_code)

# Untuk menjalankan locust, gunakan perintah berikut di terminal:
# locust -f locustfile.py --host http://127.0.0.1:8000
