from django.db import models
from django.core.validators import RegexValidator


word_limit_validator = RegexValidator(
    regex=r'^(\W*\w+\b\W*){1,4}$',
    message='Up to 4 words allowed.',
    code='invalid'
)

# Create your models here.
class Noticia (models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="noticias", null=True)

    def __str__(self):
        return self.titulo
    

class NuestraPropuesta(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='nuestra_propuesta/', null=True, blank=True)

    def __str__(self):
        return self.title
    

class PreguntasFrecuentes(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    button_text = models.CharField(max_length=100, null=True, blank=True, validators=[word_limit_validator])
    button_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.question
    
class Eventos(models.Model):
    title = models.CharField(max_length=200)
    descripcion_evento = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class QuienesSomos(models.Model):
    title = models.CharField(max_length=200)
    descripcion_quienesSomos = models.TextField()
    image = models.ImageField(upload_to='quienes_somos/', null=True, blank=True)

    def __str__(self):
        return self.title




class Section(models.Model):
    SECTION_CHOICES = [
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three'),
        ('four', 'Four'),
        ('five', 'Five'),
        ('six', 'Six'),
    ]

    section_type = models.CharField(max_length=10, choices=SECTION_CHOICES, default='one')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='section_images/')
    button_text = models.CharField(max_length=100, null=True, blank=True, validators=[word_limit_validator])
    button_link = models.URLField(null=True, blank=True)

    def get_style_class(self):
        style_classes = {
            'one': 'spotlight style1 bottom',
            'two': 'spotlight style2 right',
            'three': 'spotlight style3 left',
            'four': 'wrapper style1 special fade-up',
            'five': 'wrapper style2 special fade',
            'six': 'wrapper style2 special fade',
        }
        return style_classes.get(self.section_type, 'default-class')

    def __str__(self):
        return self.title



class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='images/')