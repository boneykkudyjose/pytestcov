def lower_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.lower()

def test_capitalize_string():
    assert lower_string('Test') == 'Test'