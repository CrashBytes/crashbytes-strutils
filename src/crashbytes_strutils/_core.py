"""String utilities — case conversion, slugify, masking, and more."""

from __future__ import annotations

import re
import unicodedata

_EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
_WORD_BOUNDARY_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|[0-9]+")
_NON_ALPHANUM_RE = re.compile(r"[^a-z0-9]+")
_HTML_TAG_RE = re.compile(r"<[^>]+>")


def _split_words(text: str) -> list[str]:
    """Split text into words at case boundaries, spaces, hyphens, underscores."""
    return _WORD_BOUNDARY_RE.findall(text)


def to_snake_case(text: str) -> str:
    """Convert text to ``snake_case``."""
    return "_".join(w.lower() for w in _split_words(text))


def to_camel_case(text: str) -> str:
    """Convert text to ``camelCase``."""
    words = _split_words(text)
    if not words:
        return ""
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])


def to_pascal_case(text: str) -> str:
    """Convert text to ``PascalCase``."""
    return "".join(w.capitalize() for w in _split_words(text))


def to_kebab_case(text: str) -> str:
    """Convert text to ``kebab-case``."""
    return "-".join(w.lower() for w in _split_words(text))


def to_title_case(text: str) -> str:
    """Convert text to ``Title Case``."""
    return " ".join(w.capitalize() for w in _split_words(text))


def to_constant_case(text: str) -> str:
    """Convert text to ``CONSTANT_CASE``."""
    return "_".join(w.upper() for w in _split_words(text))


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = _NON_ALPHANUM_RE.sub("-", ascii_text).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate *text* to *max_length* characters, appending *suffix* if cut."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def mask(text: str, visible: int = 4, char: str = "*") -> str:
    """Mask all but the last *visible* characters."""
    if len(text) <= visible:
        return text
    return char * (len(text) - visible) + text[-visible:]


def between(text: str, start: str, end: str) -> str | None:
    """Extract the substring between *start* and *end*, or ``None``."""
    s = text.find(start)
    if s == -1:
        return None
    s += len(start)
    e = text.find(end, s)
    if e == -1:
        return None
    return text[s:e]


def strip_html(text: str) -> str:
    """Remove HTML tags from *text*."""
    return _HTML_TAG_RE.sub("", text)


def is_valid_email(value: str) -> bool:
    """Check if *value* is a valid email address."""
    return bool(_EMAIL_RE.match(value))


def is_blank(value: str | None) -> bool:
    """Check if *value* is ``None``, empty, or whitespace-only."""
    return value is None or value.strip() == ""


def reverse(text: str) -> str:
    """Reverse a string."""
    return text[::-1]


def count_words(text: str) -> int:
    """Count the number of words in *text*."""
    return len(text.split())


def initials(text: str, separator: str = "") -> str:
    """Extract initials from *text*."""
    return separator.join(w[0].upper() for w in text.split() if w)


def pad_left(text: str, length: int, char: str = " ") -> str:
    """Pad *text* on the left to *length* with *char*."""
    return text.rjust(length, char)


def pad_right(text: str, length: int, char: str = " ") -> str:
    """Pad *text* on the right to *length* with *char*."""
    return text.ljust(length, char)


def remove_whitespace(text: str) -> str:
    """Remove all whitespace from *text*."""
    return re.sub(r"\s+", "", text)
