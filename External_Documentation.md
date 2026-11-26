# External Documentation

A simple Python program that demonstrates how a brute-force password attack
works, by trying every possible combination of characters until it matches a
target password. It also estimates the longest time an attack could take, so
you can see how quickly the difficulty grows as a password gets longer.

> **Educational use only.** This is a demonstration run against a password we
> already know. It is for learning how brute-force searching and password
> strength work — not for gaining access to any real account or system.

## How it works

The program uses a **brute-force (exhaustive) search**. This is the simplest
kind of search: it has no shortcuts or guesses based on clues. It just tries
every possibility in order until it finds a match.

The search is built from two loops:

1. The **outer loop** chooses the length to try — first all 1-character
   strings, then all 2-character strings, and so on (shortest first).
2. The **inner loop** uses `itertools.product()` to generate every
   combination of that length, in order, and compares each one to the target.

Because it checks *everything*, the number of combinations grows as
`number_of_characters ** length`. Adding just one or two characters to a
password multiplies the work enormously — which is exactly why longer
passwords are stronger.

## Features

- A simple text menu to set the password, estimate the run time, or run the
  simulation.
- A worst-case time estimate, calculated *before* running, based on the size
  of the character set and the password length.
- A live attempt counter and timer while the search runs.

## How to run

1. Make sure you have **Python 3** installed.
2. Run the program from a terminal:

   ```bash
   python brute_force_sim.py
   ```

3. Use the menu to set a password, estimate the time, or run the simulation.
   Press `Ctrl+C` at any time to stop a running search.

The program uses only the Python standard library (`itertools` and `time`),
so there is nothing extra to install.

## References

- Python Software Foundation. *itertools — Functions creating iterators for
  efficient looping* (`itertools.product`).
  https://docs.python.org/3/library/itertools.html
- Python Software Foundation. *time — Time access and conversions*
  (`time.perf_counter`). https://docs.python.org/3/library/time.html
