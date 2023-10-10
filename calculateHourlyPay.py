#   Working calculateHourlyPay - Clean implimentation by Inj
#   Need to add step by step comments 

def validate_input(input: str) -> bool:
    try:
        input = float(input)
    except ValueError:
        print("Invalid input.")
        return False
    return True


def calculate_input(wage_input: str, hours_input: str) -> float:
    wage_input = float(wage_input)
    hours_input = float(hours_input)

    if hours_input <= 40:
        return hours_input * wage_input
    elif hours_input > 40:
        return (hours_input - 40) * wage_input * 1.5 + (40 * wage_input)


def calculateHourlyPay():
    while True:
        wage_input = input("What is your hourly wage? \n $ ")
        if validate_input(wage_input) == False:
            continue
        hours_input = input("How many hours have you worked? ")
        if validate_input(hours_input) == False:
            continue
        print(f"Your incoming payment will be {calculate_input(wage_input, hours_input):.2f}")
        return


def main():
    calculateHourlyPay()


if __name__ == "__main__":
    main()
