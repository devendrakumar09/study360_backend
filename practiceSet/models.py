from django.db import models
import uuid
# Create your models here.

class MainCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    title = models.CharField(max_length=250,null=False)
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    deleted_at = models.DateTimeField(auto_now=True,)
    
    def __str__(self):
        return self.title   



class Categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    cat =  models.ForeignKey("MainCategory", related_name="main_category" , on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250,null=False)
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    deleted_at = models.DateTimeField(auto_now=True,)
    
    def __str__(self):
        return self.title   
  

class Set(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey("Categories", related_name="category_set", on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=False)
    description = models.CharField(max_length=50,null=False)
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    deleted_at = models.DateTimeField(auto_now=True,)
    
    def __str__(self):
        return self.title

class Queston(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    set = models.ForeignKey("Set", related_name="set_question", on_delete=models.CASCADE)
    question = models.CharField(max_length=250,null=False)
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    deleted_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.question

class Answers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey("Queston", related_name="question_answer", on_delete=models.CASCADE)
    answer = models.CharField(max_length=250,null=False)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    deleted_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.answer
