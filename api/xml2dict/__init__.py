"""
xml2dict
Thunder Chen<nkchenz@gmail.com> 2007.9.1

Convert an XML string or file with XML data to a dict object.
http://code.google.com/p/xml2dict/
"""

from .xml2dict import XML2Dict, Dict2XML
from object_dict import object_dict


def xml2dict(data):
    """Turn XML into a dictionary."""
    converter = XML2Dict()
    if hasattr(data, 'read'):
        # Then it's a file.
        data = data.read()
    return converter.fromstring(data)


def dict2xml(data):
    """Turn a dictionary into XML."""
    converter = Dict2XML()
    return converter.tostring(data)


__all__ = [XML2Dict, Dict2XML, xml2dict, dict2xml, object_dict]
