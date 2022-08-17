
# exec(open(r'D:\Programs\B7_Django\firstproject\db_shell.py').read())


from app1.models import *

# all_data = Persons.objects.all()

# if all_data.exists():
#     print("data exist")

# to fetch all data
# print(all_data)  # <QuerySet [<Persons: Persons object (1)>, <Persons: Persons object (2)>, <Persons: Persons object (3)>]>

# for i in all_data:
    # print(i)

# Persons object (1)
# Persons object (2)
# Persons object (3)

# for i in all_data:
#     print(i.__dict__)

# {'_state': <django.db.models.base.ModelState object at 0x000002021F4BBDF0>, 'id': 1, 'Name': 'abc', 'Address': 'Wakad', 'City': 'Pune', 'Age': 25}
# {'_state': <django.db.models.base.ModelState object at 0x000002021F4BBD30>, 'id': 2, 'Name': 'xyz', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 22}
# {'_state': <django.db.models.base.ModelState object at 0x000002021F4B8760>, 'id': 3, 'Name': 'pqr', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 21}

# to change
# p_obj = Persons.objects.get(id=2)
# p_obj.Name = "Aditi"
# p_obj.save()


# p_obj = Persons.objects.get(City = "Pune", Address = "Akurdi") # and query
# print(p_obj.__dict__)

# queryset = Persons.objects.filter(Name__startswith='a') | Persons.objects.filter(Name__endswith='r')
# print(queryset)   # <QuerySet [<Persons: Persons object (1)>, <Persons: Persons object (2)>, <Persons: Persons object (3)>]>

# queryset = Persons.objects.filter(Name__contains='i')
# print(queryset)  # <QuerySet [<Persons: Persons object (2)>]>

# queryset = Persons.objects.filter(Name__startswith='A') & Persons.objects.filter(Name__contains='i')
# print(queryset)  # <QuerySet [<Persons: Persons object (2)>]>


# To Perform AND Query 

# Case 1 --- using &
# queryset1 = Persons.objects.filter(Name__startswith='A') & Persons.objects.filter(Age__gt=21)
# print(str(queryset1.query))
# SELECT "persons"."id", "persons"."Name", "persons"."Address", "persons"."City", "persons"."Age" FROM "persons" WHERE ("persons"."Name" LIKE A% ESCAPE '\' AND "persons"."Age" > 21)
# print(queryset)  # <QuerySet [<Persons: Persons object (1)>, <Persons: Persons object (2)>]>

# Case 2 --- using comma
# queryset2 = Persons.objects.filter(Name__startswith='A', Age__gt=21)
# print(queryset)  # <QuerySet [<Persons: Persons object (1)>, <Persons: Persons object (2)>]>
# print(str(queryset2.query))

# Case 3 --- using Q
# from django.db.models import Q

# queryset3 = Persons.objects.filter(Q(Name__startswith = 'A') & Q(Age__gt = 21))
# print(qs) #  <QuerySet [<Persons: Persons object (1)>, <Persons: Persons object (2)>]>
# print(str(queryset3.query))

# NOT Query

# case 1 : using exclude
# qs = Persons.objects.all().exclude(Name = "abc")
# print(qs)   # <QuerySet [<Persons: Persons object (2)>, <Persons: Persons object (3)>]>
# print(str(qs.query))
# SELECT "persons"."id", "persons"."Name", "persons"."Address", "persons"."City", "persons"."Age" FROM "persons" WHERE NOT ("persons"."Name" = abc)

# case 2 :using Q() method
# from django.db.models import Q

# queryset = Persons.objects.filter(~Q(id__lt=1))
# print(queryset)  # <QuerySet [<Persons: Persons object (1)>]>

# -------------------------- 24 june 2022 (Models) ----------------------------------

# data = Persons.objects.all().values("Name", "Age")
# print(data)  # <QuerySet [{'Name': 'abc', 'Age': 25}, {'Name': 'Aditi', 'Age': 22}, {'Name': 'pqr', 'Age': 21}]>

# data = Persons.objects.all().values_list("Name", "Age")
# print(data)   # <QuerySet [('abc', 25), ('Aditi', 22), ('pqr', 21)]>

# diff bet values and values list ?
        #  values --- Dict
        #  values_list --- list of tuple


# data = Persons.objects.all().only("Name")
# for i in data:
#     print(i.__dict__) 

# {'_state': <django.db.models.base.ModelState object at 0x000001B0CE138910>, 'id': 1, 'Name': 'abc'}
# {'_state': <django.db.models.base.ModelState object at 0x000001B0CE138850>, 'id': 2, 'Name': 'Aditi'}
# {'_state': <django.db.models.base.ModelState object at 0x000001B0CE138790>, 'id': 3, 'Name': 'pqr'}

