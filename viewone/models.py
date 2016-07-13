from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IbmTruth(models.Model):
    co_name = models.CharField(primary_key=True, max_length=500)
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

    def __str__(self):
	return self.co_name

    class Meta:
        managed = False
        db_table = 'ibm_truth'

class AuthortableTest(models.Model):
    author_name = models.CharField(max_length=60, primary_key=True)
    complete_addr = models.TextField(blank=True, null=True)
    pubmed_id = models.CharField(max_length=20)
    department = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    tools_used = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.author_name

    class Meta:
        managed = False
        db_table = 'authortable_test'
	unique_together = (("author_name","pubmed_id"),)

class PubmedTitles(models.Model):
    pubmed_id = models.CharField(max_length=20, primary_key=True)
    title = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pubmed_id

    class Meta:
        managed = False
        db_table = 'pubmed_titles'

class PubmedAuthor(models.Model):
    author_name = models.CharField(max_length=60, primary_key=True)
    complete_addr = models.TextField(blank=True, null=True)
    pmid = models.DecimalField(max_digits=25, decimal_places=0)
    department = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    tools_used = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.author_name

    class Meta:
        managed = False
        db_table = 'authortable1_pubmed'
        unique_together = (("author_name","pmid"),)