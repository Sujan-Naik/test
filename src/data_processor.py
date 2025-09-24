"""Data processing utilities for handling and transforming datasets.

This module provides classes and functions for common data processing tasks
including filtering, transformation, and statistical analysis.

Example:
    Basic usage of the DataProcessor class:
    
    >>> processor = DataProcessor([1, 2, 3, 4, 5])
    >>> processor.get_mean()
    3.0
    >>> processor.filter_greater_than(3)
    [4, 5]
"""

from typing import List, Union, Optional
import statistics


class DataProcessor:
    """A utility class for processing numerical data.
    
    This class provides methods for statistical analysis and data filtering
    operations on lists of numerical data.
    
    Attributes:
        data (List[Union[int, float]]): The dataset to process.
        
    Example:
        >>> processor = DataProcessor([10, 20, 30, 40, 50])
        >>> processor.get_sum()
        150
    """
    
    def __init__(self, data: List[Union[int, float]]) -> None:
        """Initialize the DataProcessor with a dataset.
        
        Args:
            data: A list of numerical values to process.
            
        Raises:
            ValueError: If the data list is empty.
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        self.data = data
    
    def get_mean(self) -> float:
        """Calculate the arithmetic mean of the dataset.
        
        Returns:
            The mean value as a float.
            
        Example:
            >>> processor = DataProcessor([2, 4, 6])
            >>> processor.get_mean()
            4.0
        """
        return statistics.mean(self.data)
    
    def get_median(self) -> float:
        """Calculate the median of the dataset.
        
        Returns:
            The median value as a float.
        """
        return statistics.median(self.data)
    
    def get_sum(self) -> Union[int, float]:
        """Calculate the sum of all values in the dataset.
        
        Returns:
            The total sum of all values.
        """
        return sum(self.data)
    
    def filter_greater_than(self, threshold: Union[int, float]) -> List[Union[int, float]]:
        """Filter values greater than the specified threshold.
        
        Args:
            threshold: The minimum value (exclusive) for filtering.
            
        Returns:
            A new list containing only values greater than the threshold.
            
        Example:
            >>> processor = DataProcessor([1, 5, 10, 15])
            >>> processor.filter_greater_than(7)
            [10, 15]
        """
        return [x for x in self.data if x > threshold]
    
    def normalize(self) -> List[float]:
        """Normalize the dataset to values between 0 and 1.
        
        Returns:
            A new list with normalized values.
            
        Raises:
            ValueError: If all values in the dataset are identical.
        """
        min_val = min(self.data)
        max_val = max(self.data)
        
        if min_val == max_val:
            raise ValueError("Cannot normalize data with identical values")
        
        return [(x - min_val) / (max_val - min_val) for x in self.data]


def calculate_correlation(x: List[float], y: List[float]) -> float:
    """Calculate the Pearson correlation coefficient between two datasets.
    
    Args:
        x: First dataset.
        y: Second dataset.
        
    Returns:
        The correlation coefficient between -1 and 1.
        
    Raises:
        ValueError: If the datasets have different lengths.
        
    Example:
        >>> calculate_correlation([1, 2, 3], [2, 4, 6])
        1.0
    """
    if len(x) != len(y):
        raise ValueError("Datasets must have the same length")
    
    return statistics.correlation(x, y)