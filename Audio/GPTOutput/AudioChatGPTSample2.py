import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import wave
from playsound import playsound
import os


def plot_waveform(audio_segment, title):
    # Convert audio to numpy array
    samples = np.array(audio_segment.get_array_of_samples())
    plt.figure(figsize=(10, 4))
    plt.plot(samples)
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


def apply_enhancement(audio, choice):
    if choice == 1:
        # Increase volume by 6 dB
        enhanced_audio = audio + 6
    elif choice == 2:
        # Reduce volume by 6 dB
        enhanced_audio = audio - 6
    elif choice == 3:
        # Clip the audio to 3 seconds
        enhanced_audio = audio[:3000]
    elif choice == 4:
        # Change frame rate to half
        enhanced_audio = audio.set_frame_rate(audio.frame_rate // 2)
    elif choice == 5:
        # Overlay the audio with itself (simulating multiple tracks)
        enhanced_audio = audio.overlay(audio)
    else:
        enhanced_audio = None
    return enhanced_audio


def save_temp_audio(audio, filename="temp.wav"):
    audio.export(filename, format="wav")
    return filename


def main():
    print("Audio Enhancements Program")
    print("1. Increase Volume")
    print("2. Decrease Volume")
    print("3. Clip Audio to 3 Seconds")
    print("4. Change Frame Rate")
    print("5. Overlay with Itself")

    # Load the audio file
    input_audio_path = input("Enter the path to the audio file (WAV format): ").strip()
    try:
        audio = AudioSegment.from_file(input_audio_path, format="wav")
    except Exception as e:
        print(f"Error loading audio: {e}")
        return

    # Display the original audio
    print("\nPlaying original audio...")
    plot_waveform(audio, "Original Audio Waveform")
    temp_file = save_temp_audio(audio)
    playsound(temp_file)

    # Get user's choice
    choice = int(input("\nSelect an enhancement (1-5): "))
    if choice not in range(1, 6):
        print("Invalid choice! Exiting...")
        return

    # Apply the selected enhancement
    enhanced_audio = apply_enhancement(audio, choice)
    if not enhanced_audio:
        print("Failed to apply enhancement. Exiting...")
        return

    # Display and play the enhanced audio
    print("\nPlaying enhanced audio...")
    plot_waveform(enhanced_audio, f"Enhanced Audio Waveform (Option {choice})")
    enhanced_temp_file = save_temp_audio(enhanced_audio, "enhanced_temp.wav")
    playsound(enhanced_temp_file)

    # Clean up temp files
    os.remove(temp_file)
    os.remove(enhanced_temp_file)
    print("Done.")


if __name__ == "__main__":
    main()
