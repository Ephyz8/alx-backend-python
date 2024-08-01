#!/usr/bin/env python3
"""
This module provides a function for calculating the start and end indices
for pagination given a page number and page size and a class to paginate
a dataset of popular baby names
"""


from typing import Tuple, List
import cs


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
    - page (int): The current page number (1-indexed)
    - page_size (int): The number of items per page.
    Returns:
    - Tuple[int, int]: A tuple containing the start index and 
end index for the given pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""


    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the paginated data for a given page and page size.
        
        Args:
        - page (int): The current page number (1-indexed).
        - page_size (int): The number of items per page.   
        Returns:
        - List[List]: A list of rows corresponding to the 
specified page and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start:end]
