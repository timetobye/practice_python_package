"""
패키지 내부 간의 참조
- 패키지가 서브 패키지들로 구조화될 때 (예에서 나온 sound 패키지처럼), 이웃 패키지의 서브 모듈을 가리키는데 절대 임포트를 사용할 수 있습니다.
- 예를 들어, 모듈 sound.filters.vocoder 이 sound.effects 패키지의 echo 모듈이 필요하면, from sound.effects import echo 를 사용할 수 있습니다.

- 상대 임포트를 쓸 수도 있는데, from module import name 형태의 임포트 문을 사용합니다.
- 이 임포트는 상대 임포트에 수반되는 현재와 부모 패키지를 가리키기 위해 앞에 붙는 점을 사용합니다.
- 예를 들어, surround 모듈에서, 이렇게 사용할 수 있습니다:
"""

from sound.effects import echo

test_echo_result = echo.test_echo()
print(f'test_echo_result : {test_echo_result}')



