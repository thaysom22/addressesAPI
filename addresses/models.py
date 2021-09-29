from django.db import models
from django.contrib.auth import get_user_model


class Address(models.Model):
	user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, 
        related_name='addresses'
    )
	address1 = models.CharField(max_length=300, blank=True)
	address2 = models.CharField(max_length=300, blank=True)
	city = models.CharField(max_length=100, blank=True)
	region = models.CharField(max_length=100, blank=True)
	postcode = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		# specify ordering at DB level
		ordering = ['-created_at']
		verbose_name_plural = "addresses"
		# unique addresses for each user enforced at DB level
		unique_together = ['user', 'address1', 'address2',
            'city', 'region', 'postcode', 'country'] 

	def __str__(self):
		return f"{self.user}:{self.postcode}:{self.created_at}"
