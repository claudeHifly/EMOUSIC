import copy
from statistics import mean

from music21 import *

dissonance = [1, 2, 6, 8, 10, 11]
# 1: seconda minore
# 2: seconda maggiore
# 6: quarta aumentata
# 8: quinta aumentata
# 10: settima minore
# 11: settima maggiore

tempo_th = 120


def feature_extractor(m):
    tempo = m.metronomeMarkBoundaries()  # funzione da cui ricavare il tempo della battuta (bpm)

    # Inizializzazione contatori
    major = 0  # contatore accordi maggiori
    minor = 0  # contatore accordi minori
    consonant = 0  # contatore accordi consonanti
    dissonant = 0  # contatore accordi dissonanti
    nd = 0  # contatore accordi ne minori ne maggiori
    slow = 0  # somma intervalli di tempo lento
    fast = 0  # somma intervalli di tempo veloce
    avg_oct = 0  # media delle ottave per proprietà pitch
    avg_loudness = 0  # media del loudness
    c_max = None  # nota più alta
    c_min = None  # nota più bassa
    max_loud = 0  # valore massimo loudness
    min_loud = 127  # valore minimo loudness

    ###
    # conta il numero totale di accordi contenuti nella battuta
    num = len(m.getElementsByClass('Chord'))

    ###
    # iterazione sugli intervalli con diversi tempi
    slow, fast = compute_tempo(tempo, slow, fast)

    ###
    # iterazione sugli accordi
    for c in m.getElementsByClass("Chord"):
        if not c.commonName.lower() == "unison":  # si escludono gli accordi formati da una sola nota
            # calcolo delle note massima e minima
            c_min, c_max = compute_min_max(copy.deepcopy(c), c_min, c_max)

            # migliorare il risultato della chordify per la visualizzazione sul pentagramma
            c.closedPosition(inPlace=True)
            # semplificare il risultato della chordify riporatando gli accordi rivolti in accordi base
            c.simplifyEnharmonics(inPlace=True)

            # calcolare l'ottava media in cui è suonato l'accordo
            avg_oct += compute_avg_oct(c.pitches)

            # calcolare l'intensità media
            avg_loudness += compute_avg_loudness(c.volume.velocity)

            # VARIATION IN LOUDNESS
            min_loud, max_loud = compute_var_loudness(c.volume.velocity, min_loud, max_loud)

            # classificare l'accordo come maggiore o minore utilizzando gli attributi commonName e forteClassTn
            minor, major, nd = compute_min_maj(c, minor, major, nd)

            # classificare l'accordo come consonante o dissonante utilizzando gli intervalli prestabiliti
            consonant, dissonant = compute_cons_diss(c.pitches, consonant, dissonant)

    # melodic range
    if c_max is not None and c_min is not None:
        interval_range = compute_interval_range(c_min, c_max)
    else:
        interval_range = 0

    # variation in loudness
    # valore massimo - valore minimo del loudness
    delta_loud = compute_delta_loud(min_loud, max_loud)

    # pitch level
    avg_oct, avg_loudness = compute_avg_oct_loudness(avg_oct, avg_loudness, num)

    p_map = {}  # definizione del dizionario che conterrà le proprietà estrapolate
    p_map['consonant'] = consonant
    p_map['dissonant'] = dissonant
    p_map['loudness'] = avg_loudness
    p_map['var_loudness'] = delta_loud
    p_map['melodic'] = interval_range
    p_map['major'] = major
    p_map['minor'] = minor
    p_map['pitch'] = avg_oct
    p_map['fast'] = fast
    p_map['slow'] = slow
    p_map['timbre'] = None  # TBD
    p_map['round'] = None  # TBD
    p_map['sharp'] = None  # TBD
    p_map['staccato'] = None  # TBD
    p_map['legato'] = None  # TBD
    return p_map


def compute_tempo(tempo, slow, fast):
    for b in tempo:
        if b[2].number < tempo_th:
            slow += b[1] - b[0]  # intervallo di tempo lento
        else:
            fast += b[1] - b[0]  # intervallo di tempo veloce
    return slow, fast


def compute_min_max(c_ordered, c_min, c_max):
    # calcolo delle note massima e minima
    if (c_min is None or c_ordered[0] < c_min):
        c_min = c_ordered[0]
    if (c_max is None or c_ordered[-1] > c_max):
        c_max = c_ordered[-1]
    return c_min, c_max


def compute_avg_oct(pitches):
    return round(mean([p.octave for p in pitches]))


def compute_avg_loudness(velocity):
    return velocity


def compute_var_loudness(velocity, min_loud, max_loud):
    if max_loud < velocity:
        max_loud = velocity
    if min_loud > velocity:
        min_loud = velocity
    return min_loud, max_loud


def compute_min_maj(c, minor, major, nd):
    if 'major' in c.commonName.lower() or 'B' in c.forteClassTn:
        major += 1
    elif 'minor' in c.commonName.lower() or 'A' in c.forteClassTn:
        minor += 1
    else:  # accordo non definito né come maggiore né come minore
        nd += 1
    return minor, major, nd


def compute_cons_diss(notes, consonant, dissonant):
    flag = False
    for i in range(0, len(notes) - 1):
        if flag:
            break
        for j in range(i + 1, len(notes)):
            interv = abs(interval.Interval(noteStart=notes[i], noteEnd=notes[j]).semitones) % 12
            if interv in dissonance:
                dissonant += 1
                flag = True
                break
    if not flag:
        consonant += 1
    return consonant, dissonant


def compute_interval_range(c_min, c_max):
    return interval.Interval(c_min, c_max).semitones


def compute_delta_loud(min_loud, max_loud):
    return max_loud - min_loud


def compute_avg_oct_loudness(avg_oct, avg_loudness, num):
    try:
        return round(avg_oct / num), round(avg_loudness / num)
    except ZeroDivisionError:
        return 0, 0
