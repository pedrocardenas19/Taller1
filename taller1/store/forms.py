# forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']

    def clean_price(self):
        price = self.cleaned_data['price']

        # Validar que el precio sea mayor que cero
        if price <= 0:
            raise ValidationError("El precio debe ser mayor que cero.")

        return price

    def clean_image(self):
        image = self.cleaned_data['image']

        if image:
            valid_extensions = ['jpg', 'jpeg', 'png']
            file_extension = image.name.split('.')[-1].lower()
            if file_extension not in valid_extensions:
                raise ValidationError("El archivo de imagen debe tener una extensión válida (jpg, jpeg, png).")

            max_size = 5 * 1024 * 1024  # 5 MB en bytes
            if image.size > max_size:
                raise ValidationError("El tamaño de la imagen no debe superar los 5 MB.")

        return image
