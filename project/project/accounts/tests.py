import logging
from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from project.accounts.models import Profile
from project.main.models import Article

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': 'niki123',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'profile_picture': 'http://test.picture/url.png',
        'position': Profile.PUBLIC_MEMBER
    }

    VALID_PROFILE_DATA_WITH_JOURNALIST = {
        'first_name': 'Test',
        'last_name': 'User',
        'profile_picture': 'http://test.picture/url.png',
        'position': Profile.JOURNALIST
    }

    VALID_ARTICLE_DATA = {
        'name': 'The pet',
        'category': Article.ECONOMICS,
        'image': 'url.png',
        'summary': 'Test summary',
        'journalist': UserModel,
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return user, profile

    def __create_valid_user_and_profile_for_staff(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA_WITH_JOURNALIST,
            user=user,
        )

        return user, profile

    def __create_article_for_user_with_authorities(self, user):
        article = Article.objects.create(
            **self.VALID_ARTICLE_DATA,
            user=user,
        )

        return article

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        pass
        # _, profile = self.__create_valid_user_and_profile()
        # self.__get_response_for_profile(profile)

        # user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        # profile = Profile.objects.create(
        #     **self.VALID_PROFILE_DATA,
        #     user=user,
        # )
        # response = self.client.get(reverse('profile details', kwargs={
        #     'pk': profile.pk,
        # }))
        #
        # self.assertTemplateUsed('accounts/profile_details.html')

    def test_when_user_is_journalist__expect_is_staff_to_be_true(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)

        self.assertTrue(response.context['is_owner'])