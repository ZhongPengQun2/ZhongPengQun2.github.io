- modules
    - getopt
    - getpass
    - syslog
    - Fabric

- python中有对应c中make的项目build工具吗？

- asyncio


```python
>>> a=[]
>>> b=a
>>> b.append(1)
>>> b
[1]
>>> a
[1]
```


- Environment
    - pylintrc


- pip与LD_LIBRARY_PATH


- python3 -m ensurepip
    - ensurepip
        - 该调用会在当前未安装 pip 的情况下安装 pip ，如已安装则无事发生

- Pyenv
    - https://github.com/pyenv/pyenv/wiki#suggested-build-environment

- re module
    - \t
    - 
    ```
    >>>re.findall('.{3}aaa.{1}', "\nxxxaaaxxaaaffff")
    ['xxxaaax']
    ```

- PYTHONPATH
```
Pythonpath is an environment variable that is used to specify the location of Python libraries. It is typically used by developers to ensure that their code can find the required Python libraries when it is run.
```

- pip3 升级
    - https://www.jianshu.com/p/34235f5d484a
        - pip3 install --upgrade pip



```
>>> x=re.search("clients3_linux_amd64_(?P<version>.*).tar.bz2", "clients3_linux_amd64_2022-01-01.tar.bz2")
>>> x['version']

what doese `?P` mean ?
```

- b'' 的意思？比如 b'2023.06.09'
    - 意思在2和3中不同



#### py2
- Classic python low level libs

- test-driven


#### py3
- Why python2 is deprecated ? And what's the advantage of python3 ?
  - Many data science libs has stop supporting for py2, like numpy.
  - Type hinting
  - pathlib module
  - Type hinting
    - type-hinting is just a note of code ?
      - Yes, but still can enforce checking by use module https://github.com/RussBaz/enforce
  - glob module
  - format string
  - divison
  - Strict ordering
  - Unicode for NLP
  - More reable useage in ML modules, like numpy
    - `Matrix multiplication with @`
  - Preserving order of dictionaries and **kwargs
  - Iterable
  - pickle module
  - super() function
    - please explain how to use super() by yourself.
  - Future-proof APIs with keyword-only arguments
    - 这个挺实用的
  - @dataclass
    - it's to replace `namedtuple` in python2
      - namedtuple: https://blog.csdn.net/qq_30159015/article/details/80356226
  - Built-in breakpoint()

  - references:
    - https://github.com/arogozhnikov/python3_with_pleasure
    - https://www.toptal.com/python/python-3-is-it-worth-the-switch
    - https://snarky.ca/why-python-3-exists/


- Underscores in Python

- How to upgrade python, e.g. upgrade python3.6 on your machine to python3.9
  - https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/

- Class in Class ?

- 给hint type做强制，实现强类型。。

- 当可以用py2和py3实现时，是否有lint tool来限制只能用py3的语法呢？也就是避免使用py2

- `with open(` 的几种模式:
```
The opening modes are exactly the same as those for the C standard library function fopen().
The BSD fopen manpage defines them as follows:
 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
```

如何把 python3.9 build成一个单独的binary在linux下运行，有可能吗？

- python -c 中 tab 怎么写？


- io.BytesIO()
  - .seek(0)