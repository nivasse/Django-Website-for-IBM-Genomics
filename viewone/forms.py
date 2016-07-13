from django import forms
class QueryForm(forms.Form):
    co_name = forms.CharField(label='Company name', max_length=100, required=False)
    city = forms.CharField(label='City', max_length=50, required=False)
    state = forms.CharField(label='State', max_length=50, required=False)
    zip = forms.CharField(label='ZipCode', max_length=15, required=False)
    sic_code = forms.CharField(label='SIC Code', max_length=100, required=False)
    pub_priv = forms.CharField(label='Public or Private', max_length=50, required=False)
    min_sales = forms.IntegerField(label='Min Sales ($ million)', required=False)
    max_sales = forms.IntegerField(label='Max Sales ($ million)', required=False)
    lower_no_employees = forms.IntegerField(label='Min no. of employees', required=False, disabled=True)
    upper_no_employees = forms.IntegerField(label='Max no. of employees', required=False, disabled=True) 
    duns_no = forms.CharField(label='DUNS Number', max_length=50, required=False, disabled=True)
    parent_duns_no = forms.CharField(label='Parent DUNS Number:', max_length=50, required=False, disabled=True)

class SearchPubmed(forms.Form):
    author_name = forms.CharField(label='Author Name', max_length=60, required=False)
    department = forms.CharField(label='Department', max_length=50, required=False)
    institution = forms.CharField(label='Institution', max_length=100, required=False)
    city = forms.CharField(label='City', max_length=40, required=False)
    state = forms.CharField(label='State', max_length=40, required=False)
    tools_used = forms.CharField(label='Tools Used', max_length=50, required=False)

