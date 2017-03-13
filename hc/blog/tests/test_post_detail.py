from hc.blog.models import Post, Category
from hc.test import BaseTestCase


class TestBlogDetail(BaseTestCase):

    def setUp(self):
        super(TestBlogDetail, self).setUp()

    def test_blog_page_works(self):
        post = Post.objects.create(author=self.alice)
        blog_post = self.client.get("/blog/post/{0}/".format(post.id))

        assert blog_post.status_code == 200

    def test_invalid_blog_page(self):
        # Create new blog, access +1 param, assert 404
        post = Post.objects.create(author=self.alice)
        blog_post = self.client.get("/blog/post/{0}/".format(post.id+1))

        assert blog_post.status_code == 404

    def test_edit_blog(self):
        # Set alice to become a superuser in order for her to edit
        self.alice.is_superuser = True
        self.alice.is_staff = True
        self.alice.save()

        self.client.login(username="alice", password="password")
        # Create a blog
        post = Post.objects.create(author=self.alice)

        edit_form_page = self.client.get("/blog/post/{0}/edit/".format(post.id))
        assert edit_form_page.status_code == 200

        bad_edit_form_page = self.client.get("/blog/post/{0}/edit/".format(post.id+1))
        assert bad_edit_form_page.status_code == 404

        # Submit post that has been edited
        data = {
            "title": "Testing",
            "text": "Life of pie"
        }

        submitted_edit = self.client.post("/blog/post/{0}/edit/".format(post.id), data)
        post.refresh_from_db()

        assert post.title == data["title"]
        assert post.text == data["text"]

    def test_new_blog(self):
        pass

