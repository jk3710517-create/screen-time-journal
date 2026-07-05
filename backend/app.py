from fastapi import FastAPI
from pydantic import BaseModel
from db import (
    get_all_users,
    get_all_activities,
    get_all_screen_logs,
    add_screen_log,
    update_screen_log,
    delete_screen_log
)
app = FastAPI()

class ScreenLog(BaseModel):
    user_id: int
    activity_id: int
    log_date: str
    device: str
    hours_spent: float


@app.get("/")
def home():
    return {
        "message": "Welcome to Screen Time Journal API!"
    }

@app.get("/users")
def users():
    return get_all_users()

@app.get("/activities")
def activities():
    return get_all_activities()

@app.get("/screenlogs")
def screenlogs():
    return get_all_screen_logs()

@app.post("/screenlogs")
def create_screenlog(log: ScreenLog):
    add_screen_log(
        log.user_id,
        log.activity_id,
        log.log_date,
        log.device,
        log.hours_spent
    )

    return {"message": "Screen Log Added Successfully"}

@app.put("/screenlogs/{log_id}")
def update_screenlog(log_id: int, log: ScreenLog):
    update_screen_log(log_id, log.hours_spent)

    return {
        "message": "Screen Log Updated Successfully"
    }

@app.delete("/screenlogs/{log_id}")
def delete_screenlog(log_id: int):
    delete_screen_log(log_id)

    return {
        "message": "Screen Log Deleted Successfully"
    }