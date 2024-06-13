import random

def generate_secret_code():
    return random.randrange(1000, 10000)

secret_code = generate_secret_code()
def main():
    attempts = 0
    while True:
        guess = int(input("Guess the 4-digit number: "))
        attempts += 1

        if guess == secret_code:
            print(f"Great! You guessed the number in just 1 try! You're a Mastermind!")
            break
        else:
            check_guess(guess)

def check_guess(guess):
    count = 0
    guess_str = str(guess)
    secret_str = str(secret_code)
    correct = ['X'] * 4

    for i in range(4):
        if guess_str[i] == secret_str[i]:
            count += 1
            correct[i] = guess_str[i]

    print(f"Not quite the number. But you did get {count} digit(s) correct!")
    print("Digits in correct position:", ' '.join(correct))
    print("\n")

if __name__ == "__main__":
    main()
