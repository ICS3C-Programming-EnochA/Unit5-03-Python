# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program program is called "Grade Program" that has a function that takes a level and returns the middle percentage mark.


def calc_mark(level):
    if level == "4+":
        return 95
    elif level == "4":
        return 87
    elif level == "4-":
        return 80
    elif level == "3+":
        return 77
    elif level == "3":
        return 74
    elif level == "3-":
        return 71
    elif level == "2+":
        return 67
    elif level == "2":
        return 64
    elif level == "2-":
        return 61
    elif level == "1+":
        return 57
    elif level == "1":
        return 50
    elif level == "-1":
        return 49
    else:
        return -1


# def main is where we get the user_level and display user
def main():
    student_level = input("Enter the level: ")
    mark = calc_mark(student_level)
    if mark == -1:
        print("Invalid")
    else:
        print(f"Your level mark is {mark}")


if __name__ == "__main__":
    main()
