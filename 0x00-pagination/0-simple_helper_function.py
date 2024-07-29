#!/usr/bin/env python3
"""
This module provides a function for calculating the start and end indices
for pagination given a page number and page size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start index and end index for the given page and page_size.

    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - Tuple[int, int]: A tuple containing the start index and end index for the given pagination parameters.
    """

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
