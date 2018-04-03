from ocdsdata.base import Source
import requests


class CanadaMontrealSource(Source):
    publisher_name = 'Montreal'
    url = 'https://ville.montreal.qc.ca'
    source_id = 'canada_montreal'

    def gather_all_download_urls(self):

        if self.sample:
            return [{
                'url': 'https://ville.montreal.qc.ca/vuesurlescontrats/api/releases.json?limit=1000&offset=0',
                'filename': 'offset0.json',
                'data_type': 'release_package',
                'errors': []
            }]


        url = 'https://ville.montreal.qc.ca/vuesurlescontrats/api/releases.json?limit=1'
        r = requests.get(url)
        data = r.json()
        total = data['meta']['count']
        offset = 0
        out = []
        limit = 10000
        while offset < total:
            out.append({
                'url': 'https://ville.montreal.qc.ca/vuesurlescontrats/api/releases.json?limit=%d&offset=%d' % (limit, offset),
                'filename': 'offset%d.json' % offset,
                'data_type': 'release_package',
                'errors': []
            })
            offset += limit
        return out
