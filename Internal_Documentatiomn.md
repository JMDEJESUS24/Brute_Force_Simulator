# Internal Technical Documentation

## 1. Overview

**Purpose:** estimate how long a brute-force attack would take on a chosen
password, and — for short passwords — actually run the attack by trying every
character combination until it matches. Educational only: it is run against a
password that is already known.

**Modules:** Python standard library only. `itertools` generates the character
combinations and `time` measures how long the search takes. There is no network
use and nothing extra to install.

**Interface:** the program is menu-driven in the terminal; it does not read or
write any files.

## 2. Program structure

The script has two constants and three functions, plus a main menu loop.

- `characters` — the 72-character set that guesses are built from (letters, digits, symbols).
- `GUESSES_PER_SECOND = 500_000` — an assumed guessing speed, used only for the time estimate.
- `estimate_time(target)` — calculates the worst-case combinations and time (menu option 2).
- `readable_time(seconds)` — converts a number of seconds into friendly units.
- `crack(target)` — runs the real brute-force search (menu option 3).
- The `while True` menu loop — shows the options and calls the functions.

```
menu loop
 |-- estimate_time()  --> readable_time()
 |-- crack()
```

## 3. Logic of each function

### estimate_time(target)

1. Start a counter `total = 0`.
2. Loop over each password length from 1 up to the length of the target.
3. For each length, add `72 ** length` to `total` — the number of combinations of that length.
4. Divide `total` by `GUESSES_PER_SECOND` to get a time in seconds.
5. Print the password, the total combinations, and the time formatted by `readable_time()`.

This function only calculates — it does no cracking.

### readable_time(seconds)

1. If the time is under 60 seconds, return it in seconds.
2. Otherwise convert up through minutes, hours, days and years, returning at the first unit that fits.

It returns the result as a text string to whoever called it.

### crack(target)

1. Set `attempts = 0` and record the start time.
2. Outer loop: try length 1, then 2, and so on up to the target's length.
3. Inner loop: `itertools.product()` builds every combination of that length automatically.
4. Join each combination into a `guess` and add 1 to `attempts`.
5. Every 100,000 guesses, print a live progress line.
6. If the guess matches the target, print the password, attempts and time, then `return` to stop.

Both loops run a fixed number of times, so the function always ends.

### Main menu loop

1. Print the four menu options.
2. Read the user's choice.
3. Use `if/elif/else`: option 1 sets the password, 2 calls `estimate_time`, 3 calls
   `estimate_time` then `crack` (if confirmed), 4 ends the program, and any other
   input shows an error.
