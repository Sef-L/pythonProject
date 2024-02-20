assinment = float(input("What is your assignment score?: "))
test = float(input("What is your tests score?: "))
paricitpation = float(input("What is your participation score?: "))

if assinment > 100 or assinment < 0:
    raise ValueError("Assignment must be between 0 and 100")
elif test > 100 or test < 0:
    raise ValueError("Tests must be between 0 and 100")
elif paricitpation > 100 or paricitpation < 0:
    raise ValueError("Participation must be between 0 and 100")

final_grade = (assinment*0.4)+(test*0.4)+(paricitpation*0.2)
print(f"Your final grade is: {final_grade}")