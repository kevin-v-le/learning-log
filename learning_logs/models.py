from django.db import models

# Create your models here.
class Topic(models.Model):
    """ a topic the user is learning about."""
    text = models.CharField(max_length=200) #attribute 1
    date_added = models.DateTimeField(auto_now_add=True) #attribute 2

    def __str__(self):
        """ return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """journal entries for a specific topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
