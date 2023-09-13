from django import forms 

class DonacionForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=False, max_length=50)
    apellido = forms.CharField(label="Apellido", required=False, max_length=50)
    email = forms.EmailField(label="Email", required=True, max_length=50)
    monto = forms.IntegerField(label="Monto", required=True)
    fecha = forms.DateField(label="Fecha", required=True)
    comentario = forms.CharField(label="Comentario", required=False, max_length=200)


class ContactoForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)