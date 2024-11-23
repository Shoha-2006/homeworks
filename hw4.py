###Task 1



def convert_to_far(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def convert_to_cel(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius_convert = convert_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {celsius_convert:.2f} degrees C\n")

    # Prompt user for Celsius input and convert to Fahrenheit
    celsius = float(input("Enter a temperature in degrees C: "))
    fahrenheit_convert = convert_to_far(celsius)
    print(f"{celsius} degrees C = {fahrenheit_convert:.2f} degrees F")




###Task 2    




def invest(amount: float, rate: float, years: int):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")


if __name__ == "__main__":
    invest(100, 0.05, 4)




#Task 3



def print_factors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")



if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print_factors(n)




#Task 4






universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]



def enrollment_stats(data):
    enrollments = [uni[1] for uni in data]
    tuitions = [uni[2] for uni in data]
    return enrollments, tuitions



def mean(values):
    return sum(values) / len(values)



def median(values):
    sorted_val = sorted(values)
    n = len(sorted_val)
    mid = n // 2
    if n % 2 == 1:
        return sorted_val[mid]
    else:
        return (sorted_val[mid - 1] + sorted_val[mid]) / 2


if __name__ == "__main__":
    enrollments, tuitions = enrollment_stats(universities)
    total_students = sum(enrollments)
    total_tuition = sum(tuitions)
    student_mean = mean(enrollments)
    student_median = median(enrollments)
    tuition_mean = mean(tuitions)
    tuition_median = median(tuitions)

    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}")
    print(f"\nStudent mean: {student_mean:,.2f}")
    print(f"Student median: {student_median:,.0f}")
    print(f"\nTuition mean: $ {tuition_mean:,.2f}")
    print(f"Tuition median: $ {tuition_median:,.0f}")
