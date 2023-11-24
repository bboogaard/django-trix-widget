from django import forms
from django.test.testcases import SimpleTestCase
from pyquery import PyQuery

from trix_widget.widgets import TrixWidget


class FormTest(forms.Form):

    text = forms.CharField(widget=TrixWidget())


class TestWidgets(SimpleTestCase):

    def test_round_trip(self):
        form = FormTest(initial={
            'text': 'Foobar'
        })
        output = form.as_p()
        doc = PyQuery(output)
        hidden_field = PyQuery(doc.find('input[type="hidden"]'))
        self.assertEqual(hidden_field.val(), 'Foobar')
        trix_editor = PyQuery(doc.find('trix-editor'))
        self.assertEqual(trix_editor.attr('input'), 'id_text')
        form = FormTest(data={
            'text': '<div><strong>Hello</strong><br><br>Hello world</div>'
        })
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data['text'], '<strong>Hello</strong><br><br>Hello world')
