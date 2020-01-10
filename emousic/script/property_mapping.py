HARM_PERC = 66.67 # HARM_PERC = 50
LOUD_TRESH_MAX = 69  # LOUD_TRESH_MAX = 63
LOUD_TRESH_MIN = 57  # LOUD_TRESH_MIN = 63
VAR_LOUD_TRESH_MAX = 69  # VAR_LOUD_TRESH_MAX = 63
VAR_LOUD_TRESH_MIN = 57  # VAR_LOUD_TRESH_MIN = 63
MELO_TRESH_MAX = 16  # MELO_TRESH_MAX = 24
MELO_TRESH_MIN = 16  # MELO_TRESH_MIN = 24
MODE_PERC = 66.67  # MODE_PERC = 50
PITC_TRESH_MAX = 4
PITC_TRESH_MIN = 4
TEMP_PERC = 66.67  # TEMP_PERC = 50
TIMB_XXX = None  # TBD
AMPL_XXX = None  # TBD
ARTI_PERC = 50  # TBD


def create_map(property_dict):
    feature_map = {}  # definizione del dizionario che conterrà le proprietà estrapolate
    feature_map['amplitude'] = ""
    feature_map['articulation'] = ""
    feature_map['harmony'] = ""
    feature_map['loudness'] = ""
    feature_map['var_loud'] = ""
    feature_map['melodic'] = ""
    feature_map['mode'] = ""
    feature_map['pitch'] = ""
    feature_map['tempo'] = ""
    feature_map['timbre'] = ""

    # controllo su AMPL da implementare
    # implementare a tutte le perc il controllo sulla divisione per zero
    # if (property_dict["staccato"] / (property_dict["staccato"] + property_dict["legato"])) * 100 >= ARTI_PERC:
    #     feature_map["articulation"] = "staccato"
    # elif (property_dict["legato"] / (property_dict["staccato"] + property_dict["legato"])) * 100 >= ARTI_PERC:
    #     feature_map["articulation"] = "legato"

    try:
        if (property_dict["consonant"] / (property_dict["consonant"] + property_dict["dissonant"])) * 100 >= HARM_PERC:
            feature_map["harmony"] = "consonant"
        elif (property_dict["dissonant"] / (property_dict["consonant"] + property_dict["dissonant"])) * 100 >= HARM_PERC:
            feature_map["harmony"] = "dissonant"
    except ZeroDivisionError:
        pass

    if property_dict["loudness"] >= LOUD_TRESH_MAX:
        feature_map["loudness"] = "loud"
    elif property_dict["loudness"] <= LOUD_TRESH_MIN:
        feature_map["loudness"] = "soft"

    if property_dict["var_loudness"] >= VAR_LOUD_TRESH_MAX:
        feature_map["var_loud"] = "large"
    elif property_dict["var_loudness"] <= VAR_LOUD_TRESH_MIN:
        feature_map["var_loud"] = "small"

    if property_dict["melodic"] > MELO_TRESH_MAX:
        feature_map["melodic"] = "wide"
    elif property_dict["melodic"] <= MELO_TRESH_MIN:
        feature_map["melodic"] = "narrow"

    try:
        if (property_dict["major"] / (property_dict["major"] + property_dict["minor"])) * 100 >= MODE_PERC:
            feature_map["mode"] = "major"
        elif (property_dict["minor"] / (property_dict["major"] + property_dict["minor"])) * 100 >= MODE_PERC:
            feature_map["mode"] = "minor"
    except ZeroDivisionError:
        pass

    if property_dict["pitch"] > PITC_TRESH_MAX:
        feature_map["pitch"] = "high"
    elif property_dict["pitch"] <= PITC_TRESH_MIN:
        feature_map["pitch"] = "low"

    try:
        if (property_dict["fast"] / (property_dict["fast"] + property_dict["slow"])) * 100 >= TEMP_PERC:
            feature_map["tempo"] = "fast"
        elif (property_dict["slow"] / (property_dict["fast"] + property_dict["slow"])) * 100 >= MODE_PERC:
            feature_map["tempo"] = "slow"
    except ZeroDivisionError:
        pass

    # controllo su TIMB da implementare

    return feature_map
