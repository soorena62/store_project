from django import forms
from .models import Order
# Create your model here:


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'If you have any notes please enter here otherwise leave it empty.'
            }),
        }
