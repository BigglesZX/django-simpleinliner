from django.conf import settings


''' If set to True, simpleinliner will raise an exception when a static file
    could not be found. Other exceptions may exist in the future.
'''
SIMPLEINLINER_RAISE_EXCEPTIONS = \
    getattr(settings, 'SIMPLEINLINER_RAISE_EXCEPTIONS', False)

''' This dict controls the attributes given to the `script` and `style` tags
    generated by simpleinliner for wrapping inlined static files.
'''
SIMPLEINLINER_DEFAULT_TAG_ATTRIBUTES = \
    getattr(settings, 'SIMPLEINLINER_DEFAULT_TAG_ATTRIBUTES', {
        'script': {
            'charset': 'utf-8',
            'type': 'text/javascript',
        },
        'style': {
            'charset': 'utf-8',
            'type': 'text/css',
        },
    })
