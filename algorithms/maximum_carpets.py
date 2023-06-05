from typing import Dict, List, Union

def buy_maximum_carpets(
    carpets: List[Dict[str, Union[str, int]]],
    budget: int,
) -> List[Dict[str, Union[str, int]]]:
    """
    Time Complexity: O(num_carpets * budget)
    Space Complexity: O((num_carpets + 1) * (budget + 1))
    """
    num_carpets = len(carpets)
    # Create a table to store the maximum number of carpets for the given budget
    table = [[0] * (budget + 1) for _ in range(num_carpets + 1)]

    for i in range(1, num_carpets + 1):
        for j in range(1, budget + 1):
            # If the current carpet's price is less than or equal to the current budget,
            # we have two choices: include the carpet or exclude it
            if carpets[i - 1]['price'] <= j:
                # Calculate the maximum number of carpets by considering both choices
                table[i][j] = max(table[i - 1][j], table[i - 1][j - carpets[i - 1]['price']] + 1)
            else:
                # If the current carpet's price is greater than the budget, exclude the carpet
                table[i][j] = table[i - 1][j]

    # Trace back the table to find the carpets that were selected
    selected_carpets = []
    i, j = num_carpets, budget
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            selected_carpets.append(carpets[i - 1])
            j -= carpets[i - 1]['price']
        i -= 1

    return selected_carpets
