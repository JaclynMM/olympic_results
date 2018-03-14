from datamerge import *


# This creates a bool column to match search term with search term being male. How many male medalists?

def create_bool_field_from_search_term(data_sample, search_term):
    new_array = []
    new_array.append(data_sample[0].append(search_term))

    for row in data_sample[1:]:
        new_bool_field = False
        if search_term in row[6]:
            new_bool_field = True

        row.append(new_bool_field)
        new_array.append(row)

    return new_array

def filter_col_by_bool(data_sample, col):
    matches_search_term = []

    for item in data_sample[1:]:
        if item[col]:
            matches_search_term.append(item)

    return matches_search_term

new_csv = create_bool_field_from_search_term(results, "men")
number_of_male_medalists = results(filter_col_by_bool(new_csv, 9))
print("Male Medal Winners:" number_of_male_medalists(new_csv))