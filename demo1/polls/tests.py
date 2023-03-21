
# Create your tests here. can test both function and interface

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30) # add 30 days, why we need this is because we can use this function in admin.py, the (day=1) is the time range
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) # assertit is a function to test, if the result is true, then it will pass, if false, then it will fail
