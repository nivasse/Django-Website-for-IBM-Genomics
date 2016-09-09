# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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


class CikList(models.Model):
    co_name = models.CharField(max_length=1000, blank=True, null=True)
    cik_no = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cik_list'


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


class Fortune1000(models.Model):
    rank = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    co_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fortune1000'


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

    class Meta:
        managed = False
        db_table = 'healthcare_co'


class HealthcareTruth(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    genetic_testing = models.CharField(max_length=25, blank=True, null=True)
    url = models.CharField(max_length=25, blank=True, null=True)
    population = models.CharField(max_length=25, blank=True, null=True)
    tools_used = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'healthcare_truth'


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

    class Meta:
        managed = False
        db_table = 'ibm_truth'


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

    class Meta:
        managed = False
        db_table = 'med_device'


class NamedCompanies(models.Model):
    ticker = models.CharField(max_length=25, blank=True, null=True)
    co_name = models.CharField(max_length=300, blank=True, null=True)
    last_sale = models.CharField(max_length=25, blank=True, null=True)
    market_cap = models.CharField(max_length=25, blank=True, null=True)
    ipo_year = models.CharField(max_length=25, blank=True, null=True)
    sector = models.CharField(max_length=1000, blank=True, null=True)
    industry = models.CharField(max_length=1000, blank=True, null=True)
    summary_quote = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'named_companies'


class NsfawardsAuthors(models.Model):
    award = models.ForeignKey('NsfawardsTest1', models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    author_role = models.CharField(max_length=50, blank=True, null=True)

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
    institution_zipcode = models.BigIntegerField(blank=True, null=True)
    institution_phone_number = models.BigIntegerField(blank=True, null=True)
    institution_street_address = models.CharField(max_length=50, blank=True, null=True)
    institution_country = models.CharField(max_length=25, blank=True, null=True)
    institution_state = models.CharField(max_length=20, blank=True, null=True)
    institution_state_code = models.CharField(max_length=2, blank=True, null=True)

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

    class Meta:
        managed = False
        db_table = 'pharma'


class Pubmed2(models.Model):
    record = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    institution = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    tools_used = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pubmed2'


class PubmedidTitles(models.Model):
    generated_id = models.CharField(max_length=20, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    pmid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pubmedid_titles'


class Sales(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)
    sales = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class SecIndex(models.Model):
    cik_no = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    co_name = models.CharField(max_length=1000, blank=True, null=True)
    form_type = models.CharField(max_length=25, blank=True, null=True)
    date_filed = models.CharField(max_length=25, blank=True, null=True)
    fike_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_index'


class Test(models.Model):
    co_name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class TrunkList(models.Model):
    co_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trunk_list'
