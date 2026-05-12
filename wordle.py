import random

GREEN = "\033[42m\033[30m"
YELLOW = "\033[43m\033[30m"
GRAY = "\033[100m\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

WORD_LIST = [
    "apple", "brave", "crane", "dream", "eagle",
    "fable", "grace", "haste", "input", "joker",
    "kneel", "lemon", "magic", "noble", "olive",
    "paint", "queen", "river", "stone", "tiger",
    "ultra", "vivid", "waste", "xenon", "yacht",
    "zebra", "alarm", "blend", "chord", "drift",
    "ember", "flint", "gloom", "honey", "index",
    "jazzy", "karma", "lunar", "mirth", "nerve",
    "ocean", "plume", "quirk", "radar", "shelf",
    "thyme", "usher", "vault", "witty", "expel",
]

def get_feedback(guess, secret):
    feedback = []
    secret_chars = list(secret)
    result = ["gray"] * 5

    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "green"
            secret_chars[i] = None

    for i in range(5):
        if result[i] == "green":
            continue
        if guess[i] in secret_chars:
            result[i] = "yellow"
            secret_chars[secret_chars.index(guess[i])] = None

    for i, color in enumerate(result):
        if color == "green":
            feedback.append(f"{GREEN} {guess[i].upper()} {RESET}")
        elif color == "yellow":
            feedback.append(f"{YELLOW} {guess[i].upper()} {RESET}")
        else:
            feedback.append(f"{GRAY} {guess[i].upper()} {RESET}")

    return "".join(feedback)

def play():
    secret = random.choice(WORD_LIST)
    attempts = 6
    print(f"\n{BOLD}Welcome to Wordle!{RESET}")
    print("Guess the 5-letter word. You have 6 attempts.")
    print(f"{GREEN} G {RESET} = right letter, right spot  "
          f"{YELLOW} Y {RESET} = right letter, wrong spot  "
          f"{GRAY} X {RESET} = not in word\n")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/6: ").strip().lower()
            if len(guess) != 5:
                print("  Must be exactly 5 letters. Try again.")
            elif not guess.isalpha():
                print("  Letters only. Try again.")
            else:
                break

        print("  " + get_feedback(guess, secret))
        print()

        if guess == secret:
            print(f"{BOLD}You got it in {attempt}! The word was '{secret.upper()}'.{RESET}\n")
            return

    print(f"Out of attempts! The word was {BOLD}{secret.upper()}{RESET}.\n")

def main():
    while True:
        play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main() 
