import time


def self_destruct():
    countdown = 10
    print("This unit will now self destruct.")
    time.sleep(1)
    while countdown != 0:   # countdown displays with a 1 sec cooldown
        print(countdown)
        countdown -= 1
        time.sleep(1)
    if countdown == 0:
        print("*Explosion Sounds*")  # animated this later. Filler for now

def math():
    answer = input("Yes or No?: ").capitalize()
    try:
        if answer == "Yes":
            x = float(input("What's the First Number?: "))
            y = float(input("And the Second Number?: "))
            answer = x + y
            print(f"The Answer is {answer}")
            time.sleep(2)
        elif answer == "No":
            print("i tHOuGht We weRe BESTIES!!!!! :(")
            time.sleep(2)
    except ValueError:
        print("Input Error Detected!")
        time.sleep(1)
    finally:
        self_destruct()

def main():
    print("Hello User ")
    name = input("What is your Name?: ")
    print(f"Hello {name}!")  # f statement adds input to str.
    time.sleep(1)
    print("My name is Add Bot! Lets be Friends!")
    time.sleep(1)
    print("Want me to add something for you Best Friend?")
    math()

main()
# This program adds 2 user input integers together then explodes
