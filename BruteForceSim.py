# Brute-force password simulator (educational)
# A simple program that tries every possible combination of characters
# until it matches a target password. This is a demonstration only,
# run against a password we already know.
#
# Search method: brute-force (exhaustive) search. It has no shortcuts --
# it simply tries length 1, then length 2, and so on, testing every
# combination in order until it finds a match. Because it checks
# everything, the time grows very fast as the password gets longer.

import itertools
import time

# The characters the program is allowed to try
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Rough guess speed for a normal laptop running Python (guesses per second).
# This is an estimate so we can predict the time -- change it if you like.
GUESSES_PER_SECOND = 500_000


def estimate_time(target):
    """Work out the worst-case number of guesses and how long it could take."""
    total = 0
    for length in range(1, len(target) + 1):
        total = total + len(characters) ** length   # combinations of this length

    seconds = total / GUESSES_PER_SECOND

    print("\nPassword:", target, "(", len(target), "characters )")
    print("Total combinations to try:", format(total, ","))
    print("Longest it could take:", readable_time(seconds))
    print()


def readable_time(seconds):
    """Turn a number of seconds into easy-to-read units."""
    if seconds < 60:
        return str(round(seconds, 2)) + " seconds"
    minutes = seconds / 60
    if minutes < 60:
        return str(round(minutes, 2)) + " minutes"
    hours = minutes / 60
    if hours < 24:
        return str(round(hours, 2)) + " hours"
    days = hours / 24
    if days < 365:
        return str(round(days, 2)) + " days"
    years = days / 365
    return format(round(years), ",") + " years"


def crack(target):
    """Try every combination until the password is found."""
    attempts = 0
    start = time.perf_counter()
    print("Starting... (press Ctrl+C to stop)\n")

    for length in range(1, len(target) + 1):
        for combo in itertools.product(characters, repeat=length):
            guess = "".join(combo)
            attempts = attempts + 1

            if guess == target:
                elapsed = time.perf_counter() - start
                print("Password found:", guess)
                print("Attempts:", format(attempts, ","))
                print("Time taken:", round(elapsed, 4), "seconds")
                return


# ---- Simple menu ----
target = "Sp@in"

while True:
    print("===== Brute-Force Simulator =====")
    print("1. Set the password")
    print("2. Estimate the longest run time")
    print("3. Run the simulation")
    print("4. Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        target = input("Enter the password: ")
    elif choice == "2":
        estimate_time(target)
    elif choice == "3":
        estimate_time(target)
        go = input("This may take a while. Continue? (y/n): ")
        if go == "y":
            crack(target)
    elif choice == "4":
        break
    else:
        print("Please choose 1, 2, 3 or 4.\n")