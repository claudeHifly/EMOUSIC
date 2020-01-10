from .senticnote import senticnote

def mapping(feature_map):
    occurences = {}
    for k in feature_map:
        if feature_map[k] != "":
            entries = senticnote[feature_map[k]]
            for e in entries:
                try:
                    occurences[e] += 1
                except:
                    occurences[e] = 1

    return occurences


