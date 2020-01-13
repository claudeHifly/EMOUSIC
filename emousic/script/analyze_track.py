from .average_criteria import *
from .average_criteria_with_zero import *
from .emotion_mapping import *
from .feature_extractor import *
from .majority_criteria import *
from .property_mapping import *

approach_criteria = []
approach_criteria.append(compute_emotion_with_zero)
approach_criteria.append(compute_emotion_without_zero)
approach_criteria.append(compute_emotion_majority)


def analyze_track(stream_chordified, approach):
    for m in stream_chordified.measures(0, None):
        p_map = feature_extractor(m)
        print("\nstep 1: P_map", p_map)

        feature_map = create_map(p_map)
        print("\nstep 2: feature_map", feature_map)

        test_dict = mapping(feature_map)
        print("\nstep 3: test_dict", test_dict)

        sentics_test = approach_criteria[approach](test_dict)
        print("\nstep 4 approccio:", approach, "\nsentic test:", sentics_test)

        yield (
            m.measureNumber, sentics_test['pleasantness'][0], sentics_test['attention'][0],
            sentics_test['sensitivity'][0],
            sentics_test['aptitude'][0], sentics_test['moodtag_1'], sentics_test['moodtag_2'], sentics_test['polarity'])


def get_n_measures(file):
    mf = midi.MidiFile()
    mf.open(file)
    mf.read()
    mfTS = midi.translate.midiFileToStream(mf)
    mfTS = mfTS.chordify()  # funzione che compatta tutte le Part della traccia in un'unica Part
    n = len(mfTS.measures(0, None))
    print('No. of measures:', n)
    return mfTS, n
