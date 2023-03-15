# Wire these new views into the polls.urls module by adding the following path() calls:
# Path: demo1/polls/urls.py
# Compare this snippet from demo1/polls/views.py:

from django.urls import path
from . import views

app_name = 'polls' # add namespaces to URLconf
urlpatterns = [
## ex: /polls/
    path('', views.index, name='index'),

## add the detail, results, and vote 
    
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
