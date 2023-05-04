- django signal post_save 如何获取到changed的field？
    - Identify the changed fields in django post_save signal
    - 可以在pre_save的signal中设置一个varible来保存old值


```
/usr/local/lib/python3.6/dist-packages/django/db/models/fields/__init__.py:1369: RuntimeWarning: DateTimeField Release.created received a naive datetime (2020-05-03 00:00:00) while time zone support is active.


```


- migration file, elidable=True

- Squashing migrations
    - xx