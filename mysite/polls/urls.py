from django.urls import path
from . import views

# namespacing URL names
# detail -> <namespace>:detail (in views) when using links
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

'''
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''

