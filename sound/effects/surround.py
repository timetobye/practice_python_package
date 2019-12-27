"""
상대 임포트
- from . import echo
- from .. import formats
- from ..filters import equalizar

상대 임포트가 현재 모듈의 이름에 기반을 둔다는 것에 주의
메인 모듈의 이름은 항상 "__main__" 이기 때문에, 파이썬 응용 프로그램의 메인 모듈로 사용될 목적의 모듈들은 반드시 절대 임포트를 사용해야 함
"""
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
