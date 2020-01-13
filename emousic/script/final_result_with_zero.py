from .average_criteria_with_zero import *


def compute_result_with_zero(final_list):
    sentics_track = {}
    sentics_track['pleasantness'] = [0, 0]
    sentics_track['attention'] = [0, 0]
    sentics_track['sensitivity'] = [0, 0]
    sentics_track['aptitude'] = [0, 0]
    occurrencies = len(final_list)
    for e in final_list:
        sentics_track['pleasantness'][0] += e.pleasantness
        sentics_track['attention'][0] += e.attention
        sentics_track['sensitivity'][0] += e.sensitivity
        sentics_track['aptitude'][0] += e.aptitude

    sentics_track['pleasantness'][0] /= occurrencies
    sentics_track['attention'][0] /= occurrencies
    sentics_track['sensitivity'][0] /= occurrencies
    sentics_track['aptitude'][0] /= occurrencies

    mood_1, mood_2 = get_moodtags(sentics_track)

    sentics_track['moodtag_1'] = mood_1
    sentics_track['moodtag_2'] = mood_2
    sentics_track['polarity'] = (sentics_track['pleasantness'][0] - abs(sentics_track['sensitivity'][0]) + abs(
        sentics_track['attention'][0]) + sentics_track['aptitude'][0]) / 3

    final_sentics = (round(sentics_track['pleasantness'][0], 3),
                     round(sentics_track['attention'][0], 3),
                     round(sentics_track['sensitivity'][0], 3),
                     round(sentics_track['aptitude'][0], 3),
                     sentics_track['moodtag_1'],
                     sentics_track['moodtag_2'],
                     round(sentics_track['polarity'], 3))

    return final_sentics
