from datetime import datetime
from fastapi import FastAPI, HTTPException
from db.schemas import DB_Workmanagment

# currently time
time = datetime.now()

# initializing FastAPI library
app = FastAPI()

# initializing db tables
db_schemas = DB_Workmanagment()

@app.get("/")
async def get_users_applications():
    return db_schemas.db_get_users_applications_viewed()
       

@app.post("/applications")
async def user_application(
    name: str, 
    income: int, 
    existing_debt: int,
):
    user_application = [name, income, existing_debt]
    db_schemas.db_insert_user_application(
        name = name, 
        income = income, 
        existing_debt = existing_debt, 
        application_created = time
    )
 
    if user_application:
        db_schemas.db_insert_application_events(
            decision_viewed= "Under Review",
            decision_generated= "Under generation"
        )
        return {
            "message": "application receive successfully",
            "applicant_information": f"Name: {name}, Income: {income}, Existing Debt: {existing_debt}, Application Created at: {time}"
        }
    

    raise HTTPException(
        status_code=400,
        detail="application couldn't being process",        
    )
    
