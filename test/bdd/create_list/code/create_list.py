from typing import Optional, List, Union


def create_list(element: Optional[Union[int, float, str]] = None) -> List[Optional[Union[int, float, str]]]:
    new_list = []
    if element:
        new_list.append(element)
    return new_list
