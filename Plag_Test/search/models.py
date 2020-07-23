from django.db import models

# Create your models here.
class result_insert(models.Model):
    Q_id = models.AutoField(primary_key=True)
    Question = models.CharField(max_length=100)
    Option_1 = models.CharField(max_length=100)
    Option_2 = models.CharField(max_length=100)
    Option_3 = models.CharField(max_length=100)
    Option_4 = models.CharField(max_length=100)
    Option_5 = models.CharField(max_length=100)
    Reason_if_match_percent_greater_than_50 = models.CharField(max_length=300)
    objects=models.Manager()
    class Meta:
        db_table="post_check_results"

    def __str__(self):
        return self.Question