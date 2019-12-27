Python Package
----------
![alt text](https://img.shields.io/badge/version-Python3.6.5-red)
> Python Package 에 대해 이해하기 위해 작성하였습니다.

# Introduction
Python 에서 사용하고 있는 패키지를 호출하는 방법에 대해 이해하는 문서 입니다.

모든 내용은 Python 공식 문서를 바탕으로 작성 되었습니다.
- Official Document
  - KOR : https://docs.python.org/ko/3/tutorial/modules.html
  - ENG : https://docs.python.org/3/tutorial/modules.html

# 연습용 코드 다운로드
```
git clone https://github.com/timetobye/practice_python_package.git
```

# 작업 환경
- OS : macOS High Sierra
- version : Python 3.6.X

# Structure
- 공식 문서에서는 아래와 같은 구조를 잡고 설명하고 있습니다.
- 예시로 나와있는 항목에 대해 함수가 없어서 임의로 몇 개 만들어 두었습니다.

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

# 안내 사항
- 모든 코드 실행은 `sound directory`와 동일한 위치에 놓인 step_x.py 파일을 실행합니다.

# Step 1

1. `import sound.effects.echo` 명령어를 통해 `echo.py`를 호출 합니다.
2. `echo.py`에 존재하는 `test_echo()`를 호출 합니다.
3. return 값을 전달 받아 출력을 해봅니다.
4. 결과는 `test_echo` 로 나와야 정상 입니다.

```python
import sound.effects.echo

test_echo_result = sound.effects.echo.test_echo()
print(f'test_echo_result : {test_echo_result}')
```

# Step 2

1. `import sound.effects.echo` 명령어를 통해 `echo.py`를 호출 합니다.
2. `echo.py`에 존재하는 `echofilter` 함수를 호출 합니다.
3. 입력 받는 parameter 값은 4개로 input_value, output_value, delay, atten 입니다.
4. 편의상 숫자로 모두 입력 받겠습니다.
5. 결과는 input_value * delay + output_value * atten 의 계산 결과입니다.

````python
import sound.effects.echo

echo_filter_result = sound.effects.echo.echofilter(5, 4, 3, 2)
print(f'echo_filter_result : {echo_filter_result}')
````

# Step 3

1. `from sound.effects import echo` 명령어를 통해 `echo.py`를 호출 합니다. 이것도 서브 모듈 `echo` 를 로드하고, 패키지 접두어 없이 사용할 수 있게 합니다. 그래서 이런 식으로 사용할 수 있습니다.
2. `echo.py`에 존재하는 `echofilter()`를 호출 합니다.
3. 입력 받는 parameter 값은 4개로 input_value, output_value, delay, atten 입니다.
4. 편의상 숫자로 모두 입력 받겠습니다.
5. 결과는 input_value * delay + output_value * atten 의 계산 결과입니다.

````python
from sound.effects import echo

echo_filter_result = echo.echofilter(5, 4, 3, 2)
print(f'echo_filter_result : {echo_filter_result}')
````

Step2 와 다른 점은 `import sound.effects.echo` 방식이 아닌 `from sound.effects import echo` 이라는 것 입니다.


# Step 4

**issue**
`from sound.effects import *` 명령어를 통해 `effects` directory 내의 모든 모듈을 호출
- 이상적으로는, 어떻게든 파일 시스템에서 패키지에 어떤 모듈들이 들어있는지 찾은 다음, 그것들 모두를 임포트 하기를 원할 것입니다.
- 이렇게 하는 데는 시간이 오래 걸리고 서브 모듈을 임포트 함에 따라 어떤 서브 모듈을 명시적으로 임포트할 경우만 일어나야만 하는 원하지 않는 부수적 효과가 발생할 수 있습니다.

**solution**
- 패키지의 `__init__.py` 코드가 `__all__` 이라는 이름의 목록을 제공하면, 이것을 `from package import *` 를 만날 때 임포트 해야만 하는 모듈 이름들의 목록으로 받아들입니다.
- 설사 어떤 모듈이 `import *` 를 사용할 때 특정 패턴을 따르는 이름들만 익스포트 하도록 설계되었다 하더라도, 프로덕션 코드에서는 여전히 좋지 않은 사례
- 차라리 `from package import specific_submodule` 를 사용하는 게 훨씬 나은 코드이다.

````python
from sound.effects import *

test_echo_result = echo.test_echo()
print(f'test_echo_result : {test_echo_result}')

echo_filter_result = echo.echofilter(5, 4, 3, 2)
print(f'echo_filter_result : {echo_filter_result}')
````

# Step 5

**notice**
- 이 부분은 공식 문서를 따라하면서 고생을 좀 했습니다.
- **상대 임포트**를 다룹니다.
  - `sound - effects directory`의 `surround.py` 모듈에 작성되어 있습니다.

```bash
-- 공식 문서에 안내 된 상대 임포트 3가지

from . import echo : 실행 됨

from .. import formats : 실행 안 됨, 왜 안 되는지 모름

from ..filters import equalizar : 실행 됨
```

동일 directory 내 모듈 참조
- `from . import echo`
- surround 모듈에서 echo 모듈을 import 하려면 `.` 을 이용하면 됩니다.

다른 directory 내 모듈 참조
- `..filters import equalizar`
- surround 모듈에서 filters directory에 있는 equalizar 모듈을 import 하려면 `..directory` 을 이용하면 됩니다.


surround.py에는 다음과 같이 구성되어 있습니다.

```python
from . import echo
from ..filters import equalizer
# from .. import formats


def test_surround():
    result = echo.test_echo()

    return result


def test_filter_equalizer():
    result = equalizer.test_equalizer()

    return result


# def test_formats():
#     result = formats.auread.test_reverse()
#
#     return result
```

**실행은 surround.py 를 하는 것이 아닙니다.**
- 상대 임포트가 현재 모듈의 이름에 기반을 둔다는 것에 주의
- 메인 모듈의 이름은 항상 `"__main__"`이기 때문에, 파이썬 응용 프로그램의 메인 모듈로 사용될 목적의 모듈들은 반드시 절대 임포트를 사용해야 함
- sound `directory` 와 동일한 위치에서 실행합니다.

```python
from sound.effects import surround


def call_test_surround():
    result = surround.test_surround()

    return result


def call_test_filter():
    result = surround.test_filter_equalizer()

    return result


# def call_test_formats():
#     result = surround.test_formats()
#
#     return result


def main():
    surround_result = call_test_surround()
    print(surround_result)

    filter_result = call_test_filter()
    print(filter_result)


if __name__ == "__main__":
    main()
```

**상대 참조 보다는 절대 참조를 써서 보다 명시적으로 표현하는 것이 나을 것 같습니다.**