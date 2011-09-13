import re
import pprint
class ShowHeadersMiddleware(object):
    def process_request(self, request):
        print '-' * 100

        regex = re.compile('^HTTP_')
        headers = dict((regex.sub('', header), value) for (header, value)
               in request.META.items() if header.startswith('HTTP_'))
        pp = pprint.PrettyPrinter()
        pp.pprint(request.META)

        print '-' * 100
  