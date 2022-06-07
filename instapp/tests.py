from django.test import TestCase

from .models import Profile, Post, Comment
from django.contrib.auth.models import User

#Create your tests here.

class Test_Profile(TestCase):
    '''
    Class test to test model profile
    '''
    def setUp(self):
        self.user = User(username='moh')
        self.user.save()

        self.profile_test = Profile(id=1, name='my default', profile_picture='default_1.jpg', bio='My bio should be tested',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

class Test_Comment(TestCase):
    """
    Class to test the comments model
    """
    def setUp(self):
        
        self.new_user = User(username = "Moh")
        self.new_user.save()
        self.new_post =Post(name = 'Moh', user = self.new_user)
        self.new_post.save_image()
        self.new_comment = Comment(comment = "default comment", post = self.new_post)

    
    def test_is_instance(self):
        
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_init(self):
        
        self.assertTrue(self.new_comment.comment == "default comment")

    def test_save_comment(self):

        self.new_comment.save()
        self.assertTrue(len(Comment.objects.all()) > 0)

    def test_delete_comment(self):
        """
        This will test whether the comment is deleted
        """
        self.new_comment.save()
        self.assertTrue(len(Comment.objects.all()) > 0)
        self.new_comment.delete()
        self.assertTrue(len(Comment.objects.all()) == 0)


class Test_Post(TestCase):
    '''
    Class to test the Post model
    '''
    def setUp(self):
        self.profile_test = Profile(name='Maya Meta', user=User(username='Maya'))
        self.profile_test.save()

        self.post_test = Post(image='insta.jpeg', name='for maya', caption='caption test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, Post))

    def test_save_image(self):
        self.post_test.save_image()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_image(self):
        self.post_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)

    def tearDown(self):
        
        User.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()