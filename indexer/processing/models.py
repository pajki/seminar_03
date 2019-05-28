from django.db import models


class IndexWord(models.Model):
    word = models.TextField(max_length=255, primary_key=True)

    def __str__(self):
        return "Index word {}".format(self.word)


class Posting(models.Model):

    class Meta:
        unique_together = ["word", "document_name"]

    word = models.ForeignKey(IndexWord, on_delete=models.CASCADE)
    document_name = models.TextField(max_length=255)
    frequency = models.IntegerField()
    indexes = models.TextField(max_length=255)

    def __str__(self):
        return "Posting {} with {}".format(self.document_name, self.word)
