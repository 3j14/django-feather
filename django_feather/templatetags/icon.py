from django import template

from django_feather import icons

register = template.Library()


class IconNode(template.Node):
    """Icon Node

    A Feather Icon DOM Node that can be used to render Feather Icons in
    the Django Templating Engine
    """

    def __init__(self, icon_expr, attrs: dict = {}):
        self.icon_expr = icon_expr
        self.attrs = attrs

    def render(self, context) -> str:
        """Render

        Render the IconNode as a string DOM object.

        :param context: The context of the current template. Passed by
            the template engine
        :return: String DOM object
        :trype: str
        """
        try:
            # Resolve the icon name from the context.
            # `icon_expr` can be either a variable (e.g. `self.icon`)
            # or an actual string (e.g. `"icon"`)
            icon_name = self.icon_expr.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        if not icon_name:
            return ''
        # Use the python underscore convention for icon names
        icon_name = icon_name.replace('-', '_')
        if not hasattr(icons, icon_name):
            # Icon could not be found
            return ''

        svg: str = getattr(icons, icon_name)
        head: list = ['<svg']
        tail: list = [svg.split('<svg ')[-1]]
        attributes: list = ['%s=\"%s\"' % (attr, val.resolve(context))
                            for attr, val in self.attrs.items()]
        if 'width' not in self.attrs:
            attributes.append('width=\"24\"')
        if 'height' not in self.attrs:
            attributes.append('height=\"24\"')
        return ' '.join(head + attributes + tail)


@register.tag(name='icon')
def icon(parser, token) -> IconNode:
    """Icon Tag

    Feather Icon Tag for django templates

    .. usage::
        - `{% icon "icon_name"  class="css-class" %}`
        - `{% icon self.icon class="css-class" height="18" %}`

    :param parser: Passed by the templating engine
    :param token: A list of attributes passed to the tag
    :return: A IconNode instance
    :rtype: IconNode
    """
    bits = token.split_contents()[1:]
    icon_expr = parser.compile_filter(bits[0])
    bits = bits[1:]

    attrs = {}

    for bit in bits:
        attr, val = bit.split('=')
        # setup to resolve context variables as value
        attrs[attr] = parser.compile_filter(val)

    return IconNode(icon_expr, attrs=attrs)
