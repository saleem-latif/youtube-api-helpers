__author__ = 'Saleem Latif'

from httplib import ResponseNotReady, IncompleteRead
from httplib2 import FailedToDecompressContent
from googleapiclient.errors import HttpError

from youtube.api.base import APIBase
from youtube.parsers.search import SearchResponse
from youtube.models.search import SearchResult

from youtube.decorators import default_on_error


class Search(APIBase):
    """
    This class is responsible for searching youtube content.
    """
    def __init__(self, youtube, **kwargs):
        self.reset_params()
        self.params.update(kwargs)
        super(Search, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        result = SearchResponse(self.fetch(**self.params))
        return SearchResult.from_search_result(result)

    @default_on_error(
        (
            ValueError, UnicodeDecodeError, AttributeError, IncompleteRead,
            ResponseNotReady, HttpError, FailedToDecompressContent,
        ),
        {}
    )
    def fetch(self, **params):
        self.reset_params()
        return self.youtube.api.search().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))

    @property
    def videos(self):
        self.params.update(type='video')
        return self

    @property
    def channels(self):
        self.params.update(type='channel')
        return self

    @property
    def playlist(self):
        self.params.update(type='playlist')
        return self
