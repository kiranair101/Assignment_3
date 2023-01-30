def BMI_calculator(height, weight):
    """
    To Calculate the BMI. Source: Mechanical.com
    """
    BMI = round(weight / (height ** 2) * 703, 1)
    if BMI < 18.5:
        return "You are currently underweight and your BMI is " + str(BMI)
    if 18.5 < BMI < 24.9:
        return "You are currently normal and your BMI is " + str(BMI)
    if 25 < BMI < 29.9:
        return "You are currently overweight and your BMI is " + str(BMI)
    if 30 < BMI < 34.9:
        return "You are currently obese (Class 1) and your BMI is " + str(BMI)
    if 35 < BMI < 39.9:
        return "You are currently obese (Class 2) and your BMI is " + str(BMI)
    if BMI > 40:
        return "You are currently extremely obese and your BMI is " + str(BMI)
