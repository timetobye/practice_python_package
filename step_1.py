"""
1. import sound.effects.echo 명령어를 통해 echo.py를 호출 합니다.
2. echo.py에 존재하는 test_echo()를 호출 합니다.
3. return 값을 전달 받아 출력을 해봅니다.
4. 결과는 `test_echo` 로 나와야 정상 입니다.
"""

import sound.effects.echo

test_echo_result = sound.effects.echo.test_echo()
print(f'test_echo_result : {test_echo_result}')


