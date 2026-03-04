"""Tests for crashbytes-strutils."""

from __future__ import annotations

from crashbytes_strutils import (
    between,
    count_words,
    initials,
    is_blank,
    is_valid_email,
    mask,
    pad_left,
    pad_right,
    remove_whitespace,
    reverse,
    slugify,
    strip_html,
    to_camel_case,
    to_constant_case,
    to_kebab_case,
    to_pascal_case,
    to_snake_case,
    to_title_case,
    truncate,
)


class TestCaseConversion:
    def test_to_snake_case(self) -> None:
        assert to_snake_case("helloWorld") == "hello_world"
        assert to_snake_case("HelloWorld") == "hello_world"
        assert to_snake_case("hello-world") == "hello_world"
        assert to_snake_case("HELLO_WORLD") == "hello_world"
        assert to_snake_case("XMLParser") == "xml_parser"

    def test_to_camel_case(self) -> None:
        assert to_camel_case("hello_world") == "helloWorld"
        assert to_camel_case("HelloWorld") == "helloWorld"
        assert to_camel_case("hello-world") == "helloWorld"
        assert to_camel_case("") == ""

    def test_to_pascal_case(self) -> None:
        assert to_pascal_case("hello_world") == "HelloWorld"
        assert to_pascal_case("helloWorld") == "HelloWorld"

    def test_to_kebab_case(self) -> None:
        assert to_kebab_case("helloWorld") == "hello-world"
        assert to_kebab_case("hello_world") == "hello-world"

    def test_to_title_case(self) -> None:
        assert to_title_case("hello_world") == "Hello World"
        assert to_title_case("helloWorld") == "Hello World"

    def test_to_constant_case(self) -> None:
        assert to_constant_case("helloWorld") == "HELLO_WORLD"
        assert to_constant_case("hello-world") == "HELLO_WORLD"


class TestSlugify:
    def test_basic(self) -> None:
        assert slugify("Hello World") == "hello-world"

    def test_special_chars(self) -> None:
        assert slugify("Hello & World!") == "hello-world"

    def test_unicode(self) -> None:
        assert slugify("H\u00e9llo W\u00f6rld") == "hello-world"

    def test_multiple_dashes(self) -> None:
        assert slugify("hello   world") == "hello-world"

    def test_leading_trailing(self) -> None:
        assert slugify("  hello  ") == "hello"


class TestTruncate:
    def test_no_truncation_needed(self) -> None:
        assert truncate("hello", 10) == "hello"

    def test_truncation(self) -> None:
        assert truncate("hello world", 8) == "hello..."

    def test_custom_suffix(self) -> None:
        assert truncate("hello world", 8, "~") == "hello w~"

    def test_exact_length(self) -> None:
        assert truncate("hello", 5) == "hello"


class TestMask:
    def test_basic(self) -> None:
        assert mask("1234567890") == "******7890"

    def test_custom_visible(self) -> None:
        assert mask("1234567890", visible=2) == "********90"

    def test_custom_char(self) -> None:
        assert mask("1234567890", char="#") == "######7890"

    def test_short_string(self) -> None:
        assert mask("123", visible=4) == "123"


class TestBetween:
    def test_basic(self) -> None:
        assert between("Hello [World] End", "[", "]") == "World"

    def test_no_start(self) -> None:
        assert between("Hello World", "[", "]") is None

    def test_no_end(self) -> None:
        assert between("Hello [World", "[", "]") is None

    def test_empty_result(self) -> None:
        assert between("Hello [] End", "[", "]") == ""


class TestStripHtml:
    def test_basic(self) -> None:
        assert strip_html("<p>Hello</p>") == "Hello"

    def test_nested(self) -> None:
        assert strip_html("<div><b>Hello</b></div>") == "Hello"

    def test_no_tags(self) -> None:
        assert strip_html("Hello") == "Hello"

    def test_self_closing(self) -> None:
        assert strip_html("Hello<br/>World") == "HelloWorld"


class TestValidation:
    def test_valid_email(self) -> None:
        assert is_valid_email("user@example.com") is True

    def test_invalid_email(self) -> None:
        assert is_valid_email("not-an-email") is False

    def test_is_blank_none(self) -> None:
        assert is_blank(None) is True

    def test_is_blank_empty(self) -> None:
        assert is_blank("") is True

    def test_is_blank_whitespace(self) -> None:
        assert is_blank("   ") is True

    def test_is_blank_content(self) -> None:
        assert is_blank("hello") is False


class TestMisc:
    def test_reverse(self) -> None:
        assert reverse("hello") == "olleh"
        assert reverse("") == ""

    def test_count_words(self) -> None:
        assert count_words("hello world foo") == 3
        assert count_words("") == 0

    def test_initials(self) -> None:
        assert initials("John Doe") == "JD"
        assert initials("John Doe", separator=".") == "J.D"

    def test_pad_left(self) -> None:
        assert pad_left("42", 5, "0") == "00042"

    def test_pad_right(self) -> None:
        assert pad_right("hi", 5) == "hi   "

    def test_remove_whitespace(self) -> None:
        assert remove_whitespace("hello world") == "helloworld"
        assert remove_whitespace("  a  b  ") == "ab"
