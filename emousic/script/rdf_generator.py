class rdfGenerator:

    def __init__(self, song_name):
        self.song_name = song_name
        self.file = self._create_file()

    def _create_file(self):
        base = ".\emousic\static\\rdf\\"
        file_name = base + self.song_name + ".xml"
        return open(file_name, 'w+')

    def rdf_init(self):
        rdf_string = '<?xml version="1.0"?>\n' \
                     '<rdf:RDF xmlns:rdf="http://w3.org/1999/02/22-rdf-syntax-ns#">\n'
        self.file.write(rdf_string)

    def rdf(self, pleasantness, attention, sensitivity, aptitude, moodtag_1, moodtag_2, polarity, battuta_iniziale=None,
            battuta_finale=None):
        if (battuta_iniziale is not None) and (battuta_finale is not None):
            battuta = "_" + str(battuta_iniziale) + "_" + str(battuta_finale)
        elif (battuta_iniziale is None) and (battuta_finale is None):
            battuta = ""
        elif (battuta_iniziale is not None) and (battuta_finale is None):
            battuta = "_" + str(battuta_iniziale)

        if polarity > 0:
            polarity_value = "positive"
        elif polarity < 0:
            polarity_value = "negative"
        else:
            polarity_value = "neutral"

        rdf_string = '  <rdf:Description rdf:about="http://senticnote.net/midi/' + self.song_name + battuta + '">\n' \
                                                                                                              '      <rdf:type rdf:resource="http://senticnote.net/midi/"/>\n' \
                                                                                                              '      <rdf:type rdf:resource="http://senticnote.net/midi/moodtag/"/>\n' \
                                                                                                              '      <text xmlns="http://senticnote.net">' + self.song_name + battuta + '</text>\n' \
                                                                                                                                                                                        '      <sentics xmlns="http://senticnote.net">\n' \
                                                                                                                                                                                        '          <pleasantness xmlns="http://senticnote.net" rdf:datatype="http://w3.org/2001/XMLSchema#float">' + str(
            pleasantness) + '</pleasantness>\n' \
                            '          <attention xmlns="http://senticnote.net" rdf:datatype="http://w3.org/2001/XMLSchema#float">' + str(
            attention) + '</attention>\n' \
                         '          <sensitivity xmlns="http://senticnote.net" rdf:datatype="http://w3.org/2001/XMLSchema#float">' + str(
            sensitivity) + '</sensitivity>\n' \
                           '          <aptitude xmlns="http://senticnote.net" rdf:datatype="http://w3.org/2001/XMLSchema#float">' + str(
            aptitude) + '</aptitude>\n' \
                        '      </sentics>\n' \
                        '      <moodtags xmlns="http://senticnote.net">\n' \
                        '          <moodtag xmlns="http://senticnote.net" rdf:resource="http://senticnote.net/midi/moodtag/' + moodtag_1 + '"/>\n' \
                                                                                                                                           '          <moodtag xmlns="http://senticnote.net" rdf:resource="http://senticnote.net/midi/moodtag/' + moodtag_2 + '"/>\n' \
                                                                                                                                                                                                                                                              '      </moodtags>\n' \
                                                                                                                                                                                                                                                              '      <polarity xmlns="http://senticnote.net">\n' \
                                                                                                                                                                                                                                                              '          <value xmlns="http://senticnote.net">' + polarity_value + '</value>\n' \
                                                                                                                                                                                                                                                                                                                                   '          <intensity xmlns="http://senticnote.net" rdf:datatype="http://w3.org/2001/XMLSchema#float">' + str(
            polarity) + '</intensity>\n' \
                        '      </polarity>\n' \
                        '  </rdf:Description>\n'
        self.file.write(rdf_string)

    def rdf_conclusion(self):
        rdf_string = '</rdf:RDF>'
        self.file.write(rdf_string)
        self.file.close()

    def rdf_to_string(self):
        file_name = ".\emousic\static\\rdf\\" + self.song_name + ".xml"
        f = open(file_name, 'r')
        rdf_str = f.read()
        f.close()
        return rdf_str
