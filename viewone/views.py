from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from .models import IbmTruth, PubmedAuthor
from django.template import RequestContext
# Create your views here.

from .forms import QueryForm, SearchPubmed

def index(request):
	return render(request, 'viewone/index.html')

def home(request):
	return render(request, 'viewone/home.html')

def searchpubmed(request):
	context = RequestContext(request)
	form = SearchPubmed()
	flag = False
	context['flag'] = flag
	if request.method == 'POST':
            form = SearchPubmed(data=request.POST)
            flag = True
            context['flag'] = flag
	if form.is_valid():
	    author_name = form.cleaned_data['author_name']
	    department = form.cleaned_data['department']
	    institution = form.cleaned_data['institution']
	    city = form.cleaned_data['city']
	    state = form.cleaned_data['state']
	    tools_used = form.cleaned_data['tools_used']
	    search_dict = {}
	    if author_name:
		search_dict['author_name__istartswith']=author_name
	    if department:
		search_dict['department__icontains']=department
	    if institution:
		search_dict['institution__icontains']=institution
	    if city:
		search_dict['city__istartswith']=city
	    if state:
		search_dict['state__istartswith']=state
	    if tools_used:
		search_dict['tools_used__istartswith']=tools_used
	    search_dict['country__istartswith']="US"
	    search_results = PubmedAuthor.objects.filter(**search_dict).order_by('pmid','author_name').exclude(author_name="et al")
            context['search_results']= search_results
        else:
            print ("Error")
        return render(request, 'viewone/searchpubmed.html', {'form': form, }, context) 
def searchcompany(request):
	context = RequestContext(request)
	form = QueryForm()
	flag = False
	context['flag'] = flag
        if request.method == 'POST':
            form = QueryForm(data=request.POST)
	    flag = True
	    context['flag'] = flag
        if form.is_valid():
            #Accessing the data in cleaned_data
            co_name = form.cleaned_data['co_name']
 	    city = form.cleaned_data['city']
	    state = form.cleaned_data['state']
	    zipcode = form.cleaned_data['zip']
	    lower_co_size = form.cleaned_data['lower_no_employees']
	    upper_co_size = form.cleaned_data['upper_no_employees']
	    sic_code = form.cleaned_data['sic_code']
	    duns_no = form.cleaned_data['duns_no']
	    parent_duns_no = form.cleaned_data['parent_duns_no']
	    pub_priv = form.cleaned_data['pub_priv']
	    min_sales = form.cleaned_data['min_sales']
	    max_sales = form.cleaned_data['max_sales']
            search_dict = {}
	    if co_name :
		search_dict['co_name__istartswith']=co_name
            if city :
                search_dict['hq_city__istartswith']=city
            if state :
                search_dict['hq_state__istartswith']=state
            if zipcode :
                search_dict['hq_zip__istartswith']=zipcode
            if lower_co_size :
                search_dict['no_employees__gt']=lower_co_size
            if upper_co_size :
                search_dict['no_employees__lt']=upper_co_size
            if sic_code :
                search_dict['sic_code__icontains']=sic_code
            if duns_no :
                search_dict['dnus_no__icontains']=duns_no
            if parent_duns_no :
                search_dict['duns_parent__exact']=int(parent_duns_no)
            if pub_priv:
                search_dict['pub_priv__icontains']=pub_priv
            if min_sales:
                search_dict['sales__gt']=min_sales*1000000
	    if max_sales:
                search_dict['sales__lt']=max_sales*1000000

	    search_results = IbmTruth.objects.filter(**search_dict).order_by('co_name')
	    context['search_results']= search_results 
	else:
	    print ("Error")
	return render(request, 'viewone/searchcompany.html', {'form': form, }, context)

def displayall(request):
    order_alpha = IbmTruth.objects.order_by('co_name')
    context = { 'order_alpha' : order_alpha}
    return render(request, 'viewone/displayall.html', context)

def company(request, co_name):
    question = get_list_or_404(IbmTruth, pk=co_name)
    question = question[0]
    return render(request, 'viewone/company.html', {'question': question})

