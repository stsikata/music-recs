import pytest

# working through possible error message/exit: https://docs.pytest.org/en/latest/getting-started.html#our-first-test-run
def fail_test():
    raise SystemExit(1)

def test_fail():
    with pytest.raises(SystemExit):
            fail_test()
