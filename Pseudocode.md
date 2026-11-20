#Setup
Set the list of characters to try (letters, numbers, symbols)
Set the assumed guessing speed to 500000 (for a typical laptop)
Set the target password to empty

#Main Menu
Print "1. Set the password"
Print "2. Estimate the longest run time"
Print "3. Run the simulation"
Print "4. Exit"

#Input user's choice
If user's choice is equal to 1
    Input the password
else if user's choice is equal to 2
    Estimate the run time
else if user's choice is equal to 3
    Estimate the run time
    Ask "Continue? (y/n)"
    If yes
        Run the simulation
else if user's choice is equal to 4
    Stop the program
else
    Print "Invalid choice"


#Estimate Run Time
Set total to 0
For each password length from 1 up to the length of the target
    Add the number of possible combinations for that length to total
Work out the time as total combinations divided by guessing speed
Print the password, the total combinations, and the readable time


#Run Simulation
Set attempts to 0
Record the start time
Print "Starting..."
For each password length from 1 up to the length of the target
    For every possible combination of that length
        Build the guess
        Add 1 to attempts
        Every 100000 attempts, show the attempts and time elapsed
        If the guess is equal to the target
            Print "Password found", the number of attempts, and the time taken
            Stop


#Readable Time
If the time is under 60 seconds, show it in seconds
else if under 60 minutes, show it in minutes
else if under 24 hours, show it in hours
else if under 365 days, show it in days
else show it in years
