# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Ad

def create_ad(name, cost, days):
    """
    Create advertisment with given name and cost,
    published number of days offset tot now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Ad.objects.create(
        name = name,
        cost = cost,
        pub_date = time,
        buyer_id=1,
        category_id=1,
    )


class AdViewTests(TestCase):
    def test_index_view_with_no_ads(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No ads are available')
        self.assertQuerysetEqual(response.context['latest_ads_list'], [])

    def test_index_view_with_a_past_ad(self):
        """
        Advertisment with pub_date in the past
        should be displayed on the index page
        """
        create_ad(name='Прошлое объявление', cost=1234, days=-30)
        response = self.client.get(reverse('ads:index'))
        self.assertQuerysetEqual(
            response.context['latest_ads_list'],
            ['<Ad: Прошлое объявление>'],
        )

    def test_index_view_with_a_future_ad(self):
        """
        Advertisment with pub_date in the future
        should not be displayed on the index page
        """
        create_ad(name='Будущее объявление', cost=1234, days=30)
        response = self.client.get(reverse('ads:index'))
        self.assertContains(response, 'No ads are available.',
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_ads_list'], [], )

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future ads exist, only past ads
        should be displayed.
        """
        create_ad(name="Прошлое объявление", cost=1234, days=-30)
        create_ad(name="Будущее объявление", cost=1234, days=30)
        response = self.client.get(reverse('ads:index'))
        self.assertQuerysetEqual(
            response.context['latest_ads_list'],
            ['<Ad: Прошлое объявление>']
        )

    def test_index_view_with_two_past_ads(self):
        """
        2 advertisments with pub_date in the past
        should all be displayed on the index page
        """
        create_ad(name='Прошлое объявление 1', cost=1234, days=-30)
        create_ad(name='Прошлое объявление 2', cost=1234, days=-30)
        response = self.client.get(reverse('ads:index'))
        self.assertQuerysetEqual(
            response.context['latest_ads_list'],
            ['<Ad: Прошлое объявление 2>', '<Ad: Прошлое объявление 1>'],
        )


class AdMethodTests(TestCase):

    def test_was_published_recently_with_future_ad(self):
        """
        was_published_recently() should return False
        for ad whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_ad = Ad(pub_date = time)
        self.assertEqual(future_ad.was_published_recently(1), False)

    def test_was_published_recently_with_recent_ad(self):
        """
        was_published_recently() should return True
        for ad whose pub_date is in 1 hour earlier
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        early_ad = Ad(pub_date = time)
        self.assertEqual(early_ad.was_published_recently(1), True)

    def test_was_published_recently_with_old_ad(self):
        """
        was_published_recently() should return False
        for ad whose pub_date is very old
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_ad = Ad(pub_date = time)
        self.assertEqual(old_ad.was_published_recently(1), False)
