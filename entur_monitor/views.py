from django.shortcuts import render, HttpResponse
# from entur_api import journey_planner_utils
from entur_api.journey_planner_utils import JourneyPlannerUtils

entur = JourneyPlannerUtils('datagutten-sis-monitor')
# Create your views here.


def monitor2(request, stop, quays1=None, quays2=None, name1='', name2='', 
             debug=False):
    if quays1 is None:
        quays1 = []
    if quays2 is None:
        quays2 = []
    print('Left')
    departures1 = entur.filter_departures(stop, quays=quays1)
    # pprint(depatures1)
    # print(departures1[0])
    print('Right')
    departures2 = entur.filter_departures(stop, quays=quays2)
    # print(departures2[0])
    return render(request, 'monitor/monitor2.html',
                  {'departures1': departures1,
                   'departures2': departures2,
                   'name1': name1,
                   'name2': name2,
                   'stop': stop,
                   'quays1': quays1,
                   'quays2': quays2,
                   'debug': debug}
                  )


def monitor2_url(request, stop, left, right, left_name='', right_name=''):
    quays1 = left.split(',')
    quays2 = right.split(',')
    return monitor2(request, stop, quays1, quays2, left_name, right_name)


def monitor2_test(request, debug=False):
    return monitor2(request, 'NSR:StopPlace:58381', 
                    ['NSR:Quay:8027', 'NSR:Quay:8028'], 
                    ['NSR:Quay:8050', 'NSR:Quay:8051'],
                    'Majorstua (Tunnelbane)', 'Majorstua (Sporvogn)', 
                    debug=debug)


def monitor2_test_debug(request):
    return monitor2(request,
                    stop='NSR:StopPlace:58381',
                    quays1=['NSR:Quay:8027', 'NSR:Quay:8028'],
                    name1='Majorstua (Tunnelbane)',
                    name2='Majorstua (Alt)',
                    debug=True)


def clock(request):
    from datetime import datetime
    time = datetime.now().strftime('%H:%M')
    return HttpResponse(time)


def refresh(request, stop, quays=''):
    quays = quays.split(',')
    # return HttpResponse(quays[0])

    departures_dict = entur.filter_departures(stop, quays=quays)
    return render(request, 'monitor/departure_column.html', 
                  {'departures': departures_dict})
