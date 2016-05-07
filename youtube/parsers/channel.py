"""

"""
__author__ = 'Saleem Latif'

from youtube.parsers.parser import BaseParser, ThumbnailsParser
from youtube.decorators import default_on_error


class ChannelsResponseParser(BaseParser):
    """

    """
    @property
    @default_on_error(KeyError, '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error(KeyError, '')
    def kind(self):
        return self.result['kind']

    @property
    @default_on_error(KeyError, None)
    def next_page_token(self):
        return self.result['nextPageToken']

    @property
    @default_on_error(KeyError, 1)
    def total_results(self):
        return self.result['pageInfo']['totalResults']

    @property
    @default_on_error(KeyError, 1)
    def results_per_page(self):
        return self.result['pageInfo']['resultsPerPage']

    @property
    def items(self):
        for item in self.result['items']:
            yield ChannelItemParser(item)


class ChannelItemParser(BaseParser):
    """
    Parser for Youtube API's search result,
    more info about videos api https://developers.google.com/youtube/v3/docs/playlists/list
    """
    @property
    @default_on_error(KeyError, '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error(KeyError, '')
    def kind(self):
        return self.result['kind']

    @property
    @default_on_error(KeyError, '')
    def id(self):
        return self.result['id']

    @property
    @default_on_error(KeyError, '')
    def title(self):
        return self.result['snippet']['title']

    @property
    @default_on_error(KeyError, '')
    def description(self):
        return self.result['snippet']['description']

    @property
    @default_on_error(KeyError, '')
    def published_at(self):
        return self.result['snippet']['publishedAt']

    @property
    @default_on_error(KeyError, '')
    def custom_url(self):
        return self.result['snippet']['customUrl']

    @property
    @default_on_error(KeyError, '')
    def thumbnails(self):
        return ThumbnailsParser(self.result['snippet']['thumbnails'])
