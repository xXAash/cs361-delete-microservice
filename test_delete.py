# -----------------------------------------------
# test_delete.py
# Test program for verifying DELETE microservice
# Inserts test data, then deletes it using the API.
# -----------------------------------------------
import requests
from pymongo import MongoClient

# === FastAPI Setup ===
BASE = "http://localhost:8000"
HEADERS = {"Authorization": "Bearer faketoken123"}

# === MongoDB Setup ===
client = MongoClient("mongodb://localhost:27017/")
db = client["myDatabase"]  # <-- Replace with your DB name
users = db["users"]
projects = db["projects"]
subtasks = db["subtasks"]

# === Insert Test Data ===
def insert_test_documents():
    user_id = users.insert_one({"name": "Test User"}).inserted_id
    project_id = projects.insert_one({"title": "Test Project"}).inserted_id
    subtask_id = subtasks.insert_one({"task": "Test Subtask"}).inserted_id
    return str(user_id), str(project_id), str(subtask_id)

# === Tests ===
def test_successful_deletion(user_id, project_id, subtask_id):
    print(f"\nDeleting test user {user_id}:")
    print(requests.delete(f"{BASE}/user/{user_id}", headers=HEADERS).json())

    print(f"\nDeleting test project {project_id}:")
    print(requests.delete(f"{BASE}/project/{project_id}", headers=HEADERS).json())

    print(f"\nDeleting test subtask {subtask_id}:")
    print(requests.delete(f"{BASE}/subtask/{subtask_id}", headers=HEADERS).json())

def test_repeat_deletion(user_id, project_id, subtask_id):
    print(f"\nAttempting to delete already-deleted user {user_id}:")
    print(requests.delete(f"{BASE}/user/{user_id}", headers=HEADERS).json())

    print(f"\nAttempting to delete already-deleted project {project_id}:")
    print(requests.delete(f"{BASE}/project/{project_id}", headers=HEADERS).json())

    print(f"\nAttempting to delete already-deleted subtask {subtask_id}:")
    print(requests.delete(f"{BASE}/subtask/{subtask_id}", headers=HEADERS).json())

def test_invalid_id():
    print("\nDeleting with invalid ObjectId format:")
    print(requests.delete(f"{BASE}/user/invalid-id", headers=HEADERS).json())

def test_missing_auth(user_id):
    print("\nDeleting without Authorization header:")
    r = requests.delete(f"{BASE}/user/{user_id}")  # no headers
    print(f"Status Code: {r.status_code}")
    print(f"Response: {r.json()}")

# === Main ===
if __name__ == "__main__":
    print("Inserting test documents...")
    user_id, project_id, subtask_id = insert_test_documents()

    print("\nRunning successful deletion tests:")
    test_successful_deletion(user_id, project_id, subtask_id)

    print("\nRunning failure cases:")
    test_repeat_deletion(user_id, project_id, subtask_id)
    test_invalid_id()
    test_missing_auth(user_id)