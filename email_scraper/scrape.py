import base64
import re

from tlds import tld_set

EMAIL_REGEX = '([%(local)s][%(local)s.]+[%(local)s]@[%(domain)s.]+\\.(?:%(tlds)s))(?:[^%(domain)s]|$)' % {
    'local': 'A-Za-z0-9!#$%&\'*+\\-/=?^_`{|}~',
    'domain': 'A-Za-z0-9\-',
    'tlds': '|'.join(tld_set)
}

HIDDEN_AT_SYM = (" (at) ", " [at] ", " (@) ", " [@] ", " @ ")
HIDDEN_DOT_SYM = (" (dot) ", " [dot] ", " (.) ", " [.] ", " . ")
HIDDEN_REGEX = [
    '(\w+({0})\w+({1})\w+)'.format(
        at.replace("(", r"\(").replace(")", r"\)").replace("[", r"\[").replace("]", r"\]"), 
        dot.replace("(", r"\(").replace(")", r"\)").replace("[", r"\[").replace("]", r"\]"), 
    )
    for at, dot in zip(HIDDEN_AT_SYM, HIDDEN_DOT_SYM)
]

def extract_emails(text):
    def unhide_email(hidden_email):
        for at_sym in HIDDEN_AT_SYM:
            hidden_email = hidden_email.replace(at_sym, "@")
        for dot_sym in HIDDEN_DOT_SYM:
            hidden_email = hidden_email.replace(dot_sym, ".")
        return hidden_email

    hidden = []
    for expr in HIDDEN_REGEX:
        hidden += [unhide_email(i[0]) for i in re.findall(expr, text)]
    return re.findall(EMAIL_REGEX, text) + hidden


def deobfuscate_html(html):
    def unescape(html_text):
        try:
            # Python 2.6-2.7
            from HTMLParser import HTMLParser
            return HTMLParser().unescape(html_text)
        except ImportError:
            # Python 3
            import html
            try:
                return html.unescape(html_text)
            except AttributeError:
                # Python 3.2/3.3
                from html.parser import HTMLParser
                return HTMLParser().unescape(html_text)

    def replace_atob(matchobj):
        return base64.b64decode(matchobj.groups()[0].encode('utf-8')).decode('utf-8')

    html = unescape(html)
    html = re.sub('atob\\([\'"]([A-Za-z0-9+/]+)[\'"]\\)', replace_atob, html)
    return html


def scrape_emails(html):
    """
    Look for email addresses in HTML and return them. This includes addresses in text, links and even obfuscated email
    addresses. Currently supports `atob()` and HTML entities obfuscations.

    :param html: string containing HTML
    :return: a set of email addresses found in the HTML
    """
    return set(extract_emails(deobfuscate_html(html)))
