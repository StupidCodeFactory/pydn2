import pytest
import pydn2

def test_to_ascii_8z():
    """
    Converts a UTF-8 encoded Unicode domain name into its ASCII (Punycode) representation.
    """
    domain = "bücher"
    result = pydn2.to_ascii_8z(domain, 0)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_to_unicode_lzlz():
    """
    Converts a possibly ACE encoded domain name (in the locale’s encoding) into a Unicode string
    encoded in the current locale’s character set.
    """
    punycode = "xn--bcher-kva"
    result = pydn2.to_unicode_lzlz(punycode, 0)
    assert isinstance(result, str)
    assert "bücher" in result

def test_to_unicode_8z8z():
    """
    Converts a possibly ACE encoded UTF-8 domain name into a UTF-8 Unicode string.
    """
    punycode = "xn--bcher-kva"
    result = pydn2.to_unicode_8z8z(punycode, 0)
    assert isinstance(result, str)
    assert "bücher" in result

def test_register_u8():
    """
    Performs IDNA2008 register conversion on a domain label given as both a UTF-8 U-label and ACE A-label.
    """
    ulabel = "bücher"
    alabel = "xn--bcher-kva"
    result = pydn2.register_u8(ulabel, alabel, 0)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_to_ascii_lz():
    """
    Converts a domain name in the locale’s encoding to its ASCII representation using IDNA2008 rules.
    """
    domain = "bücher"
    result = pydn2.to_ascii_lz(domain, 0)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_to_unicode_8zlz():
    """
    Converts a possibly ACE encoded UTF-8 domain name into a string encoded in the current locale’s character set.
    """
    punycode = "xn--bcher-kva"
    result = pydn2.to_unicode_8zlz(punycode, 0)
    assert isinstance(result, str)
    assert "bücher" in result

def test_lookup_ul():
    """
    Performs IDNA2008 lookup conversion on a domain name in the locale’s encoding,
    transcoding it to UTF-8 and NFC normalization.
    """
    domain = "bücher"
    result = pydn2.lookup_ul(domain, 0)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_register_ul():
    """Performs IDNA2008 register conversion on a domain label given in the locale’s encoding."""
    ulabel = "bücher"
    alabel = "xn--bcher-kva"
    result = pydn2.register_ul(ulabel, alabel, 0)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_strerror():
    """
    Converts an internal error code to a human-readable error message.
    """
    result = pydn2.strerror(-1)
    assert isinstance(result, str)
    assert len(result) > 0

def test_strerror_name():
    """
    Converts an internal error code to its corresponding error name.
    """
    result = pydn2.strerror_name(-1)
    assert isinstance(result, str)
    assert len(result) > 0


def test_to_ascii_8z_emoji():
    domain = "☮️.com"
    result = pydn2.to_ascii_8z(domain, pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_to_unicode_8z8z_emoji():
    domain = "😀domain"
    ascii_result = pydn2.to_ascii_8z(domain, pydn2.IDN2_NFC_INPUT  | pydn2.IDN2_TRANSITIONAL)
    result = pydn2.to_unicode_8z8z(ascii_result, pydn2.IDN2_NFC_INPUT)
    assert isinstance(result, str)
    assert "😀" in result

@pytest.mark.skip(reason="Unsure if libidn2 supports this")
def test_register_u8_emoji():
    ulabel = "☮️.com"
    alabel = pydn2.to_ascii_8z(ulabel, pydn2.IDN2_NFC_INPUT  | pydn2.IDN2_TRANSITIONAL)
    result = pydn2.register_u8(ulabel, alabel, pydn2.IDN2_TRANSITIONAL)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_to_ascii_lz_emoji():
    domain = "😀domain"
    result = pydn2.to_ascii_lz(domain, pydn2.IDN2_NFC_INPUT  | pydn2.IDN2_TRANSITIONAL)
    assert isinstance(result, str)
    assert result.startswith("xn--")

def test_to_unicode_8zlz_emoji():
    domain = "😀domain"
    ascii_domain = pydn2.to_ascii_8z(domain, pydn2.IDN2_NFC_INPUT  | pydn2.IDN2_TRANSITIONAL)
    result = pydn2.to_unicode_8zlz(ascii_domain, pydn2.IDN2_NFC_INPUT)
    assert isinstance(result, str)
    assert "😀" in result

def test_to_unicode_lzlz_emoji():
    domain = "😀domain"
    ascii_domain = pydn2.to_ascii_lz(domain, pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)
    result = pydn2.to_unicode_lzlz(ascii_domain, pydn2.IDN2_NFC_INPUT)
    assert isinstance(result, str)
    assert "😀" in result

def test_lookup_ul_emoji():
    domain = "😀domain"
    result = pydn2.lookup_ul(domain, pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)
    assert isinstance(result, str)
    assert result.startswith("xn--")

@pytest.mark.skip(reason="Unsure if libidn2 supports this")
def test_register_ul_emoji():
    ulabel = "☮️.com"
    alabel = pydn2.to_ascii_8z(ulabel, pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)
    result = pydn2.register_ul(ulabel, alabel, pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)
    assert isinstance(result, str)
    assert result.startswith("xn--")
