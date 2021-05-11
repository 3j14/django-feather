import base64
import io
from typing import Optional
from xml.dom import minidom

from django import template

from django_feather import icons

register = template.Library()


class IconNode(template.Node):
    """Icon Node

    A Feather Icon DOM Node that can be used to render Feather Icons in
    the Django Templating Engine
    """

    def __init__(self, icon_expr, attrs: Optional[dict] = None):
        if attrs is None:
            attrs = {}
        # data_uri is used to return a valid data uri string which
        # will be interpreted by browsers as an URI and can thus be used
        # to render SVGs e.g. from ``src`` attributes or from CSS.
        self.data_uri = attrs.pop("data_uri", False)
        self.icon_expr = icon_expr
        self.attrs = attrs

    def render(self, context) -> str:
        """Render

        Render the IconNode as a string DOM object.

        :param context: The context of the current template. Passed by
            the template engine
        :return: String DOM object
        :rtype: str
        """
        try:
            # Resolve the icon name from the context.
            # `icon_expr` can be either a variable (e.g. `self.icon`)
            # or an actual string (e.g. `"icon"`)
            icon_name = self.icon_expr.resolve(context)
        except template.VariableDoesNotExist:
            return ""
        if not icon_name:
            return ""
        # Use the python underscore convention for icon names
        icon_name = icon_name.replace("-", "_")
        if not hasattr(icons, icon_name):
            # Icon could not be found
            return ""

        doc = minidom.parseString(getattr(icons, icon_name))
        for attr, val in self.attrs.items():
            doc.documentElement.setAttribute(attr, val.resolve(context))

        writer = io.StringIO()
        SVGDocument(doc).writexml(writer)
        svg_output: str = writer.getvalue()
        if not self.data_uri:
            return svg_output
        else:
            svg_base64: bytes = base64.b64encode(svg_output.encode("utf-8"))
            return "data:image/svg+xml;base64,{svg_base64:s}".format(
                svg_base64=svg_base64.decode("ascii")
            )


@register.tag(name="icon")
def icon(parser, token) -> IconNode:
    """Icon Tag

    Feather Icon Tag for django templates

    .. usage::
        - `{% icon "icon_name" class="css-class" data_uri=True %}`
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
        attr, val = bit.split("=")
        # setup to resolve context variables as value
        attrs[attr] = parser.compile_filter(val)

    return IconNode(icon_expr, attrs=attrs)


class SVGDocument:
    def __init__(self, doc: minidom.Document):
        self._doc = doc

    @property
    def doc(self) -> minidom.Document:
        return self._doc

    def writexml(self, writer, indent="", addindent="", newl=""):
        """Ignore the xml tag"""
        for node in self.doc.childNodes:
            node.writexml(writer, indent, addindent, newl)
