from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=30)
    Number = models.IntegerField()
    About_me = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="media/") # boyutu büyük olduğuiçin sadece adres olarak dbde tutuluyor. Dosyayı belirtilen klasöre yüklüyor
    register_date = models.DateTimeField(auto_now_add=True) # ilk oluşturulduğu zamanı alır
    last_update_date = models.DateTimeField(auto_now=True) # her update olduğunda tarihsaat alır
    
    def __str__(self) -> str:
        return (f"{self.Number}-{self.FirstName}")
    class Meta:
        ordering = ["Number"]
        verbose_name_plural = "Student_List"  # Admin paneldeki görünen ismi değiştiriyor
        db_table = "Student_Table"  # db de tablonun ismini değiştiriyor tekrar migrate etmek gerekiyor
        