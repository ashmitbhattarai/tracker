from django import forms
from models import status1,comment,asgmnt1

class statusForm(forms.ModelForm):
	class Meta:
		model = status1
		fields = ('stats',)
		get_latest_by = 'syear'
		labels = {"stats":(''),}
		widgets = {
				"stats":forms.TextInput(
					attrs={'class':'form-control','placeholder':'Write your Status Here...'},
					# widget = forms.TextInput(label={""})
					)
		}
		
class commentForm(forms.ModelForm):
	
	class Meta:
		model = comment
		fields = ('comments',)
		get_latest_by = 'pub_date'
		
class asg1_Form(forms.ModelForm):
	
	class Meta:
		model = asgmnt1
		fields = ('subject','assignment','doi',)
		get_latest_by = 'doi'
	# class Media:
		# 'css':'thing.css'
		# OR, fields = ({'subect':'style=color:red;"'})