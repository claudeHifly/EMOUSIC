
from emousic.script.analyze_track import *
from emousic.script.rdf_generator import *
from emousic.script.final_test_compatto import *




midi_cordified, tot_measure = get_n_measures("./cant_take.mid")
approach=2

for m in analyze_track(midi_cordified, approach):
    print (m)

# min = 0
# max = 1
# measure_list = Measure.objects.all().filter(track=track.id, number__gte=min, number__lte=max)
# compact_tuple = result_compatto(measure_list, approach)
# rdf = rdfGenerator(track.name.split(".mid")[0])
# rdf.rdf_init()
# if min == 1 and max == track.tot_measure:
#     rdf.rdf(compact_tuple[0], compact_tuple[1], compact_tuple[2], compact_tuple[3], compact_tuple[4],
#         compact_tuple[5], compact_tuple[6])
# else:
#     rdf.rdf(compact_tuple[0], compact_tuple[1], compact_tuple[2], compact_tuple[3], compact_tuple[4],
#             compact_tuple[5], compact_tuple[6], min, max)
# for m in measure_list:
#     rdf.rdf(m.pleasantness, m.attention, m.sensitivity, m.aptitude, m.moodtag_1, m.moodtag_2, m.polarity_value,
#             m.number)
# rdf.rdf_conclusion()
# rdf = rdf.rdf_to_string()
