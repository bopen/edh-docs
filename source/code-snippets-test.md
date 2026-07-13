# Code snippets test

This page exercises Python code snippets in MyST Markdown with the Shibuya
theme. Hover over a block to reveal its copy button.

## Basic Python

Use a fenced block with a language for the common case. Pygments provides the
syntax highlighting.

```python
def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15
```

Inline code, such as `celsius_to_kelvin(20)`, is best for short names and
expressions.

## Caption, line numbers, and emphasis

Use the `code-block` directive when a snippet needs presentation options. The
`name` also makes {ref}`this featured snippet <average-temperature-snippet>`
referenceable.

```{code-block} python
:caption: Calculate an average temperature
:name: average-temperature-snippet
:linenos:
:emphasize-lines: 4,7

from statistics import fmean

def average_temperature(readings: list[float]) -> float:
    values = tuple(readings)
    if not values:
        raise ValueError("readings must not be empty")
    return fmean(values)
```

## Python console

Use the `pycon` lexer for an interactive session. The copy button omits the
`>>>` prompts and displayed output, leaving runnable input.

```{code-block} pycon
>>> readings = [12.4, 13.1, 12.9]
>>> round(sum(readings) / len(readings), 1)
12.8
```

## Code from a file

Use `literalinclude` for maintained or executable examples so the documentation
does not duplicate the source. It can select a Python object or a range of
lines.

```{literalinclude} _snippets/test_snippet.py
:language: python
:pyobject: celsius_mean
:caption: _snippets/test_snippet.py
:linenos:
:emphasize-lines: 4-5
```

## Dark code

Shibuya's `dark-code` class gives one block a dark treatment that is visible
when the documentation is in light mode.

```{code-block} python
:class: dark-code

theme_options = {
    "dark_code": True,
}
```

## Plain text

Use `text` when syntax highlighting would add no value. Copy still works.

```text
EDH_DATASET=example-dataset
EDH_REGION=global
```

## Collapsible code blocks

Both examples below collapse the whole code block rather than selected lines.

### Toggle button

The `toggle` class is provided by `sphinx-togglebutton`.

```{code-block} python
:class: toggle

def normalize(values: list[float]) -> list[float]:
    maximum = max(values)
    return [value / maximum for value in values]
```

### Dropdown

The `dropdown` directive is provided by `sphinx-design`.

````{dropdown} Show the complete example
```{code-block} python
def normalize(values: list[float]) -> list[float]:
    maximum = max(values)
    return [value / maximum for value in values]

normalized = normalize([2.0, 4.0, 8.0])
```
````
