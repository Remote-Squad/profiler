from django.db import models


class Research(models.Model):
    query = models.CharField(max_length=255)
    data = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "research data on " + str(self.query)
