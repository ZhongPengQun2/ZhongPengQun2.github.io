- django signal post_save 如何获取到changed的field？
    - Identify the changed fields in django post_save signal
    - 可以在pre_save的signal中设置一个varible来保存old值


```
/usr/local/lib/python3.6/dist-packages/django/db/models/fields/__init__.py:1369: RuntimeWarning: DateTimeField Release.created received a naive datetime (2020-05-03 00:00:00) while time zone support is active.


```


- migration file, elidable=True

- Squashing migrations
    - xx

- queryset 
    - https://www.oschina.net/translate/django-querysets?print
        - queryset是有cache的，因此 `for x in A.objects.filter()`只会运行一次select，但是result会都塞在memory中.
            - iterator可以防止大cache，但是会增加查询次数

- iterator

- from_db
    - Official doc: https://docs.djangoproject.com/en/4.1/ref/models/instances/#customizing-model-loading
    - 该方法什么时候被调用？每次query是都会被调用吗？

- update_fields
    - for better performance
        - https://dev.to/sankalpjonna/save-your-django-models-using-updatefields-for-better-performance-50ig


- django 的 signal 什么时候用比较好？

- mute_signals
    - Disable the list of selected signals when calling the factory, and reactivate them upon leaving.

    