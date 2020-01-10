from .majority_criteria import *


def compute_result_majority(final_list):
    majority_dict = {}

    for e in final_list:
        emotion1 = str(e.moodtag_1)[1:]  # per rimuovere il #
        emotion2 = str(e.moodtag_2)[1:]  # per rimuovere il #

        try:
            majority_dict[emotion1] += 1  # se emozione già presente, incrementa il contatore delle occorrenze
        except:
            majority_dict[emotion1] = 1  # altrimenti aggiungila al dizionario

        try:
            majority_dict[emotion2] += 1
        except:
            majority_dict[emotion2] = 1

    #print(majority_dict)

    sentics_track = compute_emotion_majority(majority_dict)

    final_sentics = (round(sentics_track['pleasantness'][0], 3),
                     round(sentics_track['attention'][0], 3),
                     round(sentics_track['sensitivity'][0], 3),
                     round(sentics_track['aptitude'][0], 3),
                     sentics_track['moodtag_1'],
                     sentics_track['moodtag_2'],
                     round(sentics_track['polarity'], 3))

    return final_sentics
