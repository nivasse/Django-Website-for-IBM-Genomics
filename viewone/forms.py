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

class SearchNsfawards(forms.Form):
    author_fname = forms.CharField(label='Investigator First Name', max_length=50, required=False)
    author_lname = forms.CharField(label='Investigator Last Name', max_length=50, required=False)
    award_id = forms.IntegerField(label='NSF Award Abstract No', required=False)
    award_amount = forms.IntegerField(label='Award Amount ($)  >= ', required=False)
    award_title = forms.CharField(label='Title Contains', max_length=100, required=False)
    award_abstract = forms.CharField(label='Abstract Contains', max_length=100, required=False)
    grant_type = forms.CharField(label='Type of Grant', max_length=50, required=False)
    lower_start_date = forms.CharField(label='Start Date (yyyy-mm-dd) >= ', max_length=10, min_length=10, required=False)
    upper_start_date = forms.CharField(label='Start Date (yyyy-mm-dd) <= ', max_length=10, min_length=10, required=False)
    lower_end_date = forms.CharField(label='End Date (yyyy-mm-dd) >= ', max_length=10, min_length=10, required=False)
    upper_end_date = forms.CharField(label='End Date (yyyy-mm-dd) <= ', max_length=10, min_length=10, required=False)
    inst_name = forms.CharField(label='Name of Sponsoring Institution', max_length=100, required=False)
    inst_city = forms.CharField(label='Institution - City', max_length=50, required=False)
    inst_state = forms.CharField(label='Institution - State', max_length=50, required=False)
    mesh_terms = forms.CharField(label='MeSH Terms', max_length=100, required=False) 
    gene_tools = forms.CharField(label='Gene Tools', max_length=50, required=False)
    gene_techniques = forms.CharField(label='Gene Techniques', max_length=50, required=False)
