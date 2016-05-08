import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Question

def create_question(question_text, days):
        """
        Create Question based on the question_text and days
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTest(TestCase):
    def test_index_without_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('mysite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No available')
        self.assertQuerysetEqual(response.context['latest_question_list', []])

    def test_index_with_past_question(self):
        """
        question with past pub_date should be on the page
        """
        create_question('Question in the past?', days=-30)
        response = self.client.get(reverse('mysite:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Question in the past?>'])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question('future question', days=30)
        create_question('past question', days=-30)
        response = self.client.get(reverse('mysite:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: past question>'])

    def test_index_view_with_two_past_questions(self):
        """
        The question index page may display multiple questions
        """
        create_question('past question 1', days=-30)
        create_question('pasr question 2', days=-5)
        response = self.client.get(reverse('mysite:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: past question 1>', '<Question: past question 2>'])


class QuestionMethodTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        Should return false for questions in the future
        """
        time = timezone.now() - datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
    def test_was_published_recently_with_recent_question(self):
        """
        Returnt true for questions written in -1 day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_questions = Question(pub_date=time)
        self.assertEqual(recent_questions.was_published_recently(), True)
