from pymongo import MongoClient
from bson.objectid import ObjectId

# === CONFIGURATION ===

# MongoDB URI (default local setup with no auth). Change if needed.
MONGO_URI = "mongodb://localhost:27017/"

DATABASE_NAME = "myDatabase"        # <-- Replace with your actual DB name
USER_COLLECTION = "users"           # <-- Replace with your actual users collection
PROJECT_COLLECTION = "projects"     # <-- Replace with your actual projects collection
SUBTASK_COLLECTION = "subtasks"     # <-- Replace with your actual subtasks collection

# If using string IDs set this to False (default OBJECT_ID)
USE_OBJECT_ID = True

# === CONNECTION SETUP ===

# Connect to the MongoDB server and select the database
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# Reference each collection in the database
users = db[USER_COLLECTION]
projects = db[PROJECT_COLLECTION]
subtasks = db[SUBTASK_COLLECTION]

# === UTILITY ===

# Converts string to ObjectId if needed (MongoDB expects ObjectId by default)
def build_id(id_val):
    return ObjectId(id_val) if USE_OBJECT_ID else id_val

# === DELETE FUNCTIONS ===

# Deletes a user document by _id from the users collection
def delete_user(user_id):
    try:
        return users.delete_one({"_id": build_id(user_id)}).deleted_count > 0
    except Exception as e:
        print(f"Error deleting user: {e}")
        return False

# Deletes a project document by _id from the projects collection
def delete_project(project_id):
    try:
        return projects.delete_one({"_id": build_id(project_id)}).deleted_count > 0
    except Exception as e:
        print(f"Error deleting project: {e}")
        return False

# Deletes a subtask document by _id from the subtasks collection
def delete_subtask(subtask_id):
    try:
        return subtasks.delete_one({"_id": build_id(subtask_id)}).deleted_count > 0
    except Exception as e:
        print(f"Error deleting subtask: {e}")
        return False