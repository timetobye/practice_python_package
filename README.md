Python Package
----------

> Python Package 에 대해 이해 합시다.

![alt text](https://img.shields.io/badge/version-Python3.6.5-red)


# 작업 중 임

# Introduction
Python 에서 사용하고 있는 패키지에 대해 공식 문서를 바탕으로 이해하는 문서 입니다.

모든 내용은 Python 공식 문서를 바탕으로 작서 되었습니다.
- Official Document
  - KOR : https://docs.python.org/ko/3/tutorial/modules.html
  - ENG : https://docs.python.org/3/tutorial/modules.html

# 설치 방법
```
git clone 주소
```

# 작업 환경
- OS : macOS High Sierra

윈도우에서는 작업 하지 않았습니다.
{: .notice--warning}


# Structure

```bash
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```




