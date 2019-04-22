from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
CHOICES=(
	('Anthem','ANTHEM'),
	('Classical','CLASSICAL'),
	('Highlife','HIGHLIFE'),
	('Hymn','HYMN'),
)
class Post(models.Model):	
	title = models.CharField(max_length=100)
	composer = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	doc_file = models.FileField(upload_to='media/site_docs/')
	genre = models.CharField(choices=CHOICES, default='Anthem', max_length=30, null=True)
	new_price = models.IntegerField(default='0.00', null=True)
	sample_view= models.ImageField(default='/media/sample_score.jpg', upload_to='sample_sheet', null=False)


	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
			return reverse('post-detail', kwargs={'pk': self.pk})
	def save(self):
			super().save()

			img = Image.open(self.sample_view.path)

			if img.height > 300 or img.width > 300:
				output_size = (100, 100)
				img.thumbnail(output_size)
				img.save(self.sample_view.path)
