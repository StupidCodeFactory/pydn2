import pytest
import pydn2

def test_to_ascii():
    """
    Test that pydn2.to_ascii correctly converts a Unicode domain name to its ASCII (Punycode) representation.
    """
    # Use a domain with non-ASCII characters.
    # In this example, "bücher" should convert to "xn--bcher-kva".
    input_domain = "bücher"
    expected_ascii = "xn--bcher-kva"

    # Call the to_ascii function without explicitly providing flags (default flags should be used).
    ascii_result = pydn2.to_ascii(input_domain)
    assert ascii_result == expected_ascii

def test_to_ascii_with_flags():
    """
    Test that the optional flags parameter works as expected.
    """
    input_domain = "bücher"
    expected_ascii = "xn--bcher-kva"

    # Even when passing flags explicitly (here, 0), the result should remain the same.
    ascii_result = pydn2.to_ascii(input_domain, 0)
    assert ascii_result == expected_ascii

def test_invalid_input_type():
    """
    Test that calling to_ascii with a non-string value raises a TypeError.
    """
    # pydn2.to_ascii is written to accept a string.
    # Passing an integer should cause PyArg_ParseTuple to fail and raise a TypeError.
    with pytest.raises(TypeError):
        pydn2.to_ascii(123)
