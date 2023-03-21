# Wire these new views into the polls.urls module by adding the following path() calls:
# Path: demo1/polls/urls.py
# Compare this snippet from demo1/polls/views.py:

from django.urls import path

from .views import IndexView, QuestionDetail, vote, ResultsView

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', QuestionDetail.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
   path('<int:question_id>/vote/', vote, name='vote'),
]

## add the detail, results, and vote 
    
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # # ex: /polls/test/
    # path('test/', views.test, name='test')

