import time
from gpiozero import PWMOutputDevice

# Define the GPIO pin where the buzzer is connected
BUZZER_PIN = 12  # Change this to the correct GPIO pin number

# Create a PWMOutputDevice object
buzzer = PWMOutputDevice(BUZZER_PIN)

# Define the frequencies for the musical notes (in Hz)
CHORDS = {
    'DO': 261,   # C4
    'RE': 294,   # D4
    'MI': 329,   # E4
    'FA': 349,   # F4
    'SOL': 392,  # G4
    'LA': 440,   # A4
    'SI': 493    # B4
}

# Define melodies
melody = [
    ('DO', 0.5), ('DO', 0.5), ('RE', 0.5), ('DO', 0.5),
    ('FA', 0.5), ('MI', 1.0),
    ('DO', 0.5), ('DO', 0.5), ('RE', 0.5), ('DO', 0.5),
    ('SOL', 0.5), ('FA', 1.0),
    ('DO', 0.5), ('DO', 0.5), ('DO', 0.5), ('LA', 0.5),
    ('FA', 0.5), ('MI', 0.5), ('RE', 1.0)
]
# melodies = {
#     "Twinkle": [
#         ('DO', 0.5), ('DO', 0.5), ('SOL', 0.5), ('SOL', 0.5),
#         ('LA', 0.5), ('LA', 0.5), ('SOL', 1.0),
#         ('FA', 0.5), ('FA', 0.5), ('MI', 0.5), ('MI', 0.5),
#         ('RE', 0.5), ('RE', 0.5), ('DO', 1.0)
#     ],
#     "Mary": [
#         ('MI', 0.5), ('RE', 0.5), ('DO', 0.5), ('RE', 0.5),
#         ('MI', 0.5), ('MI', 0.5), ('MI', 1.0),
#         ('RE', 0.5), ('RE', 0.5), ('MI', 0.5), ('RE', 0.5),
#         ('DO', 1.0)
#     ],
#     "Ode": [
#         ('MI', 0.5), ('MI', 0.5), ('FA', 0.5), ('SOL', 0.5),
#         ('SOL', 0.5), ('FA', 0.5), ('MI', 0.5), ('RE', 0.5),
#         ('DO', 0.5), ('DO', 0.5), ('RE', 0.5), ('MI', 0.5),
#         ('MI', 0.5), ('RE', 0.5), ('RE', 0.5)
#     ],
#     "Birthday": [
#         ('DO', 0.5), ('DO', 0.5), ('RE', 0.5), ('DO', 0.5),
#         ('FA', 0.5), ('MI', 1.0),
#         ('DO', 0.5), ('DO', 0.5), ('RE', 0.5), ('DO', 0.5),
#         ('SOL', 0.5), ('FA', 1.0),
#         ('DO', 0.5), ('DO', 0.5), ('DO', 0.5), ('LA', 0.5),
#         ('FA', 0.5), ('MI', 0.5), ('RE', 1.0)
#     ],
#     "Saria": [
#         ('DO', 0.5), ('RE', 0.5), ('MI', 0.5), ('RE', 0.5),
#         ('DO', 0.5), ('DO', 0.5), ('RE', 0.5), ('MI', 0.5),
#         ('RE', 0.5), ('MI', 0.5), ('RE', 0.5), ('DO', 1.0)
#     ]
# }

def play_melody(melody):
    for note, duration in melody:
        frequency = CHORDS[note]
        print(f'Playing {note} ({frequency} Hz)')
        buzzer.frequency = frequency  # Set the frequency
        buzzer.value = 0.5  # Set the duty cycle (50% to produce sound)
        time.sleep(duration)  # Duration for each note
        buzzer.value = 0  # Stop the buzzer
        time.sleep(0.1)  # Short pause between notes

play_melody(melody)