from db.schemas import DB_Workmanagment

class Score_Reviewed:
    def __init__(self):
        # initializing db tables
        self.db_schemas = DB_Workmanagment()
        self.user_information = self.db_schemas.db_get_users_information()
        self.user_income = self.db_schemas.db_get_user_income()
        self.user_debt = self.db_schemas.db_get_user_debt()
        self.users_name = self.db_schemas.db_get_users_name()
        
        # DTI Score Range
        self.credits_score = []
        self.excellent_possition = 36
        self.good_possition = 43
        self.high_risk = 50 
        
    
    def get_user_information(self):
        for i in self.user_information:
            print(i)
        
    # def reviewing_score(self,):
    #     for i in self.user_credit_score:
    #         print(i)
    #         # if i < self.good_possition and i <= self.excellent_possition:
    #         #     print(i)
                
    def score_calculations(self,):
        print(f"Users Name: {self.users_name}")
        # i = income, d = debt, u_n = users name
        for i, d, u_n in zip(self.user_income, self.user_debt, self.users_name):
            print(i)
            monthly_income = i / 12
            dti_score = (d / monthly_income) * 100
            if dti_score < self.excellent_possition:
                self.credits_score.append(dti_score)
                print("score list:", self.credits_score)
            else:
                print("There's any dti score for the excellent possition list")
                 
            print(f"{u_n} score: {dti_score}")
            

score_reviewing = Score_Reviewed()
score_reviewing.score_calculations()