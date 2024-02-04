from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import CompanyForm, EmployeeForm, DeviceForm, DeviceTransectionForm
from .models import Company, Employee, Device, DeviceTransection

# for Company

class BaseCompnayView(FormView):
    form_class = CompanyForm
    model = Company
    context_object_name = 'company'
    template_name = "company _create.html"
    success_url = reverse_lazy('company_list')
    
class CompanyListView(BaseCompnayView, ListView):
    context_object_name = 'companies'
    template_name='company_list.html'
    paginate_by = 10

class CompanyCreateView(BaseCompnayView, CreateView):
    pass


class CompanyUpdateView(BaseCompnayView, UpdateView):
    pass

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


class CompanyDetailView(BaseCompnayView, DetailView):
    template_name = "company_details.html"



# For Employee

class BaseEmployeeView(FormView):
    form_class = EmployeeForm
    model = Employee
    context_object_name = 'employee'
    template_name = "employee _create.html"
    success_url = reverse_lazy('employee_list')
    
class EmployeeListView(BaseEmployeeView, ListView):
    context_object_name = 'employees'
    template_name='employee_list.html'
    paginate_by = 10

class EmployeeCreateView(BaseEmployeeView, CreateView):
    pass


class EmployeeUpdateView(BaseEmployeeView, UpdateView):
    pass

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')


class EmployeeDetailView(BaseEmployeeView, DetailView):
    template_name = "employee_details.html"


# For Device

class BaseDeviceView(FormView):
    form_class = DeviceForm
    model = Device
    context_object_name = 'device'
    template_name = "device_create.html"
    success_url = reverse_lazy('device_list')
    
class DeviceListView(BaseDeviceView, ListView):
    context_object_name = 'devices'
    template_name='device_list.html'
    paginate_by = 10

class DeviceCreateView(BaseDeviceView, CreateView):
    pass


class DeviceUpdateView(BaseDeviceView, UpdateView):
    pass

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'device_confirm_delete.html'
    success_url = reverse_lazy('device_list')


class DeviceDetailView(BaseDeviceView, DetailView):
    template_name = "device_details.html"



# For DeviceTransection

class BaseDeviceTransectionView(FormView):
    form_class = DeviceTransectionForm
    model = DeviceTransection
    context_object_name = 'device_transection'
    template_name = "device_trans_create.html"
    success_url = reverse_lazy('device_trans_list')
    
class DeviceTransectionListView(BaseDeviceTransectionView, ListView):
    context_object_name = 'device_transections'
    template_name='device_trans_list.html'
    paginate_by = 10

class DeviceTransectionCreateView(BaseDeviceTransectionView, CreateView):
    pass


class DeviceTransectionUpdateView(BaseDeviceTransectionView, UpdateView):
    pass

class DeviceTransectionDeleteView(DeleteView):
    model = DeviceTransection
    template_name = 'device_trans_confirm_delete.html'
    success_url = reverse_lazy('device_trans_list')


class DeviceTransectionDetailView(BaseDeviceTransectionView, DetailView):
    template_name = "device_trans_details.html"
    
    

class Home(TemplateView):
    template_name = "index.html"
