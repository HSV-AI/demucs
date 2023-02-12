from pydub import AudioSegment

base = '/workspaces/demucs/data/moisesdb23_labelnoise_v1.0/ff486935-7ce2-4e23-8908-0ff5fcc50856'
bass = AudioSegment.from_file(f'{base}/bass.wav')
drums = AudioSegment.from_file(f'{base}/drums.wav')
other = AudioSegment.from_file(f'{base}/other.wav')
vocals = AudioSegment.from_file(f'{base}/vocals.wav')

combined = bass.overlay(drums)

combined.export(f'{base}/mix.wav', format='wav')