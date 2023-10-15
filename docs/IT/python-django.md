- related_name='+'
    - 如果你不希望 Django 创建一个反向关系，可以将 related_name 设置为 '+' 或者以 '+' 结束

- on_delete=models.CASCADE
    - 表示级联删除。也就是说，当关联对象被删除时，与之关联的对象也会被删除

- .only('id')
    - 

- update_or_create
    - Draw2DDevice.objects.update_or_create(defaults={'x': 777,'y': 777,}, device_id=13, version_id=1)
    - defaults是需要更新的数据字典，后面参数是用来查询的是否存在的，如果存在就更新，反之insert

- auto_now
    - 
- auto_now_add
    - 

- from drf_spectacular.utils import extend_schema

```
There are four steps involved in validating a model:

Validate the model fields - Model.clean_fields()
Validate the model as a whole - Model.clean()
Validate the field uniqueness - Model.validate_unique()
Validate the constraints - Model.validate_constraints()
All four steps are performed when you call a model’s full_clean() method.

When you use a ModelForm, the call to is_valid() will perform these validation steps for all the fields that are included on the form. 
```

- 重写model的save方法时，如何知道是create还是update？
    -

- @extend_schema(tags=["xxx"])

- serializer.is_valid()
    - 会执行哪些valid方法？


- from django.test import TestCase
    - def setUp(self) & def tearDown(self)
        - allow you to define instructions that will be executed before and after each test method.
        - python unittest中也有setUp 和 tearDown, 区别是什么？
            - 我猜测是一样的
    - def setUpTestData
        - it does not belong to unittest but to the Django framework. It is introduced in Django 1.8 as a class method of django.test.TestCase
        - It acts pretty much like setUpClass, except that the operations you do in setUpTestData will be rolled back after all tests of the same TestCase class are executed. Actually, setUpTestData is implemented in Django using setUpClass and tearDownClass.
        - The class-level atomic block described above allows the creation of initial data at the class level, once for the whole TestCase
            - 一次用于整个TestCase
        - Note that if the tests are run on a database with no transaction support (for instance, MySQL with the MyISAM engine), setUpTestData() will be called before each test, negating the speed benefits.
        Objects assigned to class attributes in setUpTestData() must support creating deep copies with copy.deepcopy() in order to isolate them from alterations performed by each test methods.
    - def setUpClass  &   def tearDownClass
        - setUpClass/tearDownClass会被调用一次，setUp/tearDown每个函数执行的时候都会被调用,所以需要一开始就初始化的数据内容，建议放在setUpClass，并且做好保护，譬如设置已存在就不再create数据

- from tastypie.resources import ALL_WITH_RELATIONS
/# Enable all basic ORM filters but do not allow filtering across relationships.
ALL = 1
/# Enable all ORM filters, including across relationships
ALL_WITH_RELATIONS = 2

- fields = [
- ordering = [
- filtering = {
```
        filtering = {
            'slug': ALL,
            'user': ALL_WITH_RELATIONS,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
```

- email = True

```
ImportError: cannot import name 'QUERY_TERMS' from 'django.db.models.sql.constants


```

- django signal and celery
    - https://medium.com/analytics-vidhya/integrating-django-signals-and-celery-cb2876ebd494

- related_name="+" related_name='+' 
    - If you’d prefer Django not to create a backwards relation, set related_name to '+' or end it with '+'.
        - if i have a backwards relation, i can access to related objects conveniently. why not use it? 
            - 
    - If you thus have two models A and B, then by setting a ForeignKey from A to B, Django will add a manager to B to obtain all related As for a given B, but by setting it to '+', we disable that behavior.

- migrations.RunPython
    - 

- 回滚
    - $ python3 manage.py migrate legal 0018