from hc.api.models import Check
from hc.test import BaseTestCase


class PauseTestCase(BaseTestCase):

    def test_it_works(self):
        check = Check(user=self.alice, status="up")
        check.save()

        url = "/api/v1/checks/%s/pause" % check.code
        r = self.client.post(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        ### Assert the expected status code and check's status
        self.assertEqual(200, r.status_code,
                         msg="For a successful request, the status code should be 200")
        check.refresh_from_db()
        self.assertEqual("paused", check.status,
                         msg="The status should be paused for a paused check")


    def test_it_validates_ownership(self):
        check = Check(user=self.bob, status="up")
        check.save()

        url = "/api/v1/checks/%s/pause" % check.code
        r = self.client.post(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 400)

        ### Test that it only allows post requests
        # Use a user with an api key just to be sure the request method is the only variant
        check = Check(user=self.alice, status="up")
        check.save()

        r = self.client.get(url, "", content_type="application/json",
                            HTTP_X_API_KEY="abc")

        self.assertEqual(405, r.status_code,
                         msg="For a non-POST request, the status should be 405")
