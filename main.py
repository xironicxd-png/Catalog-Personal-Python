import math

PASSING_GRADE = 5
MAX_FAILS_TO_REPEAT = 3

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Invalid. Must be at least 1.")
                continue
            return value
        except ValueError:
            print("Invalid. Enter a whole number.")

def get_subject_average(subject_num):
    print(f"\n--- Subject {subject_num} ---")
    while True:
        raw = input("Enter grades (separated by space): ")
        try:
            grades = [int(n) for n in raw.split()]
        except ValueError:
            print("Invalid. Enter only integers.")
            continue
        if not grades or any(g < 1 or g > 10 for g in grades):
            print("Invalid. Grades must be between 1 and 10.")
            continue
        return math.floor(sum(grades) / len(grades) + 0.5)

def main():
    nr_materii = get_positive_int("How many subjects do you have? ")
    averages = [get_subject_average(i) for i in range(1, nr_materii + 1)]

    for i, avg in enumerate(averages, start=1):
        print(f"Rounded average for subject {i}: {avg}")

    corigente = sum(1 for avg in averages if avg < PASSING_GRADE)
    media_anuala = sum(averages) / nr_materii

    print(f"\nYearly average: {media_anuala:.2f}")
    print(f"Subjects to retake: {corigente}")
    if corigente >= MAX_FAILS_TO_REPEAT:
        print("You must repeat the year")

main()
