from django.shortcuts import render
from first_app.models import AccessRecord,Webpage,Topic

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)
