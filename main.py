import pyttsx3
import random
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed of speech

# List of wrestling moves
moves = [
    "Snap down",
    "Sprawl",
    "Level change",
    "Fake shot",
    "Circle left",
    "Circle right",
    "Penetration step",
    "Duck under",
    "High crotch",
    "Single leg",
    "Double leg",
    "Back step",
]

def say_move(move):
    """Function to say the selected move"""
    engine.say(move)
    engine.runAndWait()

def stance_and_motion_workout(rounds, round_duration, rest_duration):
    """Run the workout with given rounds, round duration, and rest duration"""
    
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num} - Start your wrestling stance and motion!")
        engine.say(f"Round {round_num} start!")
        engine.runAndWait()

        start_time = time.time()
        while time.time() - start_time < round_duration:
            # Select a random move
            move = random.choice(moves)
            
            # Say the move
            say_move(move)
            
            # Wait a few seconds before the next move
            time.sleep(5)

        print(f"Round {round_num} complete! Rest for {rest_duration} seconds.")
        engine.say(f"Round {round_num} complete. Take a rest.")
        engine.runAndWait()

        if round_num < rounds:
            time.sleep(rest_duration)  # Rest between rounds

    print("Workout complete! Good job.")
    engine.say("Workout complete! Good job.")
    engine.runAndWait()

# Get user input for rounds, round time, and rest time
rounds = int(input("Enter the number of rounds: "))
round_duration = int(input("Enter the duration of each round in seconds: "))
rest_duration = int(input("Enter the rest time between rounds in seconds: "))

# Start the workout
stance_and_motion_workout(rounds, round_duration, rest_duration)
