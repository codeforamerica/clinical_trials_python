#!/usr/bin/env python
"""
Author: Zach Williams, <zach AT codeforamerica DOT org>

Copyright (c) 2011, Code for America. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary form
must reproduce the above copyright notice, this list of conditions and the
following disclaimer in the documentation and/or other materials provided with
the distribution. Neither the name of Code for America nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission. THIS SOFTWARE IS PROVIDED
BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
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
"""

setup(name="clinical_trials",
      version="1.0",
      description="Python wrapper for the Clincal Trials API.",
      long_description=long_description,
      keywords="clinical trials, clinicaltrials, clinical_trials",
      author="Zach Williams",
      author_email="zach@codeforamerica.org",
      url="https://github.com/codeforamerica/Clinical-Trials-Python",
      license="BSD",
      packages=["clinical_trials"],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test_clinical_trials.py",
      tests_require=["mock", "Mock"])
