# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AbsAwardid(models.Model):
    abs_number = models.IntegerField(blank=True, null=True)
    award = models.CharField(max_length=25, blank=True, null=True)
    award_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abs_awardid'


class AbsKeywords(models.Model):
    abs_number = models.IntegerField(blank=True, null=True)
    dic = models.CharField(max_length=250, blank=True, null=True)
    facet = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abs_keywords'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authortable1Pubmed(models.Model):
    author_name = models.CharField(max_length=60, blank=True, null=True)
    complete_addr = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    tools_used = models.CharField(max_length=30, blank=True, null=True)
    pmid = models.IntegerField()
    author_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authortable1_pubmed'


class AuthortableTest(models.Model):
    author_name = models.CharField(max_length=60, blank=True, null=True)
    complete_addr = models.TextField(blank=True, null=True)
    pubmed_id = models.CharField(max_length=20, blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    tools_used = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authortable_test'


class BusinesspatternsZipcodeUsa(models.Model):
    geo_id = models.CharField(max_length=32767, blank=True, null=True)
    geo_id2 = models.CharField(max_length=32767, blank=True, null=True)
    geo_displaylabel = models.CharField(max_length=32767, blank=True, null=True)
    naics_id = models.CharField(max_length=32767, blank=True, null=True)
    naic_sectorinfo = models.CharField(max_length=32767, blank=True, null=True)
    year_id = models.CharField(max_length=32767, blank=True, null=True)
    estab = models.CharField(max_length=32767, blank=True, null=True)
    emp = models.CharField(max_length=32767, blank=True, null=True)
    payqtr1 = models.CharField(max_length=32767, blank=True, null=True)
    payann = models.CharField(db_column='PAYANN', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    payann_simplified = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cbp_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businesspatterns_zipcode_usa'


class CikList(models.Model):
    co_name = models.CharField(max_length=1000, blank=True, null=True)
    cik_no = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cik_list'


class CitiesPopulationUsa(models.Model):
    sumlev = models.CharField(db_column='SUMLEV', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='COUNTY', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(db_column='PLACE', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    cousub = models.CharField(db_column='COUSUB', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    concit = models.CharField(db_column='CONCIT', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    primgeo_flag = models.CharField(db_column='PRIMGEO_FLAG', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    funcstat = models.CharField(db_column='FUNCSTAT', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    stname = models.CharField(db_column='STNAME', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    census2010pop = models.CharField(db_column='CENSUS2010POP', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    estimatesbase2010 = models.CharField(db_column='ESTIMATESBASE2010', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    popestimate2010 = models.CharField(db_column='POPESTIMATE2010', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    popestimate2011 = models.CharField(db_column='POPESTIMATE2011', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    popestimate2012 = models.CharField(db_column='POPESTIMATE2012', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    popestimate2013 = models.CharField(db_column='POPESTIMATE2013', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    popestimate2014 = models.CharField(db_column='POPESTIMATE2014', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    popestimate2015 = models.CharField(db_column='POPESTIMATE2015', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    population_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_population_usa'


class CitiesUsa(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32767, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=32767, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_usa'


class ClinTrials(models.Model):
    nct_no = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    recruitment = models.CharField(max_length=250, blank=True, null=True)
    study_results = models.CharField(max_length=1000, blank=True, null=True)
    conditions = models.CharField(max_length=1000, blank=True, null=True)
    interventions = models.CharField(max_length=2500, blank=True, null=True)
    sponsor_collaborators = models.CharField(db_column='sponsor/collaborators', max_length=2500, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=25, blank=True, null=True)
    age = models.CharField(max_length=250, blank=True, null=True)
    phases = models.CharField(max_length=2500, blank=True, null=True)
    enrollment_no = models.SmallIntegerField(blank=True, null=True)
    funded_by = models.CharField(max_length=1000, blank=True, null=True)
    study_type = models.CharField(max_length=2500, blank=True, null=True)
    study_design = models.CharField(max_length=2500, blank=True, null=True)
    other_ids = models.CharField(max_length=25, blank=True, null=True)
    first_received = models.CharField(max_length=25, blank=True, null=True)
    start_date = models.CharField(max_length=25, blank=True, null=True)
    completion_date = models.CharField(max_length=25, blank=True, null=True)
    last_update = models.CharField(max_length=25, blank=True, null=True)
    last_verified = models.CharField(max_length=25, blank=True, null=True)
    acronym = models.CharField(max_length=25, blank=True, null=True)
    results_first_received = models.CharField(max_length=2500, blank=True, null=True)
    primary_compl_date = models.CharField(max_length=25, blank=True, null=True)
    outcome_measures = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clin_trials'


class CompanyDataTicker(models.Model):
    symbol = models.CharField(max_length=25, blank=True, null=True)
    co_name = models.CharField(max_length=250, blank=True, null=True)
    markert_cap = models.CharField(max_length=25, blank=True, null=True)
    sector = models.CharField(max_length=250, blank=True, null=True)
    industry = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_data_ticker'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DomainsUniversities(models.Model):
    alpha_two_code = models.CharField(max_length=32767, blank=True, null=True)
    country = models.CharField(max_length=32767, blank=True, null=True)
    domain = models.CharField(max_length=32767, blank=True, null=True)
    name = models.CharField(max_length=32767, blank=True, null=True)
    web_page = models.CharField(max_length=32767, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domains_universities'


class FacetsWex(models.Model):
    file = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    city_state = models.CharField(max_length=2000, blank=True, null=True)
    gene_technique = models.CharField(max_length=2000, blank=True, null=True)
    gene_tools = models.CharField(max_length=250, blank=True, null=True)
    authors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facets_wex'


class Fortune1000(models.Model):
    rank = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    co_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fortune1000'


class GenomicsCo(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genomics_co'


class HealthcareCo(models.Model):
    co_name = models.CharField(max_length=300, blank=True, null=True)
    ticker = models.CharField(max_length=25, blank=True, null=True)
    st_address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    telephone = models.CharField(max_length=25, blank=True, null=True)
    fax = models.CharField(max_length=25, blank=True, null=True)
    co_email = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    puborprivate = models.CharField(max_length=25, blank=True, null=True)
    no_emp = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    sic_code = models.CharField(max_length=250, blank=True, null=True)
    hq = models.CharField(max_length=25, blank=True, null=True)
    sales = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'healthcare_co'


class HospitalsSurveyratingUsa(models.Model):
    provider_id = models.CharField(db_column='Provider ID', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hospital_name = models.CharField(db_column='Hospital Name', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.CharField(db_column='Address', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=32767, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(db_column='ZIP Code', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='County Name', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='Phone Number', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hospital_type = models.CharField(db_column='Hospital Type', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hospital_ownership = models.CharField(db_column='Hospital Ownership', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emergency_services = models.CharField(db_column='Emergency Services', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meets_criteria_for_meaningful_use_of_ehrs = models.CharField(db_column='Meets criteria for meaningful use of EHRs', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hospital_overall_rating = models.CharField(db_column='Hospital overall rating', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hospital_overall_rating_footnote = models.CharField(db_column='Hospital overall rating footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mortality_national_comparison = models.CharField(db_column='Mortality national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mortality_national_comparison_footnote = models.CharField(db_column='Mortality national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    safety_of_care_national_comparison = models.CharField(db_column='Safety of care national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    safety_of_care_national_comparison_footnote = models.CharField(db_column='Safety of care national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    readmission_national_comparison = models.CharField(db_column='Readmission national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    readmission_national_comparison_footnote = models.CharField(db_column='Readmission national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_experience_national_comparison = models.CharField(db_column='Patient experience national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    patient_experience_national_comparison_footnote = models.CharField(db_column='Patient experience national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    effectiveness_of_care_national_comparison = models.CharField(db_column='Effectiveness of care national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    effectiveness_of_care_national_comparison_footnote = models.CharField(db_column='Effectiveness of care national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    timeliness_of_care_national_comparison = models.CharField(db_column='Timeliness of care national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    timeliness_of_care_national_comparison_footnote = models.CharField(db_column='Timeliness of care national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    efficient_use_of_medical_imaging_national_comparison = models.CharField(db_column='Efficient use of medical imaging national comparison', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    efficient_use_of_medical_imaging_national_comparison_footnote = models.CharField(db_column='Efficient use of medical imaging national comparison footnote', max_length=32767, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    beds = models.CharField(max_length=32767, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospitals_surveyrating_usa'


class HospitalsUsa(models.Model):
    x = models.CharField(max_length=32767, blank=True, null=True)
    y = models.CharField(max_length=32767, blank=True, null=True)
    fid = models.CharField(max_length=32767, blank=True, null=True)
    id = models.CharField(max_length=32767, blank=True, null=True)
    name = models.CharField(max_length=32767, blank=True, null=True)
    address = models.CharField(max_length=32767, blank=True, null=True)
    address2 = models.CharField(max_length=32767, blank=True, null=True)
    city = models.CharField(max_length=32767, blank=True, null=True)
    state = models.CharField(max_length=32767, blank=True, null=True)
    zip = models.CharField(max_length=32767, blank=True, null=True)
    zip4 = models.CharField(max_length=32767, blank=True, null=True)
    telephone = models.CharField(max_length=32767, blank=True, null=True)
    type = models.CharField(max_length=32767, blank=True, null=True)
    status = models.CharField(max_length=32767, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=32767, blank=True, null=True)
    countyfips = models.CharField(max_length=32767, blank=True, null=True)
    country = models.CharField(max_length=32767, blank=True, null=True)
    latitude = models.CharField(max_length=32767, blank=True, null=True)
    longtitude = models.CharField(max_length=32767, blank=True, null=True)
    naics_code = models.CharField(max_length=32767, blank=True, null=True)
    naics_desc = models.CharField(max_length=32767, blank=True, null=True)
    source = models.CharField(max_length=32767, blank=True, null=True)
    source_dat = models.CharField(max_length=32767, blank=True, null=True)
    val_method = models.CharField(max_length=32767, blank=True, null=True)
    val_date = models.CharField(max_length=32767, blank=True, null=True)
    website = models.CharField(max_length=32767, blank=True, null=True)
    state_id = models.CharField(max_length=32767, blank=True, null=True)
    alt_name = models.CharField(max_length=32767, blank=True, null=True)
    st_fips = models.CharField(max_length=32767, blank=True, null=True)
    owner = models.CharField(max_length=32767, blank=True, null=True)
    ttl_staff = models.CharField(max_length=32767, blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    trauma = models.CharField(max_length=32767, blank=True, null=True)
    helipad = models.CharField(max_length=32767, blank=True, null=True)
    date_created = models.CharField(max_length=32767, blank=True, null=True)
    bed_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cbpscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    populationscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospitals_usa'


class IbmTruth(models.Model):
    co_name = models.CharField(max_length=500, blank=True, null=True)
    web_site = models.CharField(max_length=250, blank=True, null=True)
    hq_phone = models.CharField(max_length=25, blank=True, null=True)
    co_email = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sic_code = models.CharField(max_length=500, blank=True, null=True)
    sales = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    it_budget = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    sales_growth = models.CharField(max_length=250, blank=True, null=True)
    fiscal_year_end = models.CharField(max_length=25, blank=True, null=True)
    no_employees = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    fortune_rank = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    hq_street = models.CharField(max_length=500, blank=True, null=True)
    hq_city = models.CharField(max_length=250, blank=True, null=True)
    hq_state = models.CharField(max_length=25, blank=True, null=True)
    hq_zip = models.CharField(max_length=12, blank=True, null=True)
    pub_priv = models.CharField(max_length=25, blank=True, null=True)
    dnus_no = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    duns_parent = models.CharField(max_length=25, blank=True, null=True)
    twitter_link = models.CharField(max_length=250, blank=True, null=True)
    linkedin = models.CharField(max_length=250, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    symbol = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ibm_truth'


class Keywords(models.Model):
    id = models.IntegerField(blank=True, null=True)
    descriptor = models.CharField(max_length=500, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Lex2(models.Model):
    co_name = models.CharField(max_length=100, blank=True, null=True)
    ticker = models.CharField(max_length=25, blank=True, null=True)
    st_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    fax = models.CharField(max_length=25, blank=True, null=True)
    company_email_address = models.CharField(db_column='company email address', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    url = models.CharField(max_length=50, blank=True, null=True)
    pub_private = models.CharField(max_length=25, blank=True, null=True)
    employees = models.CharField(max_length=25, blank=True, null=True)
    sic = models.CharField(max_length=50, blank=True, null=True)
    headquarters = models.CharField(max_length=25, blank=True, null=True)
    naics = models.CharField(max_length=250, blank=True, null=True)
    sales = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lex_2'


class LinkedinBusiness(models.Model):
    co_name = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=750, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linkedin_business'


class MedDevice(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)
    ticker = models.CharField(max_length=25, blank=True, null=True)
    st_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=25, blank=True, null=True)
    fax = models.CharField(max_length=25, blank=True, null=True)
    co_email = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    puborprivate = models.CharField(max_length=25, blank=True, null=True)
    no_emp = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    sic_code = models.CharField(max_length=250, blank=True, null=True)
    hq = models.CharField(max_length=25, blank=True, null=True)
    sales = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'med_device'


class NamedEntity(models.Model):
    id = models.IntegerField(blank=True, null=True)
    descriptor = models.CharField(max_length=250, blank=True, null=True)
    value = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'named_entity'


class NsfawardsAuthors(models.Model):
    award = models.ForeignKey('NsfawardsTest1', models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    author_role = models.CharField(max_length=50, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nsfawards_authors'


class NsfawardsTest1(models.Model):
    award_title = models.TextField(blank=True, null=True)
    award_start_date = models.DateField(blank=True, null=True)
    award_end_date = models.DateField(blank=True, null=True)
    award_amount = models.IntegerField(blank=True, null=True)
    award_instrument = models.CharField(max_length=40, blank=True, null=True)
    organization_code = models.IntegerField(blank=True, null=True)
    org_directorate = models.CharField(max_length=31, blank=True, null=True)
    program_manager = models.CharField(max_length=35, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    initial_amendment_date = models.DateField(blank=True, null=True)
    latest_amendment_date = models.DateField(blank=True, null=True)
    award_id = models.IntegerField(primary_key=True)
    institution_name = models.CharField(max_length=70, blank=True, null=True)
    institution_city = models.CharField(max_length=30, blank=True, null=True)
    institution_zipcode = models.CharField(max_length=10, blank=True, null=True)
    institution_phone_number = models.BigIntegerField(blank=True, null=True)
    institution_street_address = models.CharField(max_length=50, blank=True, null=True)
    institution_country = models.CharField(max_length=25, blank=True, null=True)
    institution_state = models.CharField(max_length=20, blank=True, null=True)
    institution_state_code = models.CharField(max_length=2, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    mesh_terms = models.CharField(max_length=2000, blank=True, null=True)
    gene_tools = models.CharField(max_length=500, blank=True, null=True)
    gene_techniques = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nsfawards_test1'


class Pharma(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)
    ticker = models.CharField(max_length=25, blank=True, null=True)
    st_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=25, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=25, blank=True, null=True)
    fax = models.CharField(max_length=25, blank=True, null=True)
    co_email = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    puborprivate = models.CharField(max_length=100, blank=True, null=True)
    no_emp = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    sic_code = models.CharField(max_length=350, blank=True, null=True)
    hq = models.CharField(max_length=25, blank=True, null=True)
    sales = models.DecimalField(max_digits=250, decimal_places=0, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharma'


class PubmedidTitles(models.Model):
    generated_id = models.CharField(max_length=20, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    pmid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pubmedid_titles'


class ResearchAuthorTruth(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    university_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research_author_truth'


class Sales(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)
    sales = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class SecForms2016(models.Model):
    form_type = models.CharField(max_length=100, blank=True, null=True)
    co_name = models.CharField(max_length=500, blank=True, null=True)
    cik = models.CharField(max_length=25, blank=True, null=True)
    date_filed = models.CharField(max_length=100, blank=True, null=True)
    file_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_forms_2016'


class SecIndex(models.Model):
    cik_no = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    co_name = models.CharField(max_length=1000, blank=True, null=True)
    form_type = models.CharField(max_length=25, blank=True, null=True)
    date_filed = models.CharField(max_length=25, blank=True, null=True)
    fike_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_index'


class StatesUsa(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states_usa'


class Test(models.Model):
    co_name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class TestTrgm(models.Model):
    text = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_trgm'


class TrunkList(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trunk_list'


class WexDataii(models.Model):
    id = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    company_location = models.CharField(max_length=2000, blank=True, null=True)
    company_name = models.CharField(max_length=500, blank=True, null=True)
    email3 = models.CharField(max_length=2000, blank=True, null=True)
    email4 = models.CharField(max_length=1000, blank=True, null=True)
    gene_techniques = models.CharField(max_length=100, blank=True, null=True)
    gene_tools = models.CharField(max_length=25, blank=True, null=True)
    money = models.CharField(max_length=100, blank=True, null=True)
    name_initial_name = models.CharField(max_length=2000, blank=True, null=True)
    name_name = models.CharField(max_length=1000, blank=True, null=True)
    named_companies = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=25, blank=True, null=True)
    date = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_facet_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wex_dataII'
