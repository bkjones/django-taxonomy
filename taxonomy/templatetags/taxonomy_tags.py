from django.db.models import get_model
from django.template import Library, Node, TemplateSyntaxError, Variable, resolve_variable

from taxonomy.models import TaxonomyMap

register = Library()

class TaxonomyForObjectNode(Node):
    def __init__(self, obj, context_var):
        self.obj = Variable(obj)
        self.context_var = context_var

    def render(self, context):
        context[self.context_var] = \
            TaxonomyMap.objects.get_for_object(self.obj.resolve(context))
        return ''

def do_taxonomy_for_object(parser, token):
    """
    Retrieves a list of ``TaxonomyMap`` objects and stores them in a context variable.

    Usage::

       {% taxonomy_for_object [object] as [varname] %}

    Example::

        {% taxonomy_for_object foo_object as taxonomy_list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError(('%s taxonomy requires exactly three arguments') % bits[0])
    if bits[2] != 'as':
        raise TemplateSyntaxError(("second argument to %s taxonomy must be 'as'") % bits[0])
    return TaxonomyForObjectNode(bits[1], bits[3])

register.tag('taxonomy_for_object', do_taxonomy_for_object)
