from django import forms
from stdpage.models import upoad1

class upload1Form(forms.ModelForm):
	
	class Meta:
		model = upoad1
		fields = ('flname','thumbnail',)
