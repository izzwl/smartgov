from django.db import models

# Create your models here.
class Input(models.Model):
    kode = models.CharField(max_length=50,unique=True)
    parameter = models.CharField(max_length=100)
    def __str__(self):
        return self.kode + "-" + self.parameter
    class Meta:
        verbose_name = 'Input'
        verbose_name_plural = 'Input'
        ordering = ['kode']
class Output(models.Model):
    kode = models.CharField(max_length=50,unique=True)
    parameter = models.CharField(max_length=100)
    def __str__(self):
        return self.kode + "-" + self.parameter
    class Meta:
        verbose_name = 'Output'
        verbose_name_plural = 'Output'
        ordering = ['kode']
class Outcome(models.Model):
    kode = models.CharField(max_length=50,unique=True)
    parameter = models.CharField(max_length=100)
    def __str__(self):
        return self.kode + "-" + self.parameter
    class Meta:
        verbose_name = 'Outcome'
        verbose_name_plural = 'Outcome'
        ordering = ['kode']
class Metode(models.Model):
    kode = models.CharField(max_length=50,unique=True)
    nama = models.CharField(max_length=100)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name = 'Metode'
        verbose_name_plural = 'Metode'
        ordering = ['kode']

class EntryDataset(models.Model):
    metode = models.ForeignKey(Metode,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'

class InputData(models.Model):
    entry = models.ForeignKey(EntryDataset,on_delete=models.CASCADE,default=None,null=True)
    parameter = models.ForeignKey(Input,on_delete=models.CASCADE)
    value = models.DecimalField('Value (%)',default=0,max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = 'Input Data'
        verbose_name_plural = 'Input Data'
class OutputData(models.Model):
    entry = models.ForeignKey(EntryDataset,on_delete=models.CASCADE,default=None,null=True)
    parameter = models.ForeignKey(Output,on_delete=models.CASCADE)
    value = models.DecimalField('Value (%)',default=0,max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = 'Output Data'
        verbose_name_plural = 'Output Data'
class OutcomeData(models.Model):
    entry = models.ForeignKey(EntryDataset,on_delete=models.CASCADE,default=None,null=True)
    parameter = models.ForeignKey(Outcome,on_delete=models.CASCADE)
    value = models.DecimalField('Value (%)',default=0,max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = 'Outcome Data'
        verbose_name_plural = 'Outcome Data'


class Dataset(models.Model):
    metode = models.ForeignKey(Metode,on_delete=models.CASCADE,null=True,default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    input_ref = models.ForeignKey(Input,on_delete=models.CASCADE,null=True,default=None)
    input_data = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    output_ref = models.ForeignKey(Output,on_delete=models.CASCADE,null=True,default=None)
    output_data = models.DecimalField(default=0,max_digits=5, decimal_places=2)    
    outcome_ref = models.ForeignKey(Outcome,on_delete=models.CASCADE,null=True,default=None)
    outcome_data = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    def __str__(self):
        return self.pk
    


    