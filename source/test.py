import pandas as pd

def create_sample_dataframe():
    """
    Creates a sample DataFrame for demonstration purposes.

    Returns:
        pd.DataFrame: A sample DataFrame with random data.
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 40],
        'Score': [90, 85, 88, 92],
    }
    return pd.DataFrame(data)


def filter_by_score(dataframe, min_score):
    """
    Filters the DataFrame by a minimum score.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame.
        min_score (int): The minimum score to filter by.

    Returns:
        pd.DataFrame: A filtered DataFrame containing rows where the score >= min_score.
    """
    return dataframe[dataframe['Score'] >= min_score]


def calculate_average_age(dataframe):
    """
    Calculates the average age from the DataFrame.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame.

    Returns:
        float: The average age.
    """
    return dataframe['Age'].mean()


def add_bonus_score(dataframe, bonus_points):
    """
    Adds bonus points to the Score column of the DataFrame.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame.
        bonus_points (int): Points to add to each score.

    Returns:
        pd.DataFrame: A DataFrame with updated scores.
    """
    dataframe['Score'] += bonus_points
    return dataframe


def sort_by_age(dataframe, ascending=True):
    """
    Sorts the DataFrame by the Age column.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame.
        ascending (bool): Sort order. True for ascending, False for descending.

    Returns:
        pd.DataFrame: The sorted DataFrame.
    """
    return dataframe.sort_values(by='Age', ascending=ascending)
