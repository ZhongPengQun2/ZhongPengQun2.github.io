### PyInstaller
- .spec file
```python
# 
configuration = Analysis(['moccasin/__main__.py'],
                         pathex = ['.'],
                         binaries = [(libsbml_lib_path(), '.')],
                         datas = [],
                         hiddenimports = [],
                         hookspath = [],
                         runtime_hooks = [],
                         excludes = [],
                         win_no_prefer_redirects = False,
                         win_private_assemblies = False,
                         cipher = None,
                        )

application_pyz    = PYZ(configuration.pure,
                         configuration.zipped_data,
                         cipher = None,
                        )

executable         = EXE(application_pyz,
                         configuration.scripts,
                         configuration.binaries,
                         configuration.zipfiles,
                         configuration.datas,
                         name = 'moccasin',
                         debug = False,
                         strip = False,
                         upx = True,
                         runtime_tmpdir = None,
                         console = False,
                        )

app             = BUNDLE(executable,
                         name = 'MOCCASIN.app',
                         icon = 'dev/icon/moccasin.icns',
                         bundle_identifier = None,
                         info_plist = {'NSHighResolutionCapable': 'True'},
                        )
```

```python
subprocess.check_output(cmd, shell=True, text=True)
```

```python
>>> 'http://xx.com'.lstrip('xhttfffff://p')
'.com'
```
```shell
pytest tox.ini lint
```

- Python
    - python 3
    - logging
    - urllib urlparse
    -         "message": "Dangerous default value {} as argument",
    - super 放在不同的位置会怎样？
    - when staticmethod, when classmethod ?
    - collections
    - array & list
      - https://medium.com/backticks-tildes/list-vs-array-python-data-type-40ac4f294551
    - lambda, filter


- module from so file ?
```python
>>> import _tkinter
>>>
>>> _tkinter
<module '_tkinter' from '/usr/local/python-3.10.6-with-openssl-3.0.5/lib/python3.10/lib-dynload/_tkinter.cpython-310-x86_64-linux-gnu.so'>
>>>
```


