# crashbytes-strutils

Zero-dependency string utilities — case conversion, slugify, masking, and more.

## Install

```bash
pip install crashbytes-strutils
```

## Usage

```python
from crashbytes_strutils import to_snake_case, slugify, mask, truncate

to_snake_case("helloWorld")      # "hello_world"
slugify("Hello World!")          # "hello-world"
mask("4111111111111111")         # "************1111"
truncate("Long text here", 10)  # "Long te..."
```

## API

### Case Conversion
`to_snake_case`, `to_camel_case`, `to_pascal_case`, `to_kebab_case`, `to_title_case`, `to_constant_case`

### Text Manipulation
`slugify`, `truncate`, `mask`, `between`, `strip_html`, `reverse`, `pad_left`, `pad_right`, `remove_whitespace`

### Validation
`is_valid_email`, `is_blank`

### Analysis
`count_words`, `initials`

## License

MIT
