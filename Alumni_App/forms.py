from django import forms
from .models import Alumni

class AlumniRegistrationForm(forms.ModelForm):
    skills = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'List your key skills and expertise',
        'rows': 4,
        'class': 'form-control'
    }), required=False)
    
    interests = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'What are your areas of interest?',
        'rows': 4,
        'class': 'form-control'
    }), required=False)

    class Meta:
        model = Alumni
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'graduation_year', 'degree', 'company_name', 'position', 'skills', 'interests']
    
    # Adding custom validation to ensure that phone number is 10 digits long
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be 10 digits long.")
        return phone_number
    
    # Custom clean method for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Alumni.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    # Optional: Add more custom validation or formatting for other fields as needed
