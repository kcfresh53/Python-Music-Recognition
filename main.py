import asyncio
import json
import pyaudio  # For recording audio
import wave  # FOr writing audio to an output WAV file
from shazamio import Shazam


async def record():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 5  # How long to record audio
    filename = "output.wav"  # Name of output file
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    await main()


async def main():
    shazam = Shazam()
    out = await shazam.recognize_song('output.wav')  # Can change read file
    print(out)
    with open('output.json', 'w') as f:
        f.write(json.dumps(out, indent=6))


loop = asyncio.get_event_loop()
loop.run_until_complete(record())
