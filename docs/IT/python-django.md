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

