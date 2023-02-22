from pydub import AudioSegment
import os

# base = '/home/jlangley/git/demucs/data/moisesdb23_labelnoise_v1.0/ff486935-7ce2-4e23-8908-0ff5fcc50856'
base = '/home/jlangley/git/demucs/data/moisesdb23_labelnoise_v1.0'

with os.scandir(base) as entries:
    for entry in entries:
        print(entry.path)
        bass = AudioSegment.from_file(f'{entry.path}/bass.wav')
        drums = AudioSegment.from_file(f'{entry.path}/drums.wav')
        other = AudioSegment.from_file(f'{entry.path}/other.wav')
        vocals = AudioSegment.from_file(f'{entry.path}/vocals.wav')

        combined = bass.overlay(drums)
        combined = combined.overlay(vocals)
        combined = combined.overlay(other)
        combined.export(f'{entry.path}/mixture.wav', format='wav')