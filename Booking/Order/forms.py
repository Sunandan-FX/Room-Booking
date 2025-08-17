from django import forms 
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name','last_name','email','phone_number','room_number','feedback')
