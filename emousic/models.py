import os

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.dispatch import receiver


class Track(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=30)
    tot_measure = models.IntegerField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Measure(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    number = models.IntegerField()
    pleasantness = models.FloatField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
    attention = models.FloatField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
    sensitivity = models.FloatField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
    aptitude = models.FloatField(validators=[MinValueValidator(-1), MaxValueValidator(1)])
    moodtag_1 = models.CharField(max_length=20)
    moodtag_2 = models.CharField(max_length=20)
    polarity = models.IntegerField(
        choices=[
            (-1, 'Negative'),
            (0, 'Neutral'),
            (1, 'Positive'),
        ],
        default=0,
    )
    polarity_value = models.FloatField(validators=[MinValueValidator(-1), MaxValueValidator(1)])

    def save(self, *args, **kwargs):
        self.pleasantness = round(self.pleasantness, 3)
        self.attention = round(self.attention, 3)
        self.sensitivity = round(self.sensitivity, 3)
        self.aptitude = round(self.aptitude, 3)
        self.polarity_value = round(self.polarity_value, 3)
        super(Measure, self).save(*args, **kwargs)

    def __str__(self):
        return self.track.name + str(self.number)


@receiver(models.signals.post_delete, sender=Track)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
