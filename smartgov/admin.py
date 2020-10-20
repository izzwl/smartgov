from django.contrib import admin
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.urls import path,reverse
from django.shortcuts import redirect
from django import forms
import types
from .models import *

model_ordering = {
    "Input": 1,
    "Outcome": 2,
    "Output": 3,
    "Metode": 4,
    "Datasets": 5,
    "Groups": 0,
    "Users": 0,
}
class InputDataInline(admin.TabularInline):
    model = InputData
    extra = 1
    classes = ["tab-input-data-inline"]
class OutputDataInline(admin.TabularInline):
    model = OutputData
    extra = 1
    classes = ["tab-output-data-inline"]
    def has_add_permission(self,request):
        return False
    def has_change_permission(self,request,obj=None):
        return False
    def has_delete_permission(self,request,obj=None):
        return False    
class OutcomeDataInline(admin.TabularInline):
    model = OutcomeData
    extra = 1
    classes = ["tab-outcome-data-inline"]

class MasterAdmin(admin.ModelAdmin):
    def get_list_display(self,request):
        return [field.name for field in self.model._meta.fields if field.name != "id"]
class DatasetAdmin(DjangoTabbedChangeformAdmin,admin.ModelAdmin):
    change_list_template = 'smartgov/admin/changelist_dataset.html'

    def get_list_display(self,request):
        return [field.name for field in self.model._meta.fields if field.name != "id"]
    def has_add_permission(self,request):
        return False
    def has_change_permission(self,request,obj=None):
        return False
    def has_delete_permission(self,request,obj=None):
        return False
    
class EntryDatasetAdmin(DjangoTabbedChangeformAdmin,admin.ModelAdmin):
    change_form_template = 'smartgov/admin/change_entry_dataset.html'
    fields = ['metode']
    inlines = [InputDataInline,OutcomeDataInline,OutputDataInline]  
    def has_module_permission(self, request):
        return False
    def save_dataset(self,request,pk):
        pass      
    def changelist_view(self,request,extra_context=None):
        return redirect(reverse('admin:smartgov_dataset_changelist'))


def app_index(self, request, app_label, extra_context=None):
    app_dict = self._build_app_dict(request, app_label)
    # Sort the models alphabetically within each app.
    app_dict['models'].sort(key=lambda x: model_ordering[x['name']])
    context = {
        **self.each_context(request),
        'title': '%(app)s administration' % {'app': app_dict['name']},
        'app_list': [app_dict],
        'app_label': app_label,
        **(extra_context or {}),
    }

    request.current_app = self.name
    return TemplateResponse(request, self.app_index_template or [
        'admin/%s/app_index.html' % app_label,
        'admin/app_index.html'
    ], context)
    
def get_app_list(self,request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    # Sort the models alphabetically within each app.
    for app in app_list:
        app['models'].sort(key=lambda x: model_ordering[x['name']])
    return app_list

admin.site.register(Input,MasterAdmin)    
admin.site.register(Output,MasterAdmin)    
admin.site.register(Outcome,MasterAdmin)    
admin.site.register(Metode,MasterAdmin)    
admin.site.register(Dataset,DatasetAdmin)    
admin.site.register(EntryDataset,EntryDatasetAdmin)    
admin.site.get_app_list = types.MethodType(
    get_app_list,admin.site
)
admin.site.app_index = types.MethodType(
    app_index,admin.site
)
admin.site.site_header = 'SMART GOVERNANCE'