from django.db import models

class SpecialOfferEmail(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.email