from django.db import models


class Data(models.Model):
    # id = models.IntegerField(primary_key=True, db_index=True) # 게시글 고유 ID
    username = models.TextField(null=False)
    data = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.data)
