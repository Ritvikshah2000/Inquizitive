from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Quiz_Genre)
admin.site.register(Quiz_Question)
admin.site.register(Quiz_Question_Option)
admin.site.register(Quiz_User_Attempt)
admin.site.register(Quiz_Question_User_Answer)
