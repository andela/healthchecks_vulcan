from hc.blog.models import Post, Category
from hc.test import BaseTestCase


class TestPostList(BaseTestCase):

    def setUp(self):
        pass

    def test_post_list_page_works(self):
        blog_page = self.client.get("/blog/")
        assert blog_page.status_code == 200

    def test_post_url_param_same_as_database(self):
        pass


