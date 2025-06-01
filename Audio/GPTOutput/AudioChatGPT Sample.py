import numpy as np
import wave
import simpleaudio as sa
import matplotlib.pyplot as plt

def play_audio(file_path):
    """Play the audio file."""
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def plot_waveform(file_path, title):
    """Plot the waveform of the audio file."""
    with wave.open(file_path, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)
        plt.figure(figsize=(10, 4))
        plt.plot(samples)
        plt.title(title)
        plt.xlabel('Sample Number')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

def clip_audio(file_path, output_path):
    """Clip the audio amplitude to half."""
    with wave.open(file_path, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(wf.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)
        clipped_samples = np.clip(samples, -2000, 2000)  # Clip values
        with wave.open(output_path, 'wb') as wf_out:
            wf_out.setparams(params)
            wf_out.writeframes(clipped_samples.tobytes())
    return output_path

def increase_volume(file_path, output_path):
    """Increase the audio volume."""
    with wave.open(file_path, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(wf.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)
        amplified_samples = np.clip(samples * 2, -32768, 32767).astype(np.int16)  # Amplify values
        with wave.open(output_path, 'wb') as wf_out:
            wf_out.setparams(params)
            wf_out.writeframes(amplified_samples.tobytes())
    return output_path

def change_frame_rate(file_path, output_path, new_rate):
    """Change the frame rate of the audio."""
    with wave.open(file_path, 'rb') as wf:
        params = list(wf.getparams())
        params[2] = new_rate  # Change frame rate
        frames = wf.readframes(wf.getnframes())
        with wave.open(output_path, 'wb') as wf_out:
            wf_out.setparams(params)
            wf_out.writeframes(frames)
    return output_path

def reverse_audio(file_path, output_path):
    """Reverse the audio."""
    with wave.open(file_path, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(wf.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16)
        reversed_samples = samples[::-1]
        with wave.open(output_path, 'wb') as wf_out:
            wf_out.setparams(params)
            wf_out.writeframes(reversed_samples.tobytes())
    return output_path

def mix_audio(file_path1, file_path2, output_path):
    """Mix two audio files."""
    with wave.open(file_path1, 'rb') as wf1, wave.open(file_path2, 'rb') as wf2:
        params = wf1.getparams()
        frames1 = wf1.readframes(wf1.getnframes())
        frames2 = wf2.readframes(wf2.getnframes())
        samples1 = np.frombuffer(frames1, dtype=np.int16)
        samples2 = np.frombuffer(frames2, dtype=np.int16)
        mixed_samples = np.clip((samples1[:len(samples2)] + samples2) // 2, -32768, 32767).astype(np.int16)
        with wave.open(output_path, 'wb') as wf_out:
            wf_out.setparams(params)
            wf_out.writeframes(mixed_samples.tobytes())
    return output_path

def main():
    input_file = "input.wav"  # Replace with your input file
    print("Audio Enhancements:")
    print("1. Clip Audio")
    print("2. Increase Volume")
    print("3. Change Frame Rate")
    print("4. Reverse Audio")
    print("5. Mix with Another Track")
    choice = int(input("Select an option (1-5): "))

    if choice == 1:
        output_file = clip_audio(input_file, "clipped.wav")
    elif choice == 2:
        output_file = increase_volume(input_file, "amplified.wav")
    elif choice == 3:
        new_rate = int(input("Enter new frame rate: "))
        output_file = change_frame_rate(input_file, "changed_rate.wav", new_rate)
    elif choice == 4:
        output_file = reverse_audio(input_file, "reversed.wav")
    elif choice == 5:
        secondary_file = input("Enter the path to the second track: ")
        output_file = mix_audio(input_file, secondary_file, "mixed.wav")
    else:
        print("Invalid choice.")
        return

    print("Playing original audio...")
    play_audio(input_file)
    plot_waveform(input_file, "Original Audio Waveform")

    print("Playing enhanced audio...")
    play_audio(output_file)
    plot_waveform(output_file, "Enhanced Audio Waveform")

if __name__ == "__main__":
    main()
