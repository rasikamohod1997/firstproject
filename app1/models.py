from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ActiveP(models.Model):
    def get_query(self):
        return super().get_query().filter(is_delete=0)


class InActiveP(models.Model):     # Assignment point 
    def get_query(self):
        return super().get_query().filter(is_delete=1)


class CommonClass(models.Model):
    Name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.id}---{self.Name}"

class Employee(CommonClass):
    salary = models.IntegerField()

class Persons(CommonClass):
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Age = models.IntegerField()
    is_delete = models.SmallIntegerField(default=0)
    get_active_persons = ActiveP()
    get_inactive_persons = InActiveP()
    objects = models.Manager()

    class Meta:
        db_table = "persons"

    def get_person_details(self):
        print(f"""----------- Persons id : {self.id} ----------
Name : {self.Name}
Age : {self.Age}
Address : {self.Address}
City : {self.City}
""")

    @classmethod
    def get_active_persons(cls):
        return cls.objects.filter(is_delete=0)

    @classmethod
    def get_inactive_persons(cls):
        return cls.objects.filter(is_delete=1)

    @classmethod
    def get_avg_age(cls):
        all = Persons.objects.filter(is_delete=0).values_list("Age")
        lst = list(map(lambda x :x[0], all))
        avg = sum(lst)/len(lst)
        return avg


# ##################################################################################################################################    

class City1(models.Model):
    Name = models.CharField(max_length=255)
    CountryCode = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Population = models.IntegerField()

    class Meta:
        db_table = "city1"
        

#####################################################################################################################################
# Database ---> college

class College1(CommonClass):
    address = models.CharField(max_length=100)
    est_date = models.DateField()

    class Meta:
        db_table = "college"


class Princi1(CommonClass):
    exp = models.FloatField()
    salary = models.IntegerField()
    college = models.OneToOneField(College1, on_delete = models.SET_NULL, null=True)  # college_id (1 clg ---- 1 princi)

    class Meta:
        db_table = "princi"

class Department1(CommonClass):
    staff_num = models.IntegerField()
    college = models.ForeignKey(College1, on_delete = models.SET_NULL, null=True, related_name = "depts")  # college_id  (1 clg ---- M dept)


    class Meta:
        db_table = "dept"

class Students1(CommonClass):
    age = models.IntegerField()
    marks = models.IntegerField()    
    department = models.ForeignKey(Department1, on_delete = models.SET_NULL, null=True, related_name = "studs")  # dept_id  (M stud ---- 1 clg)

    class Meta:
        db_table = "student"


class Subjects1(CommonClass):
    is_practical = models.BooleanField(default = False)
    student = models.ManyToManyField(Students1)
    department = models.ForeignKey(Department1, on_delete = models.SET_NULL, null=True, related_name = "subjs")  # dept_id  (M subj ---- 1 dept)

    class Meta:
        db_table = "subject"



# ###################################################################################################################################

# import uuid


# class ProdModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)
#     category = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#     price = models.IntegerField()

#     class Meta:
#         db_table = "prod"

#     def __str__(self):
#         return f"\n{self.__dict__}"


# #######################################################################################################################################

# --------------------------- CAR MODEL -------------------------

class Car(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "car"
    
    def __str__(self):
        return self.name

class Ceo(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "ceo"

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = "fueltype"

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    fueltype = models.ManyToManyField(FuelType)

    class Meta:
        db_table = "carmodel"

    def __str__(self):
        return self.name

    
#######################################################################################################################################


class AvailProd(models.Model):
    def get_query(self):
        return super().get_query().filter(is_available=1)


class UnAvailProd(models.Model):     
    def get_query(self):
        return super().get_query().filter(is_available=0)

class Prod(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    is_available = models.SmallIntegerField(default=0)
    get_available_products = AvailProd()
    get_unavailable_products = UnAvailProd()
    objects = models.Manager()

    class Meta:
        db_table = "prod1"

    def __str__(self):
        # return f"\n{self.__dict__}"
        return f"{self.name} ----{self.category}"

    def get_product_details(self):
        print(f"""----------- Product id : {self.id} ----------
Name : {self.name}
Category : {self.category}
Quantity : {self.quantity}
Price : {self.price}
Is_Avail : {self.is_available}
""")

    @classmethod
    def get_available_products(cls):
        return cls.objects.filter(is_available=1)

    @classmethod
    def get_unavailable_products(cls):
        return cls.objects.filter(is_available=0)

    @classmethod
    def get_name_of_prods(cls):
        all = Prod.objects.filter.values_list("name")
        lst = list(filter(lambda x :x[0], all))
        return lst

    @classmethod
    def get_avg_all_prod(cls):
        all = Prod.objects.filter(is_available=1).values_list("price")
        lst = list(map(lambda x :x[0], all))
        avg = sum(lst)/len(lst)
        return avg

    @classmethod
    def get_prod_by_catgory(cls):
        return cls.objects.filter(category = "Furniture")

    @classmethod
    def update_products_availablity(cls):
        data = Prod.objects.filter(is_available__in=[0])
        data.update(is_available = 1)
        return data

    @classmethod 
    def filtered_prod(cls):
        data = Prod.objects.filter(name__startswith='S')
        return data

    @classmethod
    def prod_with_name_only(cls):
        data = Prod.objects.all().only("name")
        for i in data:
            print(i.__dict__) 

    @classmethod
    def delete_prod_by_category(cls):
        Prod.objects.filter(category = "Furniture").delete()
        return Prod.objects.all()



###############################################################################################################################

class Author(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length = 50)
    # publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name