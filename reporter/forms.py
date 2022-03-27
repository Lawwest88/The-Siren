from django.forms import ModelForm
from reporter.models import Reporter    

    
class ReporterForm(ModelForm):

    class Meta:
        model = Reporter 
        feilds = ['first_name','last_name','user_email','age']
