#!/usr/bin/env python2
import urllib2
from lxml import etree
import sys

def get_url_data(url):
    response = urllib2.urlopen(url)
    return response.read()
    stringio = StringIO.StringIO(response.read())
    filedata = stringio.getvalue()
    stringio.close()
    return filedata


def parse_url_xml_tree(url):
    parser = etree.HTMLParser()
    txt = get_url_data(url)
    tree = etree.fromstring(txt, parser)
    return tree


def get_links_matching(url, patterns):
    tree = parse_url_xml_tree(url)
    elems = tree.xpath("//a")
    links = [e.get("href") for e in elems]
    links = [link for link in links if link]
    if patterns:
        links = [link for link in links if any([pattern in link for pattern in patterns])]
    links = [urllib2.urlparse.urljoin(url, link) for link in links]
    return links


def main(args):
    for url in get_links_matching(args[0], args[1:]):
        print url
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