# single_data = Persons.objects.get(id=1)
# print(single_data)  

# {'_state': <django.db.models.base.ModelState object at 0x000002659AD840A0>, 'id': 1, 'Name': 'abc', 'Address': 'Wakad', 'City': 'Pune', 'Age': 25}

#---------------------CRUD------------------------------

# --------- Create ---------
# Case 1

# p_obj = Persons(Name="Raj", Address="Akurdi", City="Pune", Age=25) # return None
# p_obj.save()

# p_obj = Persons.objects.create(Name="Rahul", Address="Thergaon", City="Pune", Age=20)  # return Created object
# print(p_obj)

# ----- Read -----
# .all , .get, .filter

# data = Persons.objects.filter(City="Pune")
# print(data)

# <QuerySet [<Persons: 
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD846A0>, 'id': 1, 'Name': 'abc', 'Address': 'Wakad', 'City': 'Pune', 'Age': 25}>, <Persons:       
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD84AC0>, 'id': 2, 'Name': 'Aditi', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 22}>, <Persons:    
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD84700>, 'id': 3, 'Name': 'pqr', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 21}>, <Persons:       
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD84760>, 'id': 4, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25}>, <Persons:      
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD84070>, 'id': 5, 'Name': 'Rahul', 'Address': 'Thergaon', 'City': 'Pune', 'Age': 20}>]>
# >>>


# data = Persons.objects.filter(City="Pune")[0]
# print(data)  # {'_state': <django.db.models.base.ModelState object at 0x000002659AD849D0>, 'id': 1, 'Name': 'abc', 'Address': 'Wakad', 'City': 'Pune', 'Age': 25}


# data = Persons.objects.filter(City="Pune")[0:2]
# print(data)

# <QuerySet [<Persons: 
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD84AC0>, 'id': 1, 'Name': 'abc', 'Address': 'Wakad', 'City': 'Pune', 'Age': 25}>, <Persons:       
# {'_state': <django.db.models.base.ModelState object at 0x000002659AD84790>, 'id': 2, 'Name': 'Aditi', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 22}>]>


# ------ Update ------

# Updated Single Data
# data = Persons.objects.get(id=3)
# print(data.Age)
# data.Name = "Mayu"
# data.save()

# print(data)

# Bulk Updated

# data = Persons.objects.filter(Age__in=[21,24,25])
# data.update(Age=22)
# print(data)
# 

# Bulk Create (for sqlite database)

# Persons.objects.bulk_create([
#     Persons(Name="Ashwini", Address="GadgeNagar", City="Amravati", Age=30),
#     Persons(Name="Anuj", Address="ShahuNagar", City="AhmedNagar", Age=25),
# ])

# print(Persons.objects.bulk_create)


# all_data = Persons.objects.all()
# print(all_data)

# <QuerySet [<Persons:
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6204BE0>, 'id': 1, 'Name': 'abc', 'Address': 'Wakad', 'City': 'Pune', 'Age': 25}>, <Persons:       
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6204A00>, 'id': 2, 'Name': 'Aditi', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 22}>, <Persons:    
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6204F70>, 'id': 3, 'Name': 'Mayu', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 21}>, <Persons:      
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6206050>, 'id': 4, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 24}>, <Persons:      
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6205FC0>, 'id': 5, 'Name': 'Rahul', 'Address': 'Thergaon', 'City': 'Pune', 'Age': 20}>, <Persons:  
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6205EA0>, 'id': 6, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x000001E0A6205F30>, 'id': 7, 'Name': 'Anuj', 'Address': 'ShahuNagar', 'City': 'AhmedNagar', 'Age': 25}>]>  


#--------- Delete ----------

# p = Persons.objects.get(id=7).delete()
# print(p)

# p = Persons.objects.all().delete()
# print(p)



#########################################################################################################################################

# -------------------------- 25 june 2022  ----------------------------------

# createsuperuser

# D:\Programs\B7_Django\firstproject>py manage.py createsuperuser
# Username (leave blank to use 'shree'): shree
# Email address: shree@gmail.com
# Password: 
# Password (again):
# Superuser created successfully.

# changepassword   (Python@123 ----> Django@123)
# (proj_env) D:\Programs\B7_Django\firstproject>python manage.py changepassword Raj
# Changing password for user 'Raj'
# Password:             
# Password (again):
# Password changed successfully for user 'Raj'

# ------------- after is_delete ---------------------

# all_data = Persons.objects.all()
# print(all_data)

