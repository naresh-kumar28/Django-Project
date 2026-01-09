from django.db import models

# Create your models here.


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=50)

    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

    id_verified = models.CharField(max_length=100)
    uhid = models.CharField(max_length=100)
    reference_id = models.CharField(max_length=50)

    vaccination_status = models.CharField(max_length=150)

    vaccinated_by = models.CharField(max_length=150)
    vaccinated_at = models.CharField(max_length=200)

    # dose 1 (mandatory)
    dose_number1 = models.CharField(max_length=30)
    dose_date1 = models.DateField()
    manufacturer1 = models.CharField(max_length=200)
    vaccine_name1 = models.CharField(max_length=50)
    batch_number1 = models.CharField(max_length=50)
    vaccine_type1 = models.CharField(max_length=200)

    # dose 2 (optional)
    dose_number2 = models.CharField(max_length=30, null=True, blank=True)
    dose_date2 = models.DateField(null=True, blank=True)
    manufacturer2 = models.CharField(max_length=200, null=True, blank=True)
    vaccine_name2 = models.CharField(max_length=50, null=True, blank=True)
    batch_number2 = models.CharField(max_length=50, null=True, blank=True)
    vaccine_type2 = models.CharField(max_length=200, null=True, blank=True)

    # dose 3 (optional)
    dose_number3 = models.CharField(max_length=30, null=True, blank=True)
    dose_date3 = models.DateField(null=True, blank=True)
    manufacturer3 = models.CharField(max_length=200, null=True, blank=True)
    vaccine_name3 = models.CharField(max_length=50, null=True, blank=True)
    batch_number3 = models.CharField(max_length=50, null=True, blank=True)
    vaccine_type3 = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
