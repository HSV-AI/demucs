from pydub import AudioSegment
import os
import numpy as np

base = '/workspaces/demucs/data/moisesdb23_labelnoise_v1.0/test'

with os.scandir(base) as entries:
    for entry in entries:
        print(entry.path)
        bass = AudioSegment.from_file(f'{entry.path}/bass.wav')
        drums = AudioSegment.from_file(f'{entry.path}/drums.wav')
        other = AudioSegment.from_file(f'{entry.path}/other.wav')
        vocals = AudioSegment.from_file(f'{entry.path}/vocals.wav')

        silence = AudioSegment.silent(frame_rate=bass.frame_rate, duration=len(bass))
        bass = silence.overlay(bass)
        drums = silence.overlay(drums)
        other = silence.overlay(other)
        vocals = silence.overlay(vocals)

        if bass.frame_count() != drums.frame_count():
            raise ValueError(
                f"Invalid length for file {entry.name} 1: "
                f"expecting {bass.frame_count()} but got {drums.frame_count()}.")

        if bass.frame_count() != other.frame_count():
            raise ValueError(
                f"Invalid length for file {entry.name} 2: "
                f"expecting {bass.frame_count()} but got {other.frame_count()}.")

        if bass.frame_count() != vocals.frame_count():
            raise ValueError(
                f"Invalid length for file {entry.name} 3: "
                f"expecting {bass.frame_count()} but got {vocals.frame_count()}.")


        combined = bass.overlay(drums)

        if bass.frame_count() != combined.frame_count():
            raise ValueError(
                f"Invalid length for file {entry.name} 4: "
                f"expecting {bass.frame_count()} but got {combined.frame_count()}.")
        combined = combined.overlay(vocals)
        if bass.frame_count() != combined.frame_count():
            raise ValueError(
                f"Invalid length for file {entry.name} 5: "
                f"expecting {bass.frame_count()} but got {combined.frame_count()}.")
        combined = combined.overlay(other)
        if bass.frame_count() != combined.frame_count():
            raise ValueError(
                f"Invalid length for file {entry.name} 6: "
                f"expecting {bass.frame_count()} but got {combined.frame_count()}.")
        
        combined.export(f'{entry.path}/mixture.wav', format='wav')
        bass.export(f'{entry.path}/bass.wav', format='wav')
        drums.export(f'{entry.path}/drums.wav', format='wav')
        other.export(f'{entry.path}/other.wav', format='wav')
        vocals.export(f'{entry.path}/vocals.wav', format='wav')
