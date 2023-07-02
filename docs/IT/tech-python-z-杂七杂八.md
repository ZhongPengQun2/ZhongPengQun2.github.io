### PyInstaller
- .spec file
```python
# 该 moccasin/__main__.py 会被pyinstaller生成为一个可执行文件
configuration = Analysis(['moccasin/__main__.py'],    
#pathex = ['D:\\Company\\project\\untitled', 'D:\\Company']
#意思是项目需要从什么地方导入自定义库
#from mypath.util import module1  # 从D:\\Company\\project\\untitled找到mypath文件夹下面的util下面的module1
                         pathex = ['.', 'lib/python/', 'bin/'],
                         binaries = [(libsbml_lib_path(), '.')],  # 动态库
#项目需要用到什么数据，比如图片，视频等。里面格式为tuple，第一个参数是文件路径，第二个是打包后所在的路径。
#下面的代码意思就是，把image下面的所有以png结尾的文件打包到exe所在目录下的data/image目录下。把pdf目录下的#test.pdf文件打包到exe所在目录的data/pdf目录下
                         datas=[
                          ('image/*.png','data/image'),                        
                          ('pdf/test.pdf','data/pdf')
                         ],
                         hiddenimports = [],
                         hookspath = [],
                         runtime_hooks = [],
                         excludes = [],
                         win_no_prefer_redirects = False,
                         win_private_assemblies = False,
                         cipher = None,   # 加密密钥（一般无加密需求，可不设置）
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


- 参数 `--onefile`

- LD_LIBRARY_PATH=$(PY_LD_PATH) virtualenv/bin/pip3.9 install -r requirements.txt;


```
$ pyinstaller xxx-yyy.spec
The 'enum34' package is an obsolete backport of a standard library package and is incompatible with PyInstaller. Please `pip uninstall enum34` then try again.


```
```
857 INFO: UPX is not available.

```

- pyinstaller specific python version


- upx
  - upx=True
    - UPX is a free utility available for most operating systems. UPX compresses executable files and libraries, making them smaller, sometimes much smaller. UPX is available for most operating systems and can compress a large number of executable file formats

- raise_for_status()
  - 