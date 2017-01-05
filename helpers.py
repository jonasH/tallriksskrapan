# Use this file for support functions


def utf8text(text):
    return text.encode('raw_unicode_escape').decode('utf-8')
