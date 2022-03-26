from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
'''def search_result(request):
    return render(request, 'buyer/search_result.html', {})'''

class search_result(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("search_result")
    template_name = "buyer/search_result.html"
