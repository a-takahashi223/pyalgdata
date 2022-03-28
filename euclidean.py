import logging

Complex = int | float | complex

logger = logging.getLogger(__name__)


def main(a: Complex, b: Complex) -> int:
    assert a.imag == 0, "aは実数"
    a = a.real
    assert float(a).is_integer()
    a = int(a)
    assert b.imag == 0, "bは実数"
    b = b.real
    assert float(b).is_integer()
    b = int(b)

    if a == 0:
        return 0

    a = abs(a)
    while a != 0:
        logger.debug("%s", (a, b))
        a, b = b % a, a

    logger.debug("%s", (a, b))
    return b


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    print(main(42, -30))
    print(main(-30, 42))
    print(main(30.0, 42 + 0j))
    print(main(-42, -30))
    print(main(0, -1))
    print(main(2, 0))
