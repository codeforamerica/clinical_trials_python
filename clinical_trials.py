#!/usr/bin/env python

"""
Python wrapper for the Clincal Trials API.

Clinical Trials Documentation:  http://clinicaltrials.gov/ct2/info/linking
"""

import re
from urllib import quote

from api import API


class Trials(API):
    """Python wrapper for the Clinical Trials API."""

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
            'country': 'cntry1', 'state': 'state1',
            'recruiting': 'recr'
        }
        # Save compiled regular expressions.
        self._re_state = re.compile('state.*')
        self._re_country = re.compile('(country|cntry).*')
        self._re_country_num = re.compile('country(.+)')

    def search(self, search_term=None, search_type='term', **kwargs):
        """
        Search the Clinical Trials database.

        >>> Trials().search('pediatric')
        """
        if search_term:
            kwargs.update({search_type: search_term})
        kwargs = self._correct_keywords(**kwargs)
        return self.call_api('search', **kwargs)

    def _correct_keywords(self, **kwargs):
        """Internal method to loop through and correct keyword arguments."""
        search_types_dict = self.search_types_dict
        for key in kwargs:
            if self._re_state.match(key):
                state_abbrev = kwargs[key]
                kwargs[key] = 'NA:US:' + state_abbrev
            elif self._re_country.match(key):
                country_abbrev = kwargs[key]
                if len(country_abbrev) == 2:
                    # We haven't seen it before.
                    kwargs[key] = 'NA:' + country_abbrev
            if key in search_types_dict:
                # We need to go from human readable to the
                # correct search_type parameter name.
                correct_name = search_types_dict[key]
                data = kwargs.pop(key)
                kwargs.update({correct_name: data})
            elif self._re_country_num.match(key):
                # Then someone put in a keyword like `country3`.
                country_abbrev = kwargs.pop(key)
                formatted_key = self._re_country_num.sub(r'cntry\1', key)
                kwargs.update({formatted_key: country_abbrev})
        return kwargs

    def download(self, search_term=None, search_type='term', **kwargs):
        """
        Download a ZIP file of XML files pertaining to your search.

        >>> Trials().download("alzheimer's disease", count=50)
        """
        self.required_params = {'studyxml': 'true', 'output_format': None}
        zip_data = self.search(search_term, search_type, **kwargs)
        self.required_params = {'displayxml': 'true'}
        return zip_data
