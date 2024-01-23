# BMI Calculator 

name1 = "My Name"
height_m1 = 1.7272  #meters
weight_kg1 = 58

def bmi_calculator(name, height_m, weight_kg):
    
    bmi = weight_kg / (height_m ** 2) # Calculate BMI
    
    print("BMI:", bmi) # Print BMI

    # Determine if the person is overweight or not
    if bmi < 25:
        return "NOT overweight."
    else:
        return "Overweight."

result1 = bmi_calculator(name1, height_m1, weight_kg1)
print(result1)
