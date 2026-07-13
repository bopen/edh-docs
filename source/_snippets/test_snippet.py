"""Examples used by the code snippet test page."""

from collections.abc import Iterable


def celsius_mean(values: Iterable[float]) -> float:
    """Return the mean of the supplied Celsius values."""
    samples = tuple(values)
    if not samples:
        raise ValueError("values must not be empty")
    return sum(samples) / len(samples)
