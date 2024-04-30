from django.db import models
from django.utils.timezone import localtime
import datetime

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


    def get_duration(self):
        current_time = localtime()
        visit_time = self.entered_at
        delta = current_time - visit_time
        seconds = delta.total_seconds()
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        duration = f'{hours}:{minutes}'
        return duration

    def is_visit_long(self, minutes=60):
        long_time = datetime.timedelta(seconds=minutes*60)
        if self.leaved_at:
            delta = self.leaved_at - self.entered_at
        else:
            delta = localtime() - self.entered_at
        return delta > long_time

