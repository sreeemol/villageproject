from django import forms
from .models import Panchayath,Employees,enduser,Leaveapplication,Complaint,News,Salary

class PanchayathForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Panchayath
        fields = ('email', 'password','name','country','state','district','pincode')
    def clean(self):
        cleaned_data = super(PanchayathForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class EmployeesForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    confirm_password  = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model =Employees
        fields = ('email','name','jobtitle','address','phonenumber','password')
    def clean(self):
        cleaned_data = super(EmployeesForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password doesnot match"
            )
class enduserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    confirm_password  = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = enduser
        fields = ('name','jobtitle','address','phonenumber')
    def clean(self):
        cleaned_data = super(enduserForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password doesnot match"
            )
class LeaveapplicationForm(forms.ModelForm):
    class Meta:
        model = Leaveapplication
        fields = ('leave_date','description')
    
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('description',)
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('description',)
class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ('salary','ta','da','credited_on')
    
        
        
