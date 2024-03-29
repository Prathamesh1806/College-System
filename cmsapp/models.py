from django.db import models

class DeptModel(models.Model):
	did=models.IntegerField(primary_key=True)
	dname=models.CharField(max_length=30)

	def __str__(self):
		return str(self.dname)

class StuModel(models.Model):
	rno=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=30)
	dept=models.ForeignKey(DeptModel,on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.name)