from django.shortcuts import render, redirect
from django.views import View
from App.forms import DonacionForm
import mercadopago

class DonacionView(View):
    def get(self, request):
        form = DonacionForm()
        return render(request, 'Donaciones/donaciones.html', {'form': form})

    def post(self, request):
        form = DonacionForm(request.POST)
        if form.is_valid():
            # Configura las credenciales de MercadoPago
            mp = mercadopago.MP("TU_CLIENT_ID", "TU_CLIENT_SECRET")

            # Crea una preferencia de pago
            preference_data = {
                "items": [
                    {
                        "title": "Donación",
                        "quantity": 1,
                        "currency_id": "ARS",  # Ajusta según tu moneda local
                        "unit_price": float(form.cleaned_data['monto'])
                    }
                ],
                "payer": {
                    "name": form.cleaned_data['nombre'],
                    "surname": form.cleaned_data['apellido'],
                    "email": form.cleaned_data['email'],
                }
            }
            try:
                preference = mp.create_preference(preference_data)
                # Redirige al usuario a MercadoPago para completar el pago
                return redirect(preference['response']['init_point'])
            except Exception as e:
                # Log the exception (consider using a logging framework)
                print(str(e))
                # Return a response indicating an error occurred
                return render(request, 'Donaciones/donaciones.html', {'form': form, 'error': 'An error occurred while processing your donation. Please try again.'})
        else:
            return render(request, 'Donaciones/donaciones.html', {'form': form})
