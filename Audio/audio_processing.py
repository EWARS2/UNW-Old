# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #1 (worth 75% of the grade for this week)
Consider various audio enhancements (clip, multiple tracks, add volume, change frame rate, etc.).
It is O.K. if these enhancements are really simple.
Write a program with a simple menu that allows a user to select from one of at least five audio enhancements.
The program should play the original sound bite and the enhanced sound bite and display a relevant sound amplitude plot.
It is assumed that there will be many obstacles
(usually related to import libraries) in order to get your program to run.
So see how much of the code you can get to run,
and then detail whatever does not run.
YOU CAN GET FULL CREDIT FOR THIS PROGRAM EVEN IF PORTIONS OF YOUR PROGRAM DO NOT RUN.
DO NOT SPEND TOO MUCH TIME WORRYING ABOUT PARTS OF YOUR CODE THAT DON'T RUN.
"""

import os
import traceback
import matplotlib.pyplot as plt
import numpy as np
import wave
from pydub import AudioSegment  # TODO: fix my pydub install and test program

try:
    from playsound import playsound
except ImportError:
    print("Error importing playsound library.")

def exit_program(*args):
    print("Exiting...")
    exit()


def exit_on_bad_filepath(path):
    if not os.path.isfile(path):
        print(f"File {path} does not exist")
        exit_program()
    return path


# Adapted from "audio_processing" in Moodle
def display_wav(wav_path):
    # TODO: restructure for interactive graph so execution doesn't get paused.
    # plt.ion()
    obj = wave.open(wav_path, 'rb')
    raw = np.frombuffer(obj.readframes(-1), np.int16)
    plt.figure().canvas.manager.set_window_title(wav_path)
    plt.plot(raw, color='blue')
    plt.show()
    # plt.draw()
    obj.close()


# Adapted from "audio_processing" in Moodle
def analyze_wav(wav_path):
    obj = wave.open(wav_path, 'r')
    my_dictionary = dict(
        channel_count=obj.getnchannels(),
        sample_width=obj.getsampwidth(),
        frame_rate=obj.getframerate(),
        frame_count=obj.getnframes(),
        parameters=obj.getparams(),
        frames=obj.readframes(obj.getnframes())
    )
    obj.close()
    return my_dictionary


# Adapted from "audio_processing" in Moodle
def write_wav(path, frames, frame_rate=88200, channels=2, sample_width=2):
    obj = wave.open(path, 'w')
    obj.setnchannels(channels)
    obj.setsampwidth(sample_width)
    obj.setframerate(frame_rate)
    obj.writeframes(frames)
    obj.close()


# Adapted from "audio_processing" in Moodle
def crop(path):
    audio = AudioSegment.from_wav(path)
    print("Current audio duration: " + str(audio.duration_seconds))
    print("Length: " + str(len(audio)))
    minimum = int(input("Start: "))
    maximum = int(input("Finish: "))
    audio = audio[minimum:maximum]
    print("New audio duration: " + str(audio.duration_seconds))
    print("Length: " + str(len(audio)))
    audio.export(path, format="wav")


def add_gain(path):
    audio = AudioSegment.from_file(path)
    gain_db = float(input("Gain (dB): "))
    audio = audio + gain_db
    audio.export(path, format="wav")


def change_frame_rate(path):
    data = analyze_wav(path)
    print("Current frame rate: " + str(data["frame_rate"]))
    data["frame_rate"] = int(input("Change frame rate value: "))
    write_wav(path, data["frames"], data["frame_rate"], data["channel_count"], data["sample_width"])


def fade_in(path):
    audio = AudioSegment.from_wav(path)
    value = float(input("Fade-in value: "))
    audio = audio.fade_in(value)
    audio.export(path, format="wav")


def fade_out(path):
    audio = AudioSegment.from_wav(path)
    value = float(input("Fade-out value: "))
    audio = audio.fade_out(value)
    audio.export(path, format="wav")


def main():
    # Setup paths
    original_path = exit_on_bad_filepath("sample.wav")
    # original_path = exit_on_bad_filepath(input("Enter .wav path:"))
    filename, file_extension = os.path.splitext(original_path)
    edited_path = filename + "_edited" + file_extension

    # Copy data to operate on it
    data = analyze_wav(original_path)
    write_wav(edited_path, data["frames"], data["frame_rate"], data["channel_count"], data["sample_width"])

    # List of functions.
    # Used to create a pseudo case structure.
    options = [exit_program,
               crop,
               add_gain,
               fade_in,
               fade_out,
               change_frame_rate,
               ]

    # Mainloop
    while True:
        print("Displaying graph...")
        display_wav(edited_path)

        # Attempts to play sound.
        # It's written this way so that you can still run without the playsound library.
        try:
            input(f"Press Enter to play {edited_path}")
            playsound(edited_path)
        except Exception as exc:  # Pass error to console, but don't crash
            print(traceback.format_exc())
            print(exc)

        # Formatted display of functions in options.
        # Example output of example_function():
        # 0. Example Function
        print("\n\nOptions:")
        for i in range(len(options)):
            print(f"{i: >2}. " + options[i].__name__.title().replace("_", " "))

        # Get user's choice and run the according function.
        # Print errors reported from function.
        # Uses a pseudo case structure.
        try:
            choice = int(input("Choice:"))
            options[choice](edited_path)
        except Exception as exc:  # Pass error to console, but don't crash
            print(traceback.format_exc())
            print(exc)


# Call the main func
if __name__ == '__main__':
    main()
