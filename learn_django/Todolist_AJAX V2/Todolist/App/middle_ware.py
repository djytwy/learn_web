from django.contrib.gis.geoip2 import GeoIP2
import pytz


class CheckSourceMidderware(object):
    def process_request(self, request):
        from_source = request.META['HTTP_USER_AGENT']
        if 'Mozilla/4.0' in from_source:
            request.session['from_brower'] = 'IE8'
        else:
            request.session['from_brower'] = 'not IE8'
        print(request.session['from_brower'])
