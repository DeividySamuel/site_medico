from medico.models import *

class Agenda(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(null=True, blank=True, max_length=50)
    msg = models.TextField(null=True, blank=True)
    email = models.EmailField()
    agenda = models.DateTimeField(default=True)

    def __str__(self):
        return '{}'.format(self.nome)