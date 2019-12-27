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
