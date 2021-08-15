if __name__ == '__main__':
    # python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        python_students.append(student)

    scores_list = [student[1] for student in python_students]
    print(f"the score list is: {scores_list}")
    sorted(scores_list)
    print(f"ordered list: {scores_list}")

    min_value = scores_list[0]

    scores_list.remove(min_value)

    for score in scores_list:
        if min_value == score:
            scores_list.remove(score)

    second_lowest = scores_list[0]

    names_lowest = []

    for student in python_students:
        if second_lowest in student:
            names_lowest.append(student[0])

    ordered_names = names_lowest.sort
    for name in names_lowest:
        print(name)
