import numpy as np
import sounddevice as sd

duration = 1.0  # seconds
freq = 18000  # Hz (18 kHz, pushing ultrasonic range)
sample_rate = 44100

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
wave = 0.5 * np.sin(2 * np.pi * freq * t)
sd.play(wave, samplerate=sample_rate)
sd.wait()
