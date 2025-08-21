import magic8ball

def test_with_name():
    result = magic8ball.magic_8_ball("Alice", "Will I win?")
    # check that result is a string
    assert isinstance(result, str)
    # check that the name appears in the answer
    assert "Alice" in result

def test_without_name():
    result = magic8ball.magic_8_ball("", "Is this a test?")
    # still should be a string
    assert isinstance(result, str)
    # check that "Question:" appears (because no name was given)
    assert "Question:" in result
