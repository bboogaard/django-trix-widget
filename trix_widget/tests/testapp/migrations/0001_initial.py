# Generated by Django 4.2.7 on 2023-11-24 15:27

from django.db import migrations, models
import trix_widget.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrixModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', trix_widget.fields.TrixField(blank=True)),
            ],
        ),
    ]