from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    discovered = models.CharField(max_length=100)
    electron_shell = models.CharField(max_length=50)
    electrons = models.CharField(max_length=100)
    protons = models.CharField(max_length=100)
    neutrons = models.CharField(max_length=100)
    description = models.TextField()
    atomic_number = models.CharField(max_length=100)
    atomic_weight = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    melting = models.CharField(max_length=100)
    boiling = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    valence_electron = models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    electronic_config = models.CharField(max_length=100)
    oxidation_state = models.CharField(max_length=100)
    atomic_radius = models.CharField(max_length=100)
    covalent_radius = models.CharField(max_length=100)
    vander_radius = models.CharField(max_length=100)
    electronegativity = models.CharField(max_length=100)
    electronaffinity = models.CharField(max_length=100)
    magnetic_type = models.CharField(max_length=100)
    crystal_str = models.CharField(max_length=100)
    resistivity = models.CharField(max_length=100)
    superconducting_point = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
