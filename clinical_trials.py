#!/usr/bin/env python

"""
Python wrapper for the Clincal Trials API.

Clinical Trials Documentation:  http://clinicaltrials.gov/ct2/info/linking
"""

from urllib import quote

from api import API


class Trials(API):
    """Python wrapper for the Clical Trials API."""

    def __init__(self):
        super(Trials, self).__init__()
        self.base_url = 'http://clinicaltrials.gov'
        self.output_format = 'xml'
        self.required_params = {'displayxml': 'true'}
        self.search_types_dict = {
            'condition': 'cond', 'conditions': 'cond',
            'intervention': 'intr', 'interventions': 'intr',
            'outcome': 'outc', 'outcomes': 'outc',
            'sponsor': 'spons', 'sponsors': 'spons',
            'recruiting': 'recr'
        }

    def search(self, search_term=None, search_type='term', **kwargs):
        """
        Search the Clinical Trials database.

        >>> Trials().search('pediatric')
        """
        search_types_dict = self.search_types_dict
        for key in kwargs:
            if key in search_types_dict:
                correct_name = search_types_dict[key]
                data = kwargs.pop(key)
                kwargs.update({correct_name: data})
        if search_type in search_types_dict:
            search_type = search_types_dict[search_type]
        if search_term:
            kwargs.update({search_type: search_term})
        return self.call_api('search', **kwargs)

    def download(self, search_term=None, search_type='term', **kwargs):
        """
        Download a ZIP file of XML files pertaining to your search.

        >>> Trials().download("alzheimer's disease", count=50)
        """
        self.required_params = {'studyxml': 'true', 'output_format': None}
        zip_data = self.search(search_term, search_type, **kwargs)
        self.required_params = {'displayxml': 'true'}
        return zip_data
