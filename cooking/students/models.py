from django.db import models


class Student(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)

    def __str__(self) -> str:
        return f'{self.name} {self.phone}'


class Student_Detail(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, primary_key=True)
    weekly_pay = models.DecimalField(max_digits = 10,decimal_places=2, null=True, blank=True)
    last_paid_date = models.DateField(null = True, blank= True)
    last_paid_amount = models.DecimalField(max_digits = 10,decimal_places=2, null=True, blank=True)
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_date = models.DateField(null = True, blank= True)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transaction_history = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.student.name} Details'
    
    def record_transaction(self, date, amount, description=""):
        # Record a transaction and update total paid amount and remaining balance
        self.last_paid_date = date
        self.last_paid_amount = amount
        self.total_paid_amount += amount
        self.remaining_balance -= amount
        transaction_info = f"{date}: Paid {amount} - {description}\n"
        self.transaction_history += transaction_info
        return f'{self.last_paid_amount} {self.last_paid_date}'