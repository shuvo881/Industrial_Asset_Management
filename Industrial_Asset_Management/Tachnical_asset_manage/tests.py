from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Company
from .views import CompanyCreateView, CompanyListView, CompanyUpdateView, CompanyDeleteView, CompanyDetailView
from .forms import CompanyForm

class CompanyViewsTestCase(TestCase):
    def setUp(self):
        # Create a sample company for testing
        self.company = Company.objects.create(name='Test Company', description='This is a test company.')

    def test_company_create_view(self):
        request = RequestFactory().get(reverse('company_create'))
        response = CompanyCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_company_list_view(self):
        request = RequestFactory().get(reverse('company_list'))
        response = CompanyListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_company_update_view(self):
        request = RequestFactory().get(reverse('company_update', kwargs={'pk': self.company.pk}))
        response = CompanyUpdateView.as_view()(request, pk=self.company.pk)
        self.assertEqual(response.status_code, 200)

    def test_company_delete_view(self):
        request = RequestFactory().get(reverse('company_delete', kwargs={'pk': self.company.pk}))
        response = CompanyDeleteView.as_view()(request, pk=self.company.pk)
        self.assertEqual(response.status_code, 200)

    def test_company_detail_view(self):
        request = RequestFactory().get(reverse('company_details', kwargs={'pk': self.company.pk}))
        response = CompanyDetailView.as_view()(request, pk=self.company.pk)
        self.assertEqual(response.status_code, 200)

    def test_company_create_form_valid(self):
        form_data = {'name': 'New Company', 'description': 'A new test company.'}
        form = CompanyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_company_create_form_invalid(self):
        form_data = {'name': '', 'description': 'Invalid company without a name.'}
        form = CompanyForm(data=form_data)
        self.assertFalse(form.is_valid())


# same as all testing