# <QuerySet [<Persons: 
# {'_state': <django.db.models.base.ModelState object at 0x000001E42560BA90>, 'id': 1, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30, 'is_delete': 0}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x000001E42560BC10>, 'id': 2, 'Name': 'Anuj', 'Address': 'ShahuNagar', 'City': 'AhmedNagar', 'Age': 25, 'is_delete': 0}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x000001E42560BCA0>, 'id': 3, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25, 'is_delete': 0}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x000001E42560BD30>, 'id': 4, 'Name': 'Aditi', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 25, 'is_delete': 1}>]>

# all_data = Persons.objects.filter(is_delete = 0)   
# print(all_data)

# <QuerySet 
# [<Persons: {'_state': <django.db.models.base.ModelState object at 0x000001E42560BCA0>, 'id': 1, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30, 'is_delete': 0}>, 
# <Persons:{'_state': <django.db.models.base.ModelState object at 0x000001E425608C70>, 'id': 2, 'Name': 'Anuj', 'Address': 'ShahuNagar', 'City': 'AhmedNagar', 'Age': 25, 'is_delete': 0}>, 
# <Persons:{'_state': <django.db.models.base.ModelState object at 0x000001E42560BB50>, 'id': 3, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25, 'is_delete': 0}>]>

# all_data = Persons.objects.filter(is_delete = 1)   
# print(all_data)

# <QuerySet 
# [<Persons: {'_state': <django.db.models.base.ModelState object at 0x000001E425608790>, 'id': 4, 'Name': 'Aditi', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 25, 'is_delete': 1}>]>

# data1 = Persons.get_active_persons()
# print(data1)

# <QuerySet 
# [<Persons: {'_state': <django.db.models.base.ModelState object at 0x0000017C6A2FBCD0>, 'id': 1, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30, 'is_delete': 0}>,
#  <Persons:{'_state': <django.db.models.base.ModelState object at 0x0000017C6A2FBD90>, 'id': 2, 'Name': 'Anuj', 'Address': 'ShahuNagar', 'City': 'AhmedNagar', 'Age': 25, 'is_delete': 0}>, 
# <Persons: {'_state': <django.db.models.base.ModelState object at 0x0000017C6A2FBE20>, 'id': 3, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25, 'is_delete': 0}>]>


# data1 = Persons.get_inactive_persons()
# print(data1)

# <QuerySet [<Persons: 
# {'_state': <django.db.models.base.ModelState object at 0x00000200A8DFBD00>, 'id': 4, 'Name': 'Aditi', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 25, 'is_delete': 1}>]>


# print(Persons.get_avg_age())  # 26.666666666666668

# p1 = Persons.objects.get(id=3)
# print(p1)

# {'_state': <django.db.models.base.ModelState object at 0x0000020DC8BFBF10>, 'id': 3, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25, 'is_delete': 0} 


# data = Persons.objects.all()
# print(data)

# <QuerySet [<Persons: 
# {'_state': <django.db.models.base.ModelState object at 0x00000237E2DDBCA0>, 'id': 1, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30, 'is_delete': 0}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x00000237E2DDBE20>, 'id': 2, 'Name': 'Anuj', 'Address': 'ShahuNagar', 'City': 'AhmedNagar', 'Age': 25, 'is_delete': 0}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x00000237E2DDBEB0>, 'id': 3, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25, 'is_delete': 0}>, <Persons:
# {'_state': <django.db.models.base.ModelState object at 0x00000237E2DDBF40>, 'id': 4, 'Name': 'Aditi', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 25, 'is_delete': 1}>]>


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# print(dir(Persons.objects))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_constructor_args', 
# '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter', 
# '_update', 'aggregate', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 
# 'complex_filter', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 
# 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 
# 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk',
#  'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related',
#  'raw', 'reverse', 'select_for_update', 'select_related', 'union',  'update', 'update_or_create', 'use_in_migrations',
#  'using', 'values', 'values_list']   

# c = Persons.objects.count()
# print(c)   # 4

# first_data = Persons.objects.first()
# print(first_data)
# 
# {'_state': <django.db.models.base.ModelState object at 0x0000020A5E96B850>, 'id': 1, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30, 'is_delete': 0}

#-----------------------------------------------------------------------------------------------------------------------------------

# print(Persons.get_active_persons())

