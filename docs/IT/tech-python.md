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
