from django import forms
from frontpanel.models import RoleDetails

class RoleDetailsForm(forms.ModelForm):
	class Meta:
		model=RoleDetails
		exclude=["role","name","email","password","mobile","address","gender",
		"otp","otp_time","verify_link","login_time","image","active"]