# Generated by Django 4.2.5 on 2023-09-10 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_section_style_class_alter_section_section_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='style_class',
        ),
    ]
