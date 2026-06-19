from sqlalchemy import create_engine, text, select
from db.db_models import Base, UserApplication, ApplicationEvents
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import HTTPException


def creating_db():
    db_url = ("postgresql+psycopg2://postgres:root@localhost:5431/gustavocamacho")
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)
        
    with engine.connect() as connection:
        result = connection.execute(text('SELECT * from user_application;'))
        
        for row in result:
            print(row)
            
time_now = datetime.now()

class DB_Workmanagment:
    def __init__(self):
        self.db_url = ("postgresql+psycopg2://postgres:root@localhost:5431/gustavocamacho")
        self.engine = create_engine(self.db_url)
        

    def db_get_users_information(self):
        users_list = []
        users_id = []
        with Session(self.engine) as session:
            #building the statement of wich table do you wanna fetch informmation
            stmt = select(UserApplication)
            # executing as an ORM object
            for row in session.scalars(stmt).all():
                users_list.append(row)
                users_id.append(row.id)
                
        return users_list
    
    def db_get_users_id(self):
        users_id = []
        with Session(self.engine) as session:
            #building the statement of wich table do you wanna fetch informmation
            stmt = select(UserApplication)
            # executing as an ORM object
            for row in session.scalars(stmt).all():
                users_id.append(row.id)
                
        return users_id
    
    def db_get_last_users_id(self):
        # getting the last id of the user
        with Session(self.engine) as session:
            user_id = session.scalar(select(UserApplication.id).order_by(
                UserApplication.id.desc()
            ))
            # print(user_id)
            return user_id

    def db_get_user_income(self):
        income_list = []
        debt_list = []
        with Session(self.engine) as session:
            #building the statement of wich table do you wanna fetch informmation
            stmt = select(UserApplication)
            # executing as an ORM object
            for row in session.scalars(stmt).all():
                income_list.append(row.income)
                debt_list.append(row.existing_debt)

        return income_list
    
    def db_get_user_debt(self):
        debt_list = []
        with Session(self.engine) as session:
            #building the statement of wich table do you wanna fetch informmation
            stmt = select(UserApplication)
            # executing as an ORM object
            for row in session.scalars(stmt).all():
                debt_list.append(row.existing_debt)

        return debt_list
    
    def db_get_users_name(self):
        users_name_list = []
        with Session(self.engine) as session:
            #building the statement of wich table do you wanna fetch informmation
            stmt = select(UserApplication)
            # executing as an ORM object
            for row in session.scalars(stmt).all():
                users_name_list.append(row.name)

        return users_name_list
    
    def db_get_users_applications_viewed(self):
        keys_dict = ["Name:", "Decision viewed:", "Decision generated:"]
        users_application_reviewed_list = []
        with Session(self.engine) as session:
            #building the statement of wich table do you wanna fetch informmation
            stmt = (select(
                UserApplication.name,
                ApplicationEvents.decision_viewed,
                ApplicationEvents.decision_generated
                ).join(ApplicationEvents, UserApplication.id == ApplicationEvents.name_id))
            # executing as an ORM object
            for row in session.execute(stmt).all():
                users_application_reviewed_list.append(row[0])
                users_application_reviewed_list.append(row[1])
                users_application_reviewed_list.append(row[2])
        

        users_application_dict = dict(zip(keys_dict, users_application_reviewed_list))
        return users_application_dict
                
            # print(stmt)

    # insertion of data in the db.
    def db_insert_user_application(
        self,
        name,
        income: int,
        existing_debt: int,
        application_created,
    ):

        try:     
            with Session(self.engine) as session:
                user = UserApplication(
                    name=name, 
                    income=income, 
                    existing_debt=existing_debt,
                    application_created=application_created
                )
                
                session.add(user)
                
                session.commit()
                
                return {
                    "message":"Application added successfully",
                    "status_code":200
                }

        except Exception as e:
            print(f"error {e}")
            raise HTTPException(
                status_code=400,
                detail="Something went wrong"
            )
        
    def db_insert_application_events(
        self,
        decision_viewed,
        decision_generated
    ):
        try:
            with Session(self.engine) as session:
                user_id = session.scalar(
                    select(UserApplication.id).order_by(
                        UserApplication.id.desc()
                    ))
                event = ApplicationEvents(
                    name_id = user_id,
                    decision_viewed = decision_viewed,
                    decision_generated = decision_generated
                )
                
                session.add(event)
                session.commit()
                
                return {
                    "message":"Application added successfully",
                    "status_code":200
                }
            
        except Exception as e:
            print(f"error {e}")
            raise HTTPException(
                status_code=400,
                detail="error trying to load the data to the DB"
            )
# db_insert_user_application(
#     "Gustavo",
#     100000,
#     1000,
#     0,
#     time_now
# )

# creating_db()

testing = DB_Workmanagment()
# for i in testing.db_get_users_id():
#     print(i)
    

print(testing.db_get_users_applications_viewed())