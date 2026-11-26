# ============================================================
#  26-Nov-2026
#  Author: JDJ
#  Cert IV - Programming for Cybersecurity
#  Purpose: estimate how long a brute-force attack would take
#  for a chosen password, and (for short ones) actually run it.
# ============================================================

import itertools   # used to generate every possible character combination
import time        # used to measure how long the cracking take

# ---- GLOBAL VARIABLES ----

# characters: the "alphabet" the program is allowed to guess from
# (lowercase 26 + uppercase 26 + digits 10 + symbols 10 = 72 possible characters).
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Rough guess speed for a normal laptop running Python (guesses per second).
# This is an estimate so we can predict the time -- change it if you like.
GUESSES_PER_SECOND = 500_000


def estimate_time(target):
    # total: a counter that adds up every possible combination.
    total = 0
    # Loop over every password length from 1 up to the target's length.
    for length in range(1, len(target) + 1):
        # For each length there are (70 ^ length) combinations.
        # Add them onto the running total.
        total = total + len(characters) ** length   # combinations of this length

    # seconds: convert the number of guesses into a time estimate.
    seconds = total / GUESSES_PER_SECOND

    # Print the results. readable_time() is CALLED here to format seconds.
    print("\nPassword:", target, "(", len(target), "characters )")
    print("Total combinations to try:", format(total, ","))
    print("Longest it could take:", readable_time(seconds))   # <-- interaction
    print()


def readable_time(seconds):
    """Turn a number of seconds into easy-to-read units."""
    if seconds < 60:                                # under a minute
        return str(round(seconds, 2)) + " seconds"
    minutes = seconds / 60                          # convert to minutes
    if minutes < 60:
        return str(round(minutes, 2)) + " minutes"
    hours = minutes / 60                            # convert to hours
    if hours < 24:
        return str(round(hours, 2)) + " hours"
    days = hours / 24                               # convert to days
    if days < 365:
        return str(round(days, 2)) + " days"
    years = days / 365                              # convert to years
    return format(round(years), ",") + " years"


def crack(target):
    """Try every combination until the password is found."""
    attempts = 0                        # counts how many guesses we have made
    start = time.perf_counter()         # record the start time
    print("Starting... (press Ctrl+C to stop)\n")

    # Outer loop: try length 1, then 2, then 3 ... up to len(target).
    for length in range(1, len(target) + 1):
        # Inner loop: itertools.product builds EVERY combination of
        # that length automatically (this is the automation).
        for combo in itertools.product(characters, repeat=length):
            guess = "".join(combo)      # join the characters into one string
            attempts = attempts + 1     # update the counter each guess

            # Every 100,000 guesses, print a live progress update.
            if attempts % 100_000 == 0:
                elapsed = time.perf_counter() - start
                print("\rAttempts:", format(attempts, ","),
                      "| Elapsed:", round(elapsed, 1), "seconds",
                      end="", flush=True)

            # If the guess matches the target, report it and STOP.
            if guess == target:
                elapsed = time.perf_counter() - start
                print("\rPassword found:", guess)
                print("Attempts:", format(attempts, ","))
                print("Time taken:", round(elapsed, 4), "seconds")
                return


# ============================================================
#  MAIN MENU - this is what runs when the program starts.
#  It ties the functions above together based on user choice.
# ============================================================

target = ""             # holds the password the user sets (empty to start)

while True:             # repeat the menu forever until the user exits
    print("===== Brute-Force Simulator =====")
    print("1. Set the password")
    print("2. Estimate the longest run time")
    print("3. Run the simulation")
    print("4. Exit")

    # choice: stores the menu number the user typed.
    choice = input("Choose 1-4: ")

    if choice == "1":
        # Set/overwrite the target password.
        target = input("Enter the password: ")
    elif choice == "2":
        estimate_time(target)           # CALL the estimate function
    elif choice == "3":
        estimate_time(target)           # show the estimate first...
        go = input("This may take a while. Continue? (y/n): ")
        if go == "y":                   # ...only crack if the user agrees
            crack(target)               # CALL the cracking function
    elif choice == "4":
        break                           # leave the while loop -> program ends
    else:
        # Any input that is not 1-4 is caught here.
        print("Please choose 1, 2, 3 or 4.\n")