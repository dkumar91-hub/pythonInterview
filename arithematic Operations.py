'''milk expenditure'''
price_milk_per_litre=45
days=30
expenditure_milk=price_milk_per_litre*days
print("milk expenditure:",expenditure_milk)

'''veg.expenditure'''
price_veg_per_day=70
expenditure_veg=price_veg_per_day*days
print("veg expendidure:",expenditure_veg)

'''ration expenditure'''
price_ration_per_month=1000
month=1
expenditure_ration=price_ration_per_month*month
print("ration expenditure:",expenditure_ration)

'''medical expenditure'''
price_medical_per_month=7000
expenditure_medical=price_medical_per_month*month
print("medical expenditure:",expenditure_medical)

'''petrol expenditure'''
price_petrol_per_month=3000
expenditure_petrol=price_petrol_per_month*month
print("petrol expenditure:",expenditure_petrol)

'''internet expenditure'''
price_internet_per_month=1000
expenditure_internet=price_internet_per_month*month
print("internet expenditure:",expenditure_internet)

'''aditional expenditure'''
price_additional_per_day=100
expenditure_additional=price_additional_per_day*days
print("additional expenditure:",expenditure_additional)

final_expenditure=expenditure_milk+expenditure_veg+expenditure_ration+expenditure_medical+expenditure_petrol+expenditure_internet+expenditure_additional
print("total expenditure:",final_expenditure)