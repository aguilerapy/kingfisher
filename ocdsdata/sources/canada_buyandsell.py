from ocdsdata.base import Fetcher

class CanadaBuyAndSellFetcher(Fetcher):
    publisher_name = 'Buy And Sell'
    url = 'https://buyandsell.gc.ca'

    def __init__(self, base_dir, remove_dir=False, output_directory=None):
        super().__init__(base_dir, remove_dir=remove_dir, output_directory=output_directory)

    def gather_all_download_urls(self):
        return [
            [
                'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-13-14.json',
                '2013-14.json',
                'release_package',
                []
            ],
            [
                'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-14-15.json',
                '2014-15.json',
                'release_package',
                []
            ],
            [
                'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-15-16.json',
                '2015-16.json',
                'release_package',
                []
            ],
            [
                'https://buyandsell.gc.ca/cds/public/ocds/tpsgc-pwgsc_ocds_EF-FY-16-17.json',
                '2016-17.json',
                'release_package',
                []
            ],
        ]
