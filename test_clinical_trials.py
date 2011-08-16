#!/usr/bin/env python

"""Unit tests for the Clinical Trials API."""

import unittest

from mock import Mock

from clinical_trials.api import api
from clinical_trials import Trials


class TestTrialsInit(unittest.TestCase):

    def test_Trials_class_init(self):
        trials = Trials()
        self.assertEquals(trials.base_url, 'http://clinicaltrials.gov')
        self.assertEquals(trials.output_format, 'xml')
        self.assertEquals(trials.required_params, {'displayxml': 'true'})


class TestSearchMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_default_search_method(self):
        Trials().search('test')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?term=test&displayxml=true')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_no_output_formatting(self):
        Trials().search('test', output_format=None)
        self.assertFalse(api.xml2dict.called)

    def test_search_method_with_spaces(self):
        Trials().search('foo bar')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?term=foo+bar&displayxml=true')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_special_characters(self):
        Trials().search('"foo bar"')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?term=%22foo+bar%22&displayxml=true')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_search_type_arg(self):
        Trials().search('test', 'outc')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?displayxml=true&outc=test')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_human_readable_search_type(self):
        Trials().search('diabetes', 'condition')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?displayxml=true&cond=diabetes')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_closed_recruiting_kwarg(self):
        Trials().search('test', recr='closed')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?recr=closed&term=test&displayxml=true')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_just_kwargs(self):
        Trials().search(cond='diabetes', intr='Fluoxetine', recr='open')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?recr=open&displayxml=true'
                        '&cond=diabetes&intr=Fluoxetine')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_human_readable_kwargs(self):
        Trials().search(condition='diabetes', intervention='Fluoxetine',
                        recruiting='open')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?recr=open&displayxml=true'
                        '&cond=diabetes&intr=Fluoxetine')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_specified_count(self):
        Trials().search(condition="alzheimer's disease", count=200)
        expected_url = ('http://clinicaltrials.gov/search?'
                        'count=200&displayxml=true&cond=alzheimer%27s+disease')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_state_kwarg(self):
        Trials().search('cancer', state='TX')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?state1=NA%3AUS%3ATX'
                        '&displayxml=true&term=cancer')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_country_kwarg(self):
        Trials().search(condition='diabetes', country='CA')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?cntry1=NA%3ACA'
                        '&displayxml=true&cond=diabetes')
        api.urlopen.assert_called_with(expected_url)

    def test_search_method_with_multiple_country_kwargs(self):
        Trials().search(country='US', country2='CA')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?cntry1=NA%3AUS'
                        '&cntry2=NA%3ACA&displayxml=true')
        api.urlopen.assert_called_with(expected_url)


class TestDownloadMethod(unittest.TestCase):

    def setUp(self):
        api.urlopen = Mock()
        api.xml2dict = Mock()

    def test_default_download_method(self):
        Trials().download('test')
        expected_url = ('http://clinicaltrials.gov/'
                        'search?term=test&studyxml=true')
        api.urlopen.assert_called_with(expected_url)

    def test_download_method_with_human_readable_kwargs(self):
        Trials().download(condition='diabetes', intervention='Fluoxetine',
                          recruiting='open', count=150)
        expected_url = ('http://clinicaltrials.gov/'
                        'search?count=150&studyxml=true'
                        '&cond=diabetes&intr=Fluoxetine&recr=open')
        api.urlopen.assert_called_with(expected_url)


if __name__ == '__main__':
    unittest.main()
