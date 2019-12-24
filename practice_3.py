"""
# 1단계
1. from sound.effects import * 명령어를 통해 effects 내의 모든 모듈을 호출 합니다.
- 이상적으로는, 어떻게든 파일 시스템에서 패키지에 어떤 모듈들이 들어있는지 찾은 다음, 그것들 모두를 임포트 하기를 원할 것입니다.
- 이렇게 하는 데는 시간이 오래 걸리고 서브 모듈을 임포트 함에 따라 어떤 서브 모듈을 명시적으로 임포트할 경우만 일어나야만 하는 원하지 않는 부수적 효과가 발생할 수 있습니다.

2. 해결책
- 패키지의 __init__.py 코드가 __all__ 이라는 이름의 목록을 제공하면, 이것을 from package import * 를 만날 때 임포트 해야만 하는 모듈 이름들의 목록으로 받아들입니다.
- 설사 어떤 모듈이 import * 를 사용할 때 특정 패턴을 따르는 이름들만 익스포트 하도록 설계되었다 하더라도, 프로덕션 코드에서는 여전히 좋지 않은 사례
- 차라리 from package import specific_submodule 를 사용하는 게 훨씬 나은 코드이다.
"""

from sound.effects import *

test_echo_result = echo.test_echo()
print(f'test_echo_result : {test_echo_result}')

echo_filter_result = echo.echofilter(5, 4, 3, 2)
print(f'echo_filter_result : {echo_filter_result}')
