# Generated by Django 4.2.5 on 2023-09-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='noticias')),
            ],
        ),
    ]