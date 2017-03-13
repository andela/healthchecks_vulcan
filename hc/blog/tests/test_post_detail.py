from hc.blog.models import Post, Category
from hc.test import BaseTestCase


class TestBlogDetail(BaseTestCase):

    def setUp(self):
        super(TestBlogDetail, self).setUp()

    def test_blog_page_works(self):
        # Create new blog, access it using url, assert 200
        post = Post.objects.create(author=self.alice)
        blog_post = self.client.get("/blog/post/{0}/".format(post.id))

        assert blog_post.status_code == 200

    def test_invalid_blog_page(self):
        # Create new blog, access +1 param, assert 404
        pass

