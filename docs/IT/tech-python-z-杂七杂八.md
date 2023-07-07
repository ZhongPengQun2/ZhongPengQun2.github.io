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

- tenacity
  - stop_after_attempt
    - 重试次数

- python io module
  - Python io - BytesIO, StringIO
    - https://www.digitalocean.com/community/tutorials/python-io-bytesio-stringio
  - io.BytesIO
    - `Python io module allows us to manage the file-related input and output operations`
  - io.StringIO

#### pytest
- Is it possible that a function be mocked globally ?

- conftest.py

- TDD (Test Driven Development)

- pytest's fixture


#### pyinstaller
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


#### argparse
- from fabric.api import lcd

https://zhuanlan.zhihu.com/p/395173906?utm_id=0

- metavar

- action='append'

- 能否有多个parser ？




### Django doc notes
```
https://www.django-rest-framework.org/api-guide/serializers/

Expanding the usefulness of the serializers is something that we would like to address. However, it's not a trivial problem, and it will take some serious design work
扩展序列化程序的有用性是我们想要解决的问题。然而，这不是一个微不足道的问题，它需要一些认真的设计工作
```

- django serializer & drf serializer
- what should a serializer be ? i mean how to design a suitable serializer ?


#### Software lifecycle
- product & release
- release
    - refers: https://en.wikipedia.org/wiki/Software_release_life_cycle
    - alpha & beta & RC & GA release
        - RC
    - milestone release



#### jekyll
```shell
docker run -it  --rm jekyll/jekyll:3.5 bash

bundle exec jekyll serve

# gem sources -a http://gems.ruby-china.org
Error fetching http://gems.ruby-china.org:
        no such name (http://gems.ruby-china.org/specs.4.8.gz)



install ruby in ubuntu18.04 container by source code
https://tool.4xseo.com/article/501208.html
```


```shell
# kubectl get pods
The connection to the server localhost:8080 was refused - did you specify the right host or port?

[resolve] https://blog.csdn.net/a506681571/article/details/86086005

systemctl start etcd
systemctl start docker
systemctl start kube-apiserver
systemctl start kube-controller-manager
systemctl start kube-scheduler
systemctl start kubelet
systemctl start kube-proxy
----------------

```shell
# minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Stopped
kubeconfig: Configured

- 如何查看 apiserver 的 log ?
```

  - Django
      - Develop django project by docker.
      - safe url
      - url endswith '/' & not endswith
      - Path Parameters
      - setup project from legacy database
      - ALLOWED_HOSTS
        - HTTP Host header attacks
  - Django-rest-framework
      - 2种url参数的区别，为什么要这样？