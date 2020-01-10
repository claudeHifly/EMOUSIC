from music21 import *
from .emotion_mapping import *
from .average_criteria import *
from .property_mapping import *
from .average_criteria_with_zero import *
from .majority_criteria import *
from .feature_extractor import *



approach_criteria = []
approach_criteria.append(compute_emotion_with_zero)
approach_criteria.append(compute_emotion_without_zero)
approach_criteria.append(compute_emotion_majority)

def analyze_track(stream_chordified, approach):
    #
    # print("analyze_track", type(file))
    #
    # m1 = 0
    # m2 = None
    #
    # #file = "./midi_files/astrodelciel.mid"
    #
    # #ricevo in input un file di tipo midi
    # mf = midi.MidiFile()
    # mf.open(file)
    # mf.read()
    # print("INIZIO FILE TO STREAM")
    # f = midi.translate.midiFileToStream(mf)
    # print("INIZIO CHORDIFY")
    # #f = converter.parse(file)  # converte la traccia audio MIDI in uno Score
    # f = f.chordify()  # funzione che compatta tutte le Part della traccia in un'unica Part


    for m in stream_chordified.measures(0, None):
        p_map = feature_extractor(m)
        print("\nstep 1: P_map", p_map)

        feature_map = create_map(p_map)
        print("\nstep 2: feature_map", feature_map)

        test_dict = mapping(feature_map)
        print("\nstep 3: test_dict", test_dict)


        sentics_test = approach_criteria[approach](test_dict)
        print("\nstep 4 approccio:", approach, "\nsentic test:", sentics_test)

        # sentics_test_with_zero = compute_emotion_with_zero(test_dict)
        # print("\nstep 4-b: CON ZERI", sentics_test_with_zero)
        #
        # sentics_test_majority = compute_emotion_majority(test_dict)
        # print("\nstep 4-C: MAJORITY", sentics_test_majority)

        # rdf = rdfGenerator(file)
        # rdf.rdf_init()
        # rdf.rdf(sentics_test['pleasantness'][0], sentics_test['attention'][0], sentics_test['sensitivity'][0], sentics_test['aptitude'][0], sentics_test['moodtag_1'], sentics_test['moodtag_2'], sentics_test['polarity'])
        # rdf.rdf_conclusion()
        yield (m.measureNumber, sentics_test['pleasantness'][0], sentics_test['attention'][0], sentics_test['sensitivity'][0], sentics_test['aptitude'][0], sentics_test['moodtag_1'], sentics_test['moodtag_2'], sentics_test['polarity'])

def get_n_measures(file):
    #print("get_n_measure", type(file))
    mf = midi.MidiFile()
    mf.open(file)
    mf.read()
    #print("INIZIO FILE TO STREAM")
    mfTS= midi.translate.midiFileToStream(mf)
    #print("INIZIO CHORDIFY")
    mfTS = mfTS.chordify()  # funzione che compatta tutte le Part della traccia in un'unica Part
    n = len(mfTS.measures(0, None))
    print('No. of measures:', n)
    return mfTS, n
