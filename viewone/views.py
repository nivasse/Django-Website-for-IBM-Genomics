from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from .models import IbmTruth, PubmedAuthor, NsfawardsAuthors, NsfawardsTest1, HospitalsUsa, StatesUsa
from django.template import RequestContext
from django.db.models import Max,Min


# Create your views here.

from .forms import QueryForm, SearchPubmed, SearchNsfawards, SearchHospitals

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

def nsfawards(request, award_id):
    award_details = get_object_or_404(NsfawardsTest1, pk=award_id)
    authors = NsfawardsAuthors.objects.filter(award=award_id)
    return render(request, 'viewone/nsfawards.html', {'award_details': award_details, 'authors': authors, }) 

def searchnsfawards(request):
        context = RequestContext(request)
        form = SearchNsfawards()
        flag = False
        context['flag'] = flag
        if request.method == 'POST':
            form = SearchNsfawards(data=request.POST)
            flag = True
            context['flag'] = flag
        if form.is_valid():
	    author_fname = form.cleaned_data['author_fname']
	    author_lname = form.cleaned_data['author_lname']
            award_id = form.cleaned_data['award_id']
            award_amount = form.cleaned_data['award_amount']
            award_title = form.cleaned_data['award_title']
            award_abstract = form.cleaned_data['award_abstract']
            grant_type = form.cleaned_data['grant_type']
            lower_start_date = form.cleaned_data['lower_start_date']
            upper_start_date = form.cleaned_data['upper_start_date']
            lower_end_date = form.cleaned_data['lower_end_date']
            upper_end_date = form.cleaned_data['upper_end_date']
            inst_name = form.cleaned_data['inst_name']
            inst_city = form.cleaned_data['inst_city']
            inst_state = form.cleaned_data['inst_state']
            mesh_terms = form.cleaned_data['mesh_terms']	
	    gene_tools = form.cleaned_data['gene_tools']
	    gene_techniques = form.cleaned_data['gene_techniques']    
	
            #setting initial values for date range
            act_lower_start_date = NsfawardsTest1.objects.all().aggregate(Min('award_start_date'))['award_start_date__min']
            act_upper_start_date = NsfawardsTest1.objects.all().aggregate(Max('award_start_date'))['award_start_date__max']
            act_lower_end_date = NsfawardsTest1.objects.all().aggregate(Min('award_end_date'))['award_end_date__min']
	    act_upper_end_date = NsfawardsTest1.objects.all().aggregate(Max('award_end_date'))['award_end_date__max']
            search_dict = {}
	    state_dict = {}
	    author_dict = {}
            if award_id:
                search_dict['award_id__exact']=award_id
            if award_amount:
		search_dict['award_amount__gte']=award_amount
	    if award_title:
                search_dict['award_title__icontains']=award_title+" "   
            if award_abstract:
                search_dict['abstract__icontains']=award_abstract+" "
            if grant_type:
                search_dict['award_instrument__icontains']=grant_type
            if inst_name:
                search_dict['institution_name__icontains']=inst_name
            if inst_city:
                search_dict['institution_city__istartswith']=inst_city
	    if inst_state:
            	search_dict['institution_state__istartswith']=inst_state
		#search_dict['institution_state_code']=inst_state
	    if lower_start_date:
		act_lower_start_date=lower_start_date
	    if upper_start_date:
		act_upper_start_date=upper_start_date
	    if lower_end_date:
		act_lower_end_date=lower_end_date
	    if upper_end_date:
		act_upper_end_date=upper_end_date
            if mesh_terms:
		search_dict['mesh_terms__icontains'] = mesh_terms
	    if gene_tools:
		search_dict['gene_tools__istartswith'] = gene_tools
	    if gene_techniques:
		search_dict['gene_techniques__icontains'] = gene_techniques
	    if author_fname:
		author_dict['nsfawardsauthors__first_name__istartswith'] = author_fname
	    if author_lname:
		author_dict['nsfawardsauthors__last_name__istartswith'] = author_lname   	    
           
            search_dict['award_start_date__range']=[act_lower_start_date,act_upper_start_date]
	    search_dict['award_end_date__range']=[act_lower_end_date,act_upper_end_date]    
	
            search_results1 = NsfawardsTest1.objects.filter(**search_dict).order_by('award_id')
            search_results2 = NsfawardsTest1.objects.filter(**author_dict)
	    search_results3 = NsfawardsTest1.objects.filter(**state_dict)
	    search_results = search_results1 & search_results2 & search_results3
	    search_results = search_results.order_by('award_id').distinct('award_id')

	    context['search_results']= search_results
        else:
            print ("Error")
        return render(request, 'viewone/searchnsfawards.html', {'form': form, }, context)

def searchhospitals(request):
        context = RequestContext(request)
        form = SearchHospitals()
        flag = False
        context['flag'] = flag
        if request.method == 'POST':
            form = SearchHospitals(data=request.POST)
            flag = True
            context['flag'] = flag
        if form.is_valid():
            #Accessing the data in cleaned_data
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
	    county = form.cleaned_data['county']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
	    type_hospital = form.cleaned_data['desc']
	    owner = form.cleaned_data['owner']
	    trauma = form.cleaned_data['trauma']
	    min_beds = form.cleaned_data['min_beds']
	    #max_beds = form.cleaned_data['max_beds']
	    score = form.cleaned_data['score']
	    
            search_dict = {}
            if name :
                search_dict['name__istartswith']=name
            if city :
                search_dict['city__istartswith']=city
            if county:
		search_dict['county__istartswith']=county
	    if state :
                search_dict['state__istartswith']=state
            if zipcode :
                search_dict['zip__istartswith']=zipcode
	    if type_hospital:
		search_dict['type__icontains']=type_hospital
	    if owner:
		search_dict['owner__icontains']=owner
	    if trauma:
		search_dict['trauma__istartswith']=trauma
	    if min_beds:
		search_dict['beds__gte']=min_beds
	    if score:
		search_dict['score__gte']=score 

            search_results = HospitalsUsa.objects.filter(**search_dict).order_by('-score').exclude(score__isnull=True)
            context['search_results']= search_results
        else:
            print ("Error")
        return render(request, 'viewone/searchhospitals.html', {'form': form, }, context)

def hospital(request, hospital_id):
    hospital = get_object_or_404(HospitalsUsa, pk=hospital_id)
    return render(request, 'viewone/hospital.html', {'h': hospital})
