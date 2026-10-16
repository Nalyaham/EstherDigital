# esther_digital/forms.py
from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # Honeypot: real people never see or fill this; bots often do.
    website = forms.CharField(required=False)

    class Meta:
        model = ContactMessage
        fields = ["first_name", "last_name", "email", "message"]

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""