# <QuerySet [<Persons: {'_state': <django.db.models.base.ModelState object at 0x0000029D066A0190>, 'id': 1, 'Name': 'Ashwini', 'Address': 'GadgeNagar', 'City': 'Amravati', 'Age': 30, 'is_delete': 0}>,
# <Persons: {'_state': <django.db.models.base.ModelState object at 0x0000029D066A0220>, 'id': 2, 'Name': 'Anuj', 'Address': 'ShahuNagar', 'City': 'AhmedNagar', 'Age': 25, 'is_delete': 0}>, 
# <Persons: {'_state': <django.db.models.base.ModelState object at 0x0000029D066A02B0>, 'id': 3, 'Name': 'Raj', 'Address': 'Akurdi', 'City': 'Pune', 'Age': 25, 'is_delete': 0}>]>

print(Persons.objects.all())

# print(Persons.get_inactive_persons())

# <QuerySet [<Persons: {'_state': <django.db.models.base.ModelState object at 0x000001A725728490>, 'id': 4, 'Name': 'Aditi', 'Address': 'Nigdi', 'City': 'Pune', 'Age': 25, 'is_delete': 1}>]>


##################################################################################################################################

# exec(open(r'D:\Programs\B7_Django\firstproject\db_shell.py').read())

# ----------------------- College Model ---------------------

# Extract Data 

# clg1 = College1.objects.get(id =1)
# print(clg1)                          # 1---D Y Patil

# clg1 = College1.objects.get(id=1) # fetch princi from college         
# print(clg1.princi1)                   # 1---Mr. Patil

# p1 = Princi1.objects.get(id = 2)
# print(p1.college)                       # 2---ICCS


# user_inp = int(input("Enter ID : "))
# try:
#     p1 = Princi1.objects.get(id = user_inp)
#     print(p1)
# except Princi1.DoesNotExist:
#     print(f"Princi does not exist for id {user_inp}")

# >>> exec(open(r'D:\Programs\B7_Django\firstproject\db_shell.py').read())
# Enter ID : 2
# 2---Mrs.Pathare
# >>> exec(open(r'D:\Programs\B7_Django\firstproject\db_shell.py').read())
# Enter ID : 3
# Princi does not exist for id 3


# fetch departments from college

# c1 = College1.objects.get(id=1)
# print(dir(c1))       # department1_set
"""
['DoesNotExist', 'Meta', 'MultipleObjectsReturned', 'Name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', 
'_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', 
'_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', 
'_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', 
'_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', 
'_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', 
'_state', 'address', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'department1_set', 'est_date', 'from_db', 
'full_clean', 'get_deferred_fields', 'get_next_by_est_date', 'get_previous_by_est_date', 'id', 'objects', 'pk', 'prepare_database_save', 
'princi1', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']
"""
# c1 = College1.objects.get(id=1)
# all_dept = c1.department1_set.all()
# print(all_dept)

# <QuerySet [<Department1: 1---Civil>, <Department1: 2---Mechanical>]>

#---------------------------------------------------------------------------------------------------------------

# ----------- fetch college from department ------------

# d1 = Department1.objects.get(id = 2)
# print(d1.college)           # 1---D Y Patil

# using related_name

# c1 = College1.objects.get(id=1)
# print(dir(c1))     # depts
"""
['DoesNotExist', 'Meta', 'MultipleObjectsReturned', 'Name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', 
'_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', 
'_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', 
'_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', 
'_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', 
'_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', 
'_state', 'address', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'depts', 'est_date', 'from_db', 'full_clean', 
'get_deferred_fields', 'get_next_by_est_date', 'get_previous_by_est_date', 'id', 'objects', 'pk', 'prepare_database_save', 'princi1',
 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']
 """



# all_dept =c1.depts.all()
# print(all_dept)     # <QuerySet [<Department1: 1---Civil>, <Department1: 2---Mechanical>]>


# c1 = College1.objects.get(id=1)
# print(c1.est_date)              # 2022-06-26


# -------------- fetch Students from Department------------

# d1 = Department1.objects.get(id=4)
# print(d1.studs.all())           # <QuerySet [<Students1: 2---Stud2>]>


# -------------- fetch students from College -------------

# c1 = College1.objects.get(id=1)
# depts = c1.depts.all()
# for i in depts:
#     print(i.studs.all())

# <QuerySet [<Students1: 3---Stud3>]>
# <QuerySet [<Students1: 4---Stud4>, <Students1: 5---Stud5>]>

# c1 = College1.objects.get(id=1)
# depts = c1.depts.all()
# studs_list = []
# for i in depts:
#     studs_list.extend(list(i.studs.all()))
# print(studs_list)

# [<Students1: 3---Stud3>, <Students1: 4---Stud4>, <Students1: 5---Stud5>]

