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
