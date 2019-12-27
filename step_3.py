"""
1. from sound.effects import echo 명령어를 통해 echo.py를 호출 합니다.
- 이것도 서브 모듈 echo 를 로드하고, 패키지 접두어 없이 사용할 수 있게 합니다. 그래서 이런 식으로 사용할 수 있습니다.

2. echo.py에 존재하는 echofilter()를 호출 합니다.
3. 입력 받는 parameter 값은 4개로 input_value, output_value, delay, atten 입니다.
4. 편의상 숫자로 모두 입력 받겠습니다.
5. 결과는 input_value * delay + output_value * atten 의 계산 결과입니다.
"""

from sound.effects import echo

echo_filter_result = echo.echofilter(5, 4, 3, 2)
print(f'echo_filter_result : {echo_filter_result}')