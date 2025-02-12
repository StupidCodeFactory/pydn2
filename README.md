# pydn2

**pydn2** is a Python binding for [libidn2](https://libidn.gitlab.io/libidn2/), the GNU implementation of the Internationalized Domain Names (IDNA) protocol (IDNA2008/TR46). This extension enables you to perform various domain name conversions—such as converting between Unicode (U-label) and ASCII-compatible (A-label) representations—and supports the full public API of libidn2.

## Features

- **Conversion Functions**
  - Convert Unicode domain names to their ASCII (Punycode) equivalents.
  - Convert Punycode domains back to Unicode.
  - Perform lookup conversions for registration and DNS lookup.
- **Error Handling**
  - Retrieve human-readable error messages and error code names.
- **Compliance with IDNA2008/TR46**
  - Uses flags to control normalization and processing (e.g. NFC, transitional/non-transitional).

## Requirements

- **libidn2**
  Make sure [libidn2](https://www.gnu.org/software/libidn/libidn2/manual/libidn2.html) is installed on your system. On macOS with Homebrew, you can install it via:
  ```bash
  brew install libidn2
  ```
  On linux debian based system:
  ```bash
  sudo apt-get -y install libidn2-0 libidn2-dev
  ```
- A C compiler that supports building Python C extensions.
- Python 3.9–3.12 (and possibly newer versions if you update the CI matrix).

## Installation

```bash
pip install pydn2
```

## Usage

```python
import pydn2

# Convert a Unicode domain to its ASCII (Punycode) representation:
ascii_domain = pydn2.to_ascii_8z("bücher", 0)
print(ascii_domain)  # e.g., "xn--bcher-kva"

# Convert a Punycode domain back to Unicode:
unicode_domain = pydn2.to_unicode_8z8z("xn--bcher-kva", 0)
print(unicode_domain)  # e.g., "bücher"

# You can also use flags for additional processing:
ascii_domain_transitional = pydn2.to_ascii_8z("☮️.com", pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)
print(ascii_domain_transitional)
```

## Module Constants

The extension exposes several flag constants for controlling conversion behavior:
- IDN2_NFC_INPUT – Apply NFC normalization on input.
- IDN2_ALABEL_ROUNDTRIP – Apply additional round-trip conversion of A-label inputs.
- IDN2_TRANSITIONAL – Perform Unicode TR46 transitional processing.
- IDN2_NONTRANSITIONAL – Perform Unicode TR46 non-transitional processing (default).
- IDN2_NO_TR46 – Disable any TR46 transitional or non-transitional processing.
- IDN2_USE_STD3_ASCII_RULES – Use STD3 ASCII rules.


## Benchmark

| Method                    | Conversion Output | Single-thread Benchmark (sec, 1,000,000 iterations) | Multi-thread Benchmark (sec, 1,000,000 iterations) |
|---------------------------|-------------------|----------------------------------------------------:|---------------------------------------------------:|
| **pydn2 (IDNA2008/TR46)** | `xn--i-n3p.com`   |                                            1.170304 |                                           1.156370 |
| **builtin (IDNA2003)**    | `xn--i-n3p.com`   |                                            6.716825 |                                           6.674858 |
