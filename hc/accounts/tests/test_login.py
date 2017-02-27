from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from hc.api.models import Check


class LoginTestCase(TestCase):

    def test_it_sends_link(self):
        check = Check()
        check.save()

        session = self.client.session
        session["welcome_code"] = str(check.code)
        session.save()
        self.old_user_count = User.objects.count()
        form = {"email": "alice@example.org"}

        r = self.client.post("/accounts/login/", form)
        assert r.status_code == 302

        link_confirmation = self.client.get('/accounts/login_link_sent/')
        self.assertContains(link_confirmation, "Login Link Sent")

        ### Assert that a user was created
        self.user_check = User.objects.filter(email="alice@example.org")
        self.assertEqual(self.user_check[0].email, form["email"])

        # And email sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Log in to healthchecks.io')
        ### Assert contents of the email body

        ### Assert that check is associated with the new user
        user = User.objects.get(email="alice@example.org")

        check_user = Check.objects.get(user=user)
        self.assertEqual(check_user.user, user)

    def test_it_pops_bad_link_from_session(self):
        self.client.session["bad_link"] = True
        self.client.get("/accounts/login/")
        assert "bad_link" not in self.client.session

        ### Any other tests?

