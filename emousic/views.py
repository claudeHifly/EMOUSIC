import base64
import shutil
from datetime import timedelta

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .forms import *
from .models import *
from .script.analyze_track import *
from .script.final_test_compatto import *
from .script.rdf_generator import *


def index(request):
    Track.objects.all().filter(pub_date__lt=timezone.now() - timedelta(minutes=15)).delete()
    shutil.rmtree(".\emousic\static\\rdf\\")
    os.mkdir(".\emousic\static\\rdf\\")
    if request.method == "POST":
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Track(file=request.FILES['file'], name=str(request.FILES['file']))
            instance.save()
            midi_cordified, tot_measure = get_n_measures(instance.file)
            instance.tot_measure = tot_measure
            instance.save()
            for m in analyze_track(midi_cordified, int(request.POST['approach'])):
                print(m[0])
                measure = Measure(track=instance, number=m[0], pleasantness=m[1], attention=m[2], sensitivity=m[3],
                                  aptitude=m[4],
                                  moodtag_1=m[5], moodtag_2=m[6], polarity=int(m[7]), polarity_value=m[7])
                measure.save()
            measure_list = Measure.objects.all().filter(track=instance)
            measure_list_json = serializers.serialize('json', measure_list)

            file = open(instance.file.path, 'rb')
            reader = file.read()
            base64_encoded = base64.b64encode(reader)
            base64_encoded = "data:audio/midi;base64," + str(base64_encoded, "utf-8")
            file.close()

            return render(request, 'index.html',
                          {'form': form, 'track_id': instance.pk,
                           'measures': instance.tot_measure, 'measure_list': measure_list_json,
                           'track_name': instance.name, 'song': base64_encoded})
    else:
        form = TrackForm()
    return render(request, 'index.html', {'form': form})


def rdf(request):
    if request.method == "POST":
        min = int(request.POST['min_measure'])
        max = int(request.POST['max_measure'])
        approach = int(request.POST['checked_approach'])
        track_id = int(request.POST['track_id'])
        measure_list = Measure.objects.all().filter(track=track_id, number__gte=min, number__lte=max)
        compact_tuple = result_compatto(measure_list, approach)
        track = Track.objects.all().filter(pk=track_id)[0]
        rdf = rdfGenerator(track.name.split(".mid")[0])
        rdf.rdf_init()
        if min == 1 and max == track.tot_measure:
            rdf.rdf(compact_tuple[0], compact_tuple[1], compact_tuple[2], compact_tuple[3], compact_tuple[4],
                    compact_tuple[5], compact_tuple[6])
        else:
            rdf.rdf(compact_tuple[0], compact_tuple[1], compact_tuple[2], compact_tuple[3], compact_tuple[4],
                    compact_tuple[5], compact_tuple[6], min, max)
        for m in measure_list:
            rdf.rdf(m.pleasantness, m.attention, m.sensitivity, m.aptitude, m.moodtag_1, m.moodtag_2, m.polarity_value,
                    m.number)
        rdf.rdf_conclusion()
        rdf = rdf.rdf_to_string()
    else:
        pass
    return render(request, 'rdf.html', {'min': min, 'max': max, 'rdf': rdf,
                                        'xml': track.name.split(".mid")[0] + ".xml"})


def get_moodtags(request):
    track_id = request.GET['track_id']
    min = request.GET['min']
    max = request.GET['max']
    approach = request.GET['approach']
    measure_list = Measure.objects.all().filter(track=track_id, number__gte=min, number__lte=max)
    compact_tuple = result_compatto(measure_list, int(approach))
    data = {
        'compact_tuple': compact_tuple
    }
    return JsonResponse(data)


def read_wildwebmidi(request):
    f = open('emousic/static/wildwebmidi.data', 'rb')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
