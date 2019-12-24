def test_echo():
    result = 'test_echo'

    return result


def echofilter(input_value, output_value, delay=0.7, atten=4):
    result = input_value * delay + output_value * atten

    return result
