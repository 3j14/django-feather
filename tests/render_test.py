from django.test import TestCase
from django.template import Context, Template


class FeatherTemplateTest(TestCase):
    def test_render(self):
        context = Context({})
        template_to_render = Template("{% load icon %}{% icon 'coffee' %}")
        rendered_template = template_to_render.render(context)
        self.assertIn("<svg", rendered_template)

    def test_base64(self):
        context = Context({})
        template_to_render = Template("{% load icon %}{% icon 'coffee' data_uri=True %}")
        rendered_template = template_to_render.render(context)
        self.assertTrue(rendered_template.startswith("data:image/svg+xml;base64"))
