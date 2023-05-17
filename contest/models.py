from django.db import models
import uuid
from django.contrib.auth.models import User

# BASE MODEL CLASS 
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    created_at = models.DateTimeField(auto_now=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    deleted_at = models.DateTimeField(auto_now=True,)
    class Meta:
        abstract = True


# Category Model
class Categories(BaseModel):    
    title = models.CharField(max_length=250,null=False)
    thumbnail = models.ImageField(null=True)    
    def __str__(self):
        return self.title   
  
# CONTEST MODEL
class Contest(BaseModel):
    category = models.ForeignKey("Categories", related_name="category_contest", on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=False)
    description = models.CharField(max_length=50,null=False)
    thumbnail = models.ImageField(null=True)    
    def __str__(self):
        return self.title
    

# CONTEST INFORMATION MODEL
class ContestInformation(models.Model):    
    contest = models.OneToOneField("Contest", related_name="contest_information", on_delete=models.CASCADE,primary_key=True,)    
    
    firstPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    secondPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    thirdPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    Top50Price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    open = models.DateTimeField(auto_now=False, null=True)
    close = models.DateTimeField(auto_now=False,null=True )

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.contest.title

# QUESTION MODEL
class Questions(BaseModel):
    contest = models.ForeignKey("Contest", related_name="contest_question" ,on_delete=models.CASCADE,null=False)       
    question = models.CharField(max_length=250,null=False)    
    def __str__(self):
        return self.question

# ANSWER MODEL
class Answers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey("Questions", related_name="question_answer", on_delete=models.CASCADE)
    answer = models.CharField(max_length=250,null=False)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer

class Subscribe(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey("Contest", on_delete=models.CASCADE)
    Played = models.BooleanField(default=False)
    

