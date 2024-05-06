import csv
import math
from typing import List, Optional

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
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

        start_index, end_index = self.index_range(page, page_size)

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

    def index_range(self, page: int, page_size: int) -> tuple:
        start = (page - 1) * page_size
        end = start + page_size
        return start, end