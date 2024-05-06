#!/usr/bin/env python3
''' File simple_pagination'''

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(
            page, int) and page > 0, "Page number must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        total_rows = len(dataset)
        total_pages = (total_rows + page_size - 1) // page_size

        if page > total_pages:
            return []

        start_index = (page - 1) * page_size
        end_index = min(start_index + page_size, total_rows)

        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        function takes 2 int and return
        a tuple include start and end of the page
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
