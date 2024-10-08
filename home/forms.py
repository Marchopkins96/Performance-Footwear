from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    # Define form fields
    name = forms.CharField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )

    def clean(self):
        # Custom cleaning method to perform additional validation
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        message = cleaned_data.get("message")
        return cleaned_data
