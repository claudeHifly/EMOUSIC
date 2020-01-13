from senticnet.senticnet import SenticNet

sn = SenticNet()


def compute_emotion_majority(emotion_occurrences):
    sentics_dict = {}
    sentics_dict['pleasantness'] = [0, 0]
    sentics_dict['attention'] = [0, 0]
    sentics_dict['sensitivity'] = [0, 0]
    sentics_dict['aptitude'] = [0, 0]

    max_1 = None, -2
    max_2 = None, -3
    for emotion in emotion_occurrences.keys():
        if emotion_occurrences[emotion] > max_1[1]:
            max_2 = max_1
            max_1 = emotion, emotion_occurrences[emotion]
        elif emotion_occurrences[emotion] > max_2[1]:
            max_2 = emotion, emotion_occurrences[emotion]

    emotion_1 = sn.sentics(max_1[0])
    emotion_2 = sn.sentics(max_2[0])

    for k in emotion_1:
        if float(emotion_1[k]) == 0 or float(emotion_2[k]) == 0:
            sentics_dict[k][0] = float(emotion_1[k]) + float(emotion_2[k])
        else:
            sentics_dict[k][0] = (float(emotion_1[k]) + float(emotion_2[k])) / 2

    sentics_dict['moodtag_1'] = "#" + max_1[0]
    sentics_dict['moodtag_2'] = "#" + max_2[0]
    sentics_dict['polarity'] = (sentics_dict['pleasantness'][0] - abs(sentics_dict['sensitivity'][0]) + abs(
        sentics_dict['attention'][0]) + sentics_dict['aptitude'][0]) / 3

    return sentics_dict
