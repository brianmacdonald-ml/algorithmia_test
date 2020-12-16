from . import test_with_git

def test_test_with_git():
    assert test_with_git.apply("Jane") == "hello Jane"
