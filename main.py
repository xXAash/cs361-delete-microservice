from fastapi import FastAPI, HTTPException, Header
from database import delete_subtask, delete_project, delete_user

# Initialize FastAPI app
app = FastAPI()

# ------------------------------
# DELETE /subtask/{subtask_id}
# ------------------------------
# This endpoint deletes a subtask by its ID.
# It expects an Authorization header for simulated security.
@app.delete("/subtask/{subtask_id}")
def remove_subtask(subtask_id: str, authorization: str = Header(...)):
    # Check if the subtask exists and delete it
    if not delete_subtask(subtask_id):
        # If it doesn't exist, raise a 404 error
        raise HTTPException(status_code=404, detail="Subtask not found.")
    # If deletion is successful, return a success message
    return {"status": "success", "message": f"Subtask {subtask_id} has been permanently deleted."}

# ------------------------------
# DELETE /project/{project_id}
# ------------------------------
# This endpoint deletes a project with by its ID.
# It expects an Authorization header for simulated security.
@app.delete("/project/{project_id}")
def remove_project(project_id: str, authorization: str = Header(...)):
    # Check if the project exists and delete it
    if not delete_project(project_id):
        # If it doesn't exist, raise a 404 error
        raise HTTPException(status_code=404, detail="Project not found.")
    # If deletion is successful, return a success message
    return {"status": "success", "message": f"Project {project_id} has been permanently deleted."}

# ------------------------------
# DELETE /user/{user_id}
# ------------------------------
# Deletes a user account with the given ID.
# Requires an Authorization header.
@app.delete("/user/{user_id}")
def remove_user(user_id: str, authorization: str = Header(...)):
    # Check if the user exists and delete it
    if not delete_user(user_id):
        # If it doesn't exist, raise a 404 error
        raise HTTPException(status_code=404, detail="User not found.")
    # If deletion is successful, return a success message
    return {"status": "success", "message": f"User {user_id} has been permanently deleted."}
