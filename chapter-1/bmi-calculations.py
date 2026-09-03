#global varaibles and imporats

#getting user inputs as height and wright
def get_user_inputs():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    return weight, height


#calculate bmi
def calculate_bmi(weight, height):
    return weight // (height**2)

#get the bmi result
def get_bmi_result(bmi):
    print(f"bmi : {bmi}\nresult:")
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Over Weight")
    elif 30 <= bmi < 35:
        print("Obese")
    else:
        print("Extremely Obese")

#create main function to run
def main():
    weight, height =get_user_inputs()
    bmi = calculate_bmi(weight, height)
    get_bmi_result(bmi)

if __name__ == "__main__":
    main()