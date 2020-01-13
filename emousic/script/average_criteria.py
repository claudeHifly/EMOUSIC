from senticnet.senticnet import SenticNet

from .moodtag_dictionary import *

sn = SenticNet()


def compute_emotion_without_zero(emotion_occurrences):
    sentics_dict = {}
    sentics_dict['pleasantness'] = [0, 0]
    sentics_dict['attention'] = [0, 0]
    sentics_dict['sensitivity'] = [0, 0]
    sentics_dict['aptitude'] = [0, 0]

    for emotion in emotion_occurrences.keys():
        n = int(emotion_occurrences[emotion])
        sentic_level = sn.sentics(emotion)
        for k in sentic_level:
            if sentic_level[k] != '0':
                sentics_dict[k][0] += float(sentic_level[k]) * n
                sentics_dict[k][1] += n

    for key in sentics_dict.keys():
        try:
            sentics_dict[key][0] /= sentics_dict[key][1]
        except:
            sentics_dict[key][0] = 0
    mood_1, mood_2 = get_moodtags(sentics_dict)
    sentics_dict['moodtag_1'] = mood_1
    sentics_dict['moodtag_2'] = mood_2
    sentics_dict['polarity'] = (sentics_dict['pleasantness'][0] - abs(sentics_dict['sensitivity'][0]) + abs(
        sentics_dict['attention'][0]) + sentics_dict['aptitude'][0]) / 3

    return sentics_dict


def get_moodtags(sentics_dict):
    n_1, n_2 = greatest(sentics_dict)
    index = get_index(sentics_dict[n_1][0])
    m_1 = moodtags[n_1][index]
    index = get_index(sentics_dict[n_2][0])
    m_2 = moodtags[n_2][index]
    return m_1, m_2


def get_index(n):
    index = int(n / 0.33 + 3)
    if (index > 5):
        index = 5
    return index


def greatest(sentics_dict):
    max_1 = None, -2
    max_2 = None, -3
    for emotion in sentics_dict:
        if abs(sentics_dict[emotion][0]) > max_1[1]:
            max_2 = max_1
            max_1 = emotion, abs(sentics_dict[emotion][0])
        elif abs(sentics_dict[emotion][0]) > max_2[1]:
            max_2 = emotion, abs(sentics_dict[emotion][0])
    return max_1[0], max_2[0]
