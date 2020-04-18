from django.db import models
from Account.models import Member

ROLE_CHOICE=[
    ('BOARD', 'Board'),
    ('REGULAR', 'Regular')
]
class Attendance(models.Model): 
  type=models.CharField( max_length=50, choices=ROLE_CHOICE, null=True)
  board=models.ForeignKey(Member, on_delete=models.CASCADE)
 
  
  