# s1 = Students1.objects.get(id=2)
# print(dir(s1))
"""
['DoesNotExist', 'Meta', 'MultipleObjectsReturned', 'Name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', 
'_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', 
'_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', 
'_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', 
'_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', 
'_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks',
'_save_parents', '_save_table', '_set_pk_val', '_state', 'age', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 
'department', 'department_id', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'marks', 'objects', 'pk', 'prepare_database_save', 
'refresh_from_db', 'save', 'save_base', 'serializable_value', 'subjects1_set', 'unique_error_message', 'validate_unique']
"""

# fetch college and address for particular student

# s1 = Students1.objects.get(id=1)
# print(s1.department.college)        #  2---ICCS
# print(s1.department.college.address)   # Tathawade

# --------- fetch subject from student ------------ 

# s1 = Students1.objects.get(id=1)

# print(s1.subjects1_set.all())

# <QuerySet [<Subjects1: 1---Mechanics>, <Subjects1: 2---Python>]>

# fetch student from subject

# subj = Subjects1.objects.get(id=1)
# print(dir(subj))

# print(subj.student.all())

# <QuerySet [<Students1: 1---Stud1>, <Students1: 2---Stud2>]>

# -------------- fetch department from subject -----------------

# subj = Subjects1.objects.get(id=1)
# data = subj.department

# print(data)   # 4---Electrical


# delete department

# d1 = Department1.objects.get(id=4).delete()

#--------------------------- Create ---------------------------

# ---- create college ----
# from django.utils import timezone

# c1 = College1.objects.create(Name="Ram Meghe", address="Amravati", est_date=timezone.now())

# print(c1)


# ---- create princi ----
# clg = College1.objects.get(id=3)  # Meghe Clg
# Princi1.objects.create(Name="Mr.Shedage", exp=8, salary=56000, college=clg)


# ---- create department ----
# clg = College1.objects.get(id=3)  # Meghe Clg

# Department1.objects.create(Name="Chemistry", staff_num=6, college_id =3)
# Department1.objects.create(Name="Computers", staff_num=9, college_id =3)


# ---- create student ----
# s1 = Students1.objects.create(Name="Stud5", marks=45, age=18, department_id=6)

# ---- adding students in specific dept ------

# d1 = Department1.objects.get(id=6)
# # print(dir(d1))
# studs = Students1.objects.all()

# d1.studs.add(studs[0])
# d1.studs.add(studs[1])

# --------- allocate dept to specific student ------

# s1 = Students1.objects.first()

# d1 = Department1.objects.get(id=1)

# s1.department = d1
# s1.save()

# ------------ fetch dept from college ------

# d1 = Department1.objects.filter(college__Name="ICCS")
# print(d1)

# <QuerySet [<Department1: 3---IT>, <Department1: 4---Electrical>]>

# ---------- fetch stud from dept -----------

# print(Students1.objects.filter(department__Name ="Computers"))

# <QuerySet [<Students1: 2---Stud2>, <Students1: 6---Stud6>]>

# ---------- fetch students from college -------

# print(Students1.objects.filter(department__college__Name = "Ram Meghe"))

# <QuerySet [<Students1: 2---Stud2>, <Students1: 6---Stud6>]>

# ---------- fetch subjects from college -------

# print(Subjects1.objects.filter(department__college__Name = "ICCS"))

# <QuerySet [<Subjects1: 1---Mechanics>, <Subjects1: 2---Python>, <Subjects1: 5---Ele1>, <Subjects1: 6---Ele2>]>

#  ------ add students for subjects ------ (Many to Many Relationship)  Assignment

# s1 = Subjects1.objects.get(id=5)
# print(dir(s1))
# studs = Students1.objects.all()
# s1.student.add(studs[0])
# s1.student.add(studs[1])
# s1.student.add(studs[2])

# ------- add Subjects for particular student ------

# stud = Students1.objects.get(id=6)
# print(dir(stud))
# subj = Subjects1.objects.all()

# stud.subjects1_set.add(subj[0])
# stud.subjects1_set.add(subj[1])
# stud.subjects1_set.add(subj[2])

#######################################################################################################################################

# ---------------------------- CAR & CEO -------------------- 


# c1 = Car.objects.get(id=1)
# ceo1 = Ceo.objects.create(name="CEO1", car = c1)
# c2 = Car.objects.get(id=2)
# ceo2 = Ceo.objects.create(name="CEO2", car=c2)
# c3 = Car.objects.get(id=3)
# ceo3 = Ceo.objects.create(name="CEO3", car=c3)
# c4 = Car.objects.get(id=4)
# ceo4 = Ceo.objects.create(name="CEO4", car=c4)
# c5 = Car.objects.get(id=5)
# ceo5 = Ceo.objects.create(name="CEO5", car=c5)
# c6 = Car.objects.get(id=6)
# ceo6 = Ceo.objects.create(name="CEO6", car=c6)


# print(Ceo.objects.all())

# <QuerySet [<Ceo: CEO1>, <Ceo: CEO2>, <Ceo: CEO3>, <Ceo: CEO4>, <Ceo: CEO5>, <Ceo: CEO6>]>

# ------------ fetch ceo from car --------------

# c1 = Car.objects.get(id=1)
# print(dir(c1)) # ceo

# print(c1.ceo)   # CEO1

# ------------ fetch car from ceo ---------------

# ceo = Ceo.objects.get(id=3)

# print(dir(ceo))   # car

# print(ceo.car.name)   # Fortuner

# -------------- filter cars by ceo --------------

# c1 =Car.objects.filter(ceo__name__endswith="3")

# print(c1)   # <QuerySet [<Car: Fortuner>]>

# ------------- filter ceo by cars ---------------

# ceo1 = Ceo.objects.get(car__name="Ertiga")

# print(ceo1)   # CEO6

#--------------- Delete ---------------

# create new for delete 

# bmw = Car.objects.create(name="BMW")
# bmw_ceo = Ceo.objects.create(name="Jack Ryan", car=bmw)

# bmw = Car.objects.get(name = "BMW")
# # print(dir(bmw))
# print(bmw)
# print(bmw.ceo)
# bmw.delete()

# print(bmw)
# print(bmw.ceo)


# print(Car.objects.all()) # <QuerySet [<Car: Bolero>, <Car: Creta>, <Car: Fortuner>, <Car: Nexon>, <Car: Range Rover>, <Car: Ertiga>]>
# print(Ceo.objects.all()) # <QuerySet [<Ceo: CEO1>, <Ceo: CEO2>, <Ceo: CEO3>, <Ceo: CEO4>, <Ceo: CEO5>, <Ceo: CEO6>]>

# when car is deleted the ceo record is also deleted


# ------------------------------ CAR & CAR MODEL  (1 - M) ----------------------------

# create

# c1 = Car.objects.create(name="Bolero")
# c2 = Car.objects.create(name="Creta")
# c3 = Car.objects.create(name="Fortuner")
# c4 = Car.objects.create(name="Nexon")
# c5 = Car.objects.create(name="Range Rover")

# print(Car.objects.all())

# <QuerySet [<Car: Bolero>, <Car: Creta>, <Car: Fortuner>, <Car: Nexon>, <Car: Range Rover>]>

# ------------ Creating new car model ------------------

# c1 = Car.objects.get(id=1)
# cm1 = CarModel.objects.create(name="Mahindra Bolero B6", car=c1)
# c2 = Car.objects.get(id=2)
# cm2 = CarModel.objects.create(name="Hyundai Creta SX O", car=c2)
# c3 = Car.objects.get(id=3)
# cm3 = CarModel.objects.create(name="Toyoto Fortuner 4X2", car=c3)
# c4 = Car.objects.get(id=4)
# cm4 = CarModel.objects.create(name="Tata Nexon XZ Plus", car=c4)
# c5 = Car.objects.get(id=5)
# cm5 = CarModel.objects.create(name="Land Rover Range Rover", car=c5)

# print(CarModel.objects.all())
# <QuerySet [<CarModel: Mahindra Bolero B6>, <CarModel: Hyundai Creta SX O>, <CarModel: Toyoto Fortuner 4X2>, <CarModel: Tata Nexon XZ Plus>, <CarModel: Land Rover Range Rover>]>


# c6 = Car.objects.create(name="Crysta")
# c6.save()
# print(c6)

# c6 = Car.objects.get(id=6)
# cm = CarModel.objects.create(name=""Ertiga",car=c6)
# cm.save()
# print(cm)

# ----------- add carmodel to car -------------

# cm1 = CarModel.objects.create(name="Maruti Ertiga ZXI")
# cm2 = CarModel.objects.create(name="Maruti Ertiga ZDI")

# c6 = Car.objects.get(id=6)
# # print(dir(c6))

# c6.carmodel_set.add(cm1,cm2)
# print(c6.carmodel_set.all())  
# <QuerySet [<CarModel: Toyoto Innovo Crysta>, <CarModel: Maruti Ertiga ZXI>, <CarModel: Maruti Ertiga ZDI>]>

# ---------- Retrive Records --------

# From car model to car 

# cm1 = CarModel.objects.get(id=7)
# print(dir(cm1))
# print(cm1.car.name)   # Ertiga

# From car to car model

# c6 = Car.objects.get(id=6)
# print(dir(c6))   # carmodel_set

# print(c6.carmodel_set.all())
# <QuerySet [<CarModel: Maruti Ertiga ZXI>, <CarModel: Maruti Ertiga ZDI>]>

# print(c6.carmodel_set.first())     # Maruti Ertiga ZXI


# -------------------- filter car models by car ----------------------

# print(CarModel.objects.filter(car__name="Ertiga"))
# <QuerySet [<CarModel: Maruti Ertiga ZXI>, <CarModel: Maruti Ertiga ZDI>]>

# ----------------- filter car by car models ------------------------

# print(Car.objects.filter(carmodel__name="Toyoto Fortuner 4X2"))     # <QuerySet [<Car: Fortuner>]>


# ---------------------------- CAR MODEL & FUEL TYPE (M-M) --------------------


# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")

# print(FuelType.objects.all())  # <QuerySet [<FuelType: Gas>, <FuelType: Diesel>, <FuelType: Hybrid>]>


#------ Add FuelType for CarModel ----

# gas = FuelType.objects.get(id=1)
# cm1 = CarModel.objects.get(id=7)
# cm1.fueltype.add(gas)
# print(cm1.fueltype.all())   # <QuerySet [<FuelType: Gas>]>

# diesel = FuelType.objects.get(id=2)
# cm1 = CarModel.objects.get(id=7)

# cm1.fueltype.add(diesel)
# print(cm1.fueltype.all())  # <QuerySet [<FuelType: Gas>, <FuelType: Diesel>]>


# ---------- Add multiple FuleType for 1 CarModel ---------

# cm1 = CarModel.objects.get(id=1)
# ft = FuelType.objects.all()
# cm1.fueltype.add(ft[0], ft[1], ft[2])


# --------------- fetch carmodel from fueltype ------------

# ft = FuelType.objects.get(id=1)
# print(ft.carmodel_set.all())

# <QuerySet [<CarModel: Maruti Ertiga ZDI>, <CarModel: Mahindra Bolero B6>, <CarModel: Hyundai Creta SX O>]>

# ----------------- Filtering Records ----------

# cm1 = CarModel.objects.filter(fueltype__name__endswith="s")
# print(cm1)

# <QuerySet [<CarModel: Maruti Ertiga ZDI>, <CarModel: Mahindra Bolero B6>, <CarModel: Hyundai Creta SX O>]>

# cm1 = CarModel.objects.filter(fueltype__name__startswith="H")
# print(cm1)

# <QuerySet [<CarModel: Mahindra Bolero B6>, <CarModel: Tata Nexon XZ Plus>, <CarModel: Land Rover Range Rover>, <CarModel: Maruti Ertiga ZXI>]>


# ft = FuelType.objects.filter(carmodel__name__startswith="M")

# print(ft)

# <QuerySet [<FuelType: Gas>, <FuelType: Diesel>, <FuelType: Hybrid>, <FuelType: Hybrid>, <FuelType: Gas>, <FuelType: Diesel>]>

# ft = FuelType.objects.filter(carmodel__name__startswith="M").distinct()

# print(ft)

# <QuerySet [<FuelType: Gas>, <FuelType: Diesel>, <FuelType: Hybrid>]>

# ------------------- Delete Records ---------------
# cm1 = CarModel.objects.get(id=1)

# ft = FuelType.objects.all()
# print(ft)                              # <QuerySet [<FuelType: Gas>, <FuelType: Diesel>, <FuelType: Hybrid>]>
# cm1.fueltype.remove(ft[0],ft[1],ft[2])


# print(cm1.fueltype.all())   # <QuerySet []>

# biogas = FuelType.objects.create(name="Biogas")

# cars = CarModel.objects.filter(fueltype__name__startswith="B")   
# print(cars) 
# <QuerySet [<CarModel: Hyundai Creta SX O>, <CarModel: Maruti Ertiga ZXI>]>

# cars.delete()    
  
# print(cars)  # <QuerySet []>


# ############################################################################################################################################

# ProdModel.objects.bulk_create([
#     ProdModel(name="Laptop", category="Electronics", quantity=12, price=40000),
#     ProdModel(name="Mobile", category="Electronics", quantity=23, price=78000),
#     ProdModel(name="Table", category="Furniture", quantity=34, price=4000),
#     ProdModel(name="Sofa", category="Furniture", quantity=56, price=22000),
#     ProdModel(name="Fridge", category="Electronics", quantity=45, price=56000),
# ])

# all_data = ProdModel.objects.all()

# for i in all_data:
#     print(i)

########################################################################################################################################

# -------------------------- Product ---------------------------------
# 
# Prod.objects.bulk_create([
#     Prod(name="Laptop", category="Electronics", quantity=15, price=30000, is_available=0),
#     Prod(name="Sofa", category="Furniture", quantity=22, price=28000, is_available=1),
# ])


# all_prod = Prod.objects.get(id=1)
# all_prod.get_product_details()

# OUTPUT
# ----------- Product id : 1 ----------
# Name : Laptop
# Category : Electronics
# Quantity : 0
# Price : 30000
# Is_Avail : 0


# data1 = Prod.get_available_products()
# print(data1)

# Output:
# <QuerySet [<Prod: {'_state': <django.db.models.base.ModelState object at 0x000002AB09950280>, 'id': 2, 'name': 'Sofa', 'category': 'Furniture', 'quantity': 22, 'price': 28000, 'is_available': 1}>, 
# <Prod:{'_state': <django.db.models.base.ModelState object at 0x000002AB09950370>, 'id': 4, 'name': 'Kid Dress', 'category': 'Cloth', 'quantity': 200, 'price': 3000, 'is_available': 1}>, 
# <Prod:{'_state': <django.db.models.base.ModelState object at 0x000002AB09950400>, 'id': 5, 'name': 'Showpiece', 'category': 'Home Decor', 'quantity': 34, 'price': 10000, 'is_available': 1}>]>


# data2 = Prod.get_unavailable_products()
# print(data2)

# <QuerySet [<Prod:{'_state': <django.db.models.base.ModelState object at 0x000002AB09950220>, 'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'quantity': 0, 'price': 30000, 'is_available': 0}>, 
# <Prod:{'_state': <django.db.models.base.ModelState object at 0x000002AB099502E0>, 'id': 3, 'name': 'Utensils', 'category': 'Appliances', 'quantity': 0, 'price': 12000, 'is_available': 0}>]>


# data =Prod.get_avg_all_prod()
# print(data)   # 11500.0


# data = Prod.get_prod_by_catgory()
# print(data)

# <QuerySet [<Prod: {'_state': <django.db.models.base.ModelState object at 0x00000246D86DC3D0>, 'id': 2, 'name': 'Sofa', 'category': 'Furniture', 'quantity': 22, 'price': 28000, 'is_available': 1}>, 
# <Prod:{'_state': <django.db.models.base.ModelState object at 0x00000246D86DC580>, 'id': 6, 'name': 'Chairs', 'category': 'Furniture', 'quantity': 12, 'price': 5000, 'is_available': 1}>]>

# data = Prod.objects.get(id=1)
# print(dir(data))

"""
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_field_name_clashes', '_check_fields', 
 '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', 
 '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', 
 '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', 
 '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', 
 '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', 
 '_save_parents', '_save_table', '_set_pk_val', '_state', 'category', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete',
  'from_db', 'full_clean', 'get_available_products', 'get_avg_all_prod', 'get_deferred_fields', 'get_name_of_prods', 
  'get_prod_by_catgory', 'get_product_details', 'get_unavailable_products', 'id', 'is_available', 'name', 'objects', 'pk',
   'prepare_database_save', 'price', 'quantity', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 
   'unique_error_message', 'validate_unique']
"""


# Prod.update_products_availablity()

# print(Prod.objects.all())

# <QuerySet [<Prod: Laptop ----1>, 
# <Prod: Sofa ----1>, 
# <Prod: Utensils ----1>, 
# <Prod: Kid Dress ----1>, 
# <Prod: Showpiece ----1>, 
# <Prod: Chairs ----1>]>


# data =Prod.filtered_prod()
# print(data)

# <QuerySet [<Prod: Sofa ----1>, <Prod: Showpiece ----1>]>

# data =Prod.prod_with_name_only()

# {'_state': <django.db.models.base.ModelState object at 0x0000014916DD8130>, 'id': 1, 'name': 'Laptop'}
# {'_state': <django.db.models.base.ModelState object at 0x0000014916DD81F0>, 'id': 2, 'name': 'Sofa'}
# {'_state': <django.db.models.base.ModelState object at 0x0000014916DD82B0>, 'id': 3, 'name': 'Utensils'}
# {'_state': <django.db.models.base.ModelState object at 0x0000014916DD8370>, 'id': 4, 'name': 'Kid Dress'}
# {'_state': <django.db.models.base.ModelState object at 0x0000014916DD8430>, 'id': 5, 'name': 'Showpiece'}
# {'_state': <django.db.models.base.ModelState object at 0x0000014916DD84F0>, 'id': 6, 'name': 'Chairs'}


# data = Prod.delete_prod_by_category()
# print(data)

# <QuerySet [<Prod: Laptop ----Electronics>,
# <Prod: Utensils ----Appliances>, 
# <Prod: Kid Dress ----Cloth>, 
# <Prod: Showpiece ----Home Decor>]>
