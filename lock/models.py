from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class KeyInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.TextField()
    Status = models.ForeignKey('Access', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.user.username

class Access(models.Model):
    Name = models.CharField(max_length=50, help_text="Наименование доступа")
    
    def __str__(self):
        return self.Name
        
class State(models.Model):
    Name = models.CharField(max_length=50, help_text="Наименование состояния")
    
    def __str__(self):
        return self.Name
        
class Equipment(models.Model):
    Name = models.CharField(max_length=150, help_text="Оборудование")
    
    def __str__(self):
        return self.Name

class Event(models.Model):
    user = models.ForeignKey(KeyInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    equip = models.ManyToManyField(Equipment, help_text='Оборудование')
    
    def display_time(self):
        return '%s - %s' % (self.start_time.strftime("%H:%M:%S"), self.end_time.strftime("%H:%M:%S"))
        
    def display_day(self):
        return '%s.%s.%s' % (self.day.day, self.day.month, self.day.year)
        
    def __str__(self):
        return '%s.%s.%s %s:%s:%s - %s:%s:%s' % (self.day.day, self.day.month, self.day.year, self.start_time.hour, self.start_time.minute, self.start_time.second, self.end_time.hour, self.end_time.minute, self.end_time.second)
    
class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)
        
class HistoryEntered(models.Model):
    person = models.ForeignKey(KeyInfo, on_delete=models.CASCADE)
    curDateTime = models.DateTimeField()
    State = models.ForeignKey(State, on_delete=models.CASCADE)