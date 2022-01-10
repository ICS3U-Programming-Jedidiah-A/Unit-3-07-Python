#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 3, 2021
# This program shows compatible spouses for people.
def main():
    user_age_as_string = input("Enter your age: ")
    try:
        user_age_as_int = int(user_age_as_string)
        if user_age_as_int <= 0:
            print("This input is invalid")
        elif user_age_as_int <= 25:
            print("your too young")
        elif user_age_as_int >= 45:
            print("your too old")

    except Exception:
        print("This input is invalid")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
