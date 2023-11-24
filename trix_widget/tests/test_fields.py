from django import forms
from django.test.testcases import TestCase
from pyquery import PyQuery

from trix_widget.tests.testapp.models import TrixModel


class FormTest(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = TrixModel


class TestFields(TestCase):

    def test_round_trip(self):
        instance = TrixModel.objects.create(text='Foobar')
        form = FormTest(instance=instance)
        output = form.as_p()
        doc = PyQuery(output)
        hidden_field = PyQuery(doc.find('input[type="hidden"]'))
        self.assertEqual(hidden_field.val(), 'Foobar')
        trix_editor = PyQuery(doc.find('trix-editor'))
        self.assertEqual(trix_editor.attr('input'), 'id_text')
        form = FormTest(data={
            'text': '<div><strong>Hello</strong><br><br>Hello world</div>'
        }, instance=instance)
        self.assertTrue(form.is_valid(), form.errors)
        instance = form.save()
        self.assertEqual(instance.text.as_html, '<strong>Hello</strong><br><br>Hello world')
