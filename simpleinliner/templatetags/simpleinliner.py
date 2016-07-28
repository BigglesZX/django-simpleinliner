from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.encoding import smart_text
from html import HTML

from ..exceptions import SimpleInlinerException
from ..settings import *


register = template.Library()


class SimpleInlinerBaseNode(template.Node):
    ''' Base class from which CSS- and JS-specific nodes inherit

        Defines common functionality for building HTML, searching for static
        files using Django finders, and reading contents of the file.
    '''

    def __init__(self, path):
        ''' clean up the supplied path and initialise the HTML instance '''
        self.path = smart_text(path)
        self.html = HTML()

    def prepare_html_tag(self):
        ''' call the appropriate method on the html object to generate a script
            or style tag (tag name comes from a variable hence the awkward
            calling syntax). Use default attributes from settings.
        '''
        return getattr(self.html, self.html_tag_name)(
            **SIMPLEINLINER_DEFAULT_TAG_ATTRIBUTES[self.html_tag_name]
        )

    def prepare_html_tag_contents(self):
        ''' Locate the specified static file using Django's staticfiles finders,
            raising an exception if appropriate. Read in and return the file
            contents.
        '''
        contents = ''
        if settings.DEBUG:
            self.expanded_path = finders.find(self.path)
        else:
            self.expanded_path = staticfiles_storage.path(self.path)
        if not self.expanded_path:
            if SIMPLEINLINER_RAISE_EXCEPTIONS:
                raise SimpleInlinerException("The supplied static file path, "
                                             "'{0}', could not be found.".format(
                                                self.path
                                             ))
            return contents
        with open(self.expanded_path) as static_file:
            contents = static_file.read()
        return contents

    def render(self, context):
        ''' Build the appropriate HTML tag and fill it with delicious contents
        '''
        self.html_tag = self.prepare_html_tag()
        self.html_tag.text(self.prepare_html_tag_contents(), escape=False)
        return unicode(self.html_tag)


class SimpleInlinerCSSNode(SimpleInlinerBaseNode):
    ''' CSS-specific child class '''
    html_tag_name = 'style'


class SimpleInlinerJSNode(SimpleInlinerBaseNode):
    ''' JS-specific child class '''
    html_tag_name = 'script'


def prepare_path(parser, token):
    ''' Boilerplate to clean up path arg '''
    try:
        tag_name, path = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )
    if not (path[0] == path[-1] and path[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return path


@register.tag
def inlinecss(parser, token):
    ''' Invoke the CSS-specific template node '''
    path = prepare_path(parser, token)
    return SimpleInlinerCSSNode(path[1:-1])


@register.tag
def inlinejs(parser, token):
    ''' Invoke the JS-specific template node '''
    path = prepare_path(parser, token)
    return SimpleInlinerJSNode(path[1:-1])
