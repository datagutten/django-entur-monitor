from django.shortcuts import render, HttpResponse
from entur_api import EnturJourneyPlannerUtils

entur = EnturJourneyPlannerUtils('datagutten-sis-monitor')
# Create your views here.


def monitor2(request, stop, quays1=None, quays2=None, name1='', name2='',
             debug=False):
    if quays1 is None:
        quays1 = []
    if quays2 is None:
        quays2 = []
    limit = int(request.GET.get('limit', 20))
    departures1 = entur.filter_departures(stop, quays=quays1, limit=limit)
    departures2 = entur.filter_departures(stop, quays=quays2, limit=limit)

    return render(request, 'monitor/monitor2.html',
                  {'departures1': departures1,
                   'departures2': departures2,
                   'name1': name1,
                   'name2': name2,
                   'stop': stop,
                   'quays1': quays1,
                   'quays2': quays2,
                   'limit': limit,
                   'debug': debug}
                  )


def monitor1(request, stop):
    departures = entur.stop_departures_app(stop)
    departures = departures['data']['stopPlace']['estimatedCalls']
    return render(request, 'monitor/monitor1.html', {'departures': departures, 'stop': stop, 'limit': 20})


def monitor2_url(request, stop, left, right, left_name='', right_name=''):
    quays1 = left.split(',')
    quays2 = right.split(',')
    return monitor2(request, stop, quays1, quays2, left_name, right_name)


def monitor2_stops(request, stop1, stop2):
    stop1_info = entur.stop_info(stop1)
    stop2_info = entur.stop_info(stop2)
    departures1 = entur.stop_departures_app(stop1)

    departures2 = entur.stop_departures_app(stop2)
    limit = int(request.GET.get('limit', 20))
    debug = request.GET.get('debug', 'false')
    return render(request, 'monitor/monitor2.html',
                  {'departures1': departures1['data']['stopPlace']['estimatedCalls'],
                   'departures2': departures2['data']['stopPlace']['estimatedCalls'],
                   'stop1_info': stop1_info['data']['stopPlace'],
                   'stop2_info': stop2_info['data']['stopPlace'],
                   'stop1': stop1,
                   'stop2': stop2,
                   'limit': limit,
                   'debug': debug}
                  )


def monitor2_test(request, debug=False):
    return monitor2(request, 'NSR:StopPlace:58381',
                    ['NSR:Quay:8027', 'NSR:Quay:8028'],
                    ['NSR:Quay:8050', 'NSR:Quay:8051'],
                    'Majorstua (Tunnelbane)', 'Majorstua (Sporvogn)',
                    debug=debug)


def monitor2_test_debug(request):
    departures = entur.filter_departures(stop='NSR:StopPlace:58381', limit=None)
    return render(request, 'monitor/departure_column.html', {'departures': departures, 'debug': True})

    """return monitor2(request,
                    stop=,
                    quays1=['NSR:Quay:8027', 'NSR:Quay:8028'],
                    quays2=['all'],
                    name1='Majorstua (Tunnelbane)',
                    name2='Majorstua (Alt)',
                    debug=True)"""


def clock(request):
    from datetime import datetime
    time = datetime.now().strftime('%H:%M')
    return HttpResponse(time)


def refresh(request, stop, quays='all'):
    if quays == 'all':
        quays = None
    else:
        quays = quays.split(',')

    limit = int(request.GET.get('limit', None))

    departures_dict = entur.filter_departures(stop, quays=quays, limit=limit)
    return render(request, 'monitor/departure_column.html',
                  {'departures': departures_dict})


def departure_limit(request):
    # departure height: 50px
    # header: 47px+20
    # 140px
    # table header: 26px
    # departures = screen height - 140 - 26 / 50
    from math import floor
    departure_height = int(request.GET['departure_height'])
    top_offset = int(request.GET['top_offset'])
    screen_height = int(request.GET['screen_height'])

    limit = floor((screen_height - top_offset) / departure_height)
    return HttpResponse(limit)


def find_limit(request):
    return render(request, 'monitor/find_limit.html')
