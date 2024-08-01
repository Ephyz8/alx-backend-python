#!/usr/bin/env python3
"""
This module provides functionality for pagination using a Server class
and an index_range function to determine start and end indices.
"""

from typing import Tuple, List
import csv
import math

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.
    
    Args:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.
    
    Returns:
    - Tuple[int, int]: A tuple containing the start index and end index for the given pagination parameters.
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
        - List[List]: A list of rows corresponding to the specified page and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get paginated data and additional information about pagination.
        
        Args:
        - page (int): The current page number (1-indexed).
        - page_size (int): The number of items per page.
        
        Returns:
        - dict: A dictionary containing pagination information.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
