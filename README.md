Clincal Trials Python API
=========================

A Python API wrapper for the
[ClincalTrials.gov API](http://clinicaltrials.gov/ct2/info/linking).

Documentation for [ClinicalTrials.gov can be found
here.](http://clinicaltrials.gov/ct2/info/linking)


Usage
-----

The `Trials` class only has two methods -- `search` and `download`. The
same information from `search` is returned to the `download` method in
ZIP file format.

    >>> from clinical_trials import Trials
    >>> t = Trials()
    >>> t.search("alzheimer's disease")

    >>> t.search('diabetes', 'cond')
    >>> t.search('diabetes', 'condition')
    >>> t.search(condition='diabetes')

    >>> # Specify the number of trials turned.
    ... t.search(intervention='Fluoxetine', count=200)

    >>> # Find trials no longer recruiting.
    ... t.search('lyme disease', recruiting='closed')

    >>> # If you want plain XML returned back.
    ... t.search(sponsor='NHLBI', output_format=None)

    >>> # You can also find trials by location -- up to 3 states or countries.
    ... t.search('cancer', state='TX')

    >>> t.search('diabetes', state1='TX', state2='NY', state3='CA')
    >>> t.search(condition='lyme disease', country1='US', country2='CA')

    >>> # And you can download a ZIP file with the data.
    ... zip_file = t.download('cancer', count=500)


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
