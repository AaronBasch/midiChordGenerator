# generate chord shapes of a chord progression.
# have top note randomly choose higher or lower.
# most of the time do counterpoint for the bass note.
# orrr
# have all notes within chord be activated and use a range of notes to turn on.
# fluctuate range in some kind of pattern.

import random
from midiutil import MIDIFile

keyboard = ['a','a#', 'b', 'c', 'c#', 'd','d#', 'e', 'f', 'f#', 'g', 'g#']
chords =    {
            'maj':[0,4,7],
            'min':[0,3,7],
            'dim': [0,3,6],
            'aug': [0,4,8]
            }

testProgression = ['cmaj', 'amin', 'fmaj', 'gmaj']
testProgressionNotes = []
for chord in testProgression:
    chordValues = []
    key = keyboard.index(chord[0])
    if chord[1] == '#':
        key += 1
        chordType = chord[2:]
    else:
        chordType = chord[1:]
    for num in chords[chordType]:
        chordValues.append(keyboard[(num + key)%12])
    testProgressionNotes.append(chordValues)

# print(testProgressionNotes)

# create progression list of lists. then iterate through and
# use addNote method: MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

# Midi note numbers are from 21(A0) to 108(C8)


octave   = 4
track    = 0
channel  = 0
time     = 0    # In beats
duration = 4    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)


for chordNotes in testProgressionNotes:
    for note in chordNotes:
        pitch = keyboard.index(note) + 21 + octave*12
        MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time += 4
with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
