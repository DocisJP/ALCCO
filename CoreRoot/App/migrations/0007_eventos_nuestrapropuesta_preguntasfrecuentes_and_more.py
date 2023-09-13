# Generated by Django 4.2.5 on 2023-09-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_section_button_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descripcion_evento', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NuestraPropuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='nuestra_propuesta/')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasFrecuentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuienesSomos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descripcion_quienesSomos', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='quienes_somos/')),
            ],
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(max_length=400),
        ),
    ]
