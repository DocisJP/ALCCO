# Generated by Django 4.2.5 on 2023-09-10 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_type', models.CharField(choices=[('one', 'One'), ('two', 'Two'), ('three', 'Three'), ('four', 'Four'), ('five', 'Five')], max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='section_images/')),
                ('button_text', models.CharField(blank=True, max_length=100, null=True)),
                ('button_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
