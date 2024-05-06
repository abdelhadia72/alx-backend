#!/usr/bin/env python3
''' File 0-simple_helper_function'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        function takes 2 int and return
        a tuple include start and end of the page
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
