from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    review_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Review
        fields = ['review_id', 'text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
