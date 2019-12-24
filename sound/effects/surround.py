"""
상대 임포트

from . import echo

from .. import formats

from ..filters import equalizar


상대 임포트가 현재 모듈의 이름에 기반을 둔다는 것에 주의하세요.
메인 모듈의 이름은 항상 "__main__" 이기 때문에, 파이썬 응용 프로그램의 메인 모듈로 사용될 목적의 모듈들은 반드시 절대 임포트를 사용해야 합니다.
"""


# from . import echo
# from .. import formats
# from ..filters import equalizer

from .echo import test_echo

test_echo_result = test_echo()
print(test_echo_result)

# if __name__ == "__main__":
#
#     test_echo_result = test_echo()
#     print(test_echo_result)

# wav_result = formats.wavread()
# print(wav_result)

# equalizer_result = equalizer.test_equalizer()
# print(equalizer_result)


