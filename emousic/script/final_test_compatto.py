from .final_result_majority import *
from .final_result_with_zero import *
from .final_result_without_zero import *

final_criteria = []
final_criteria.append(compute_result_with_zero)
final_criteria.append(compute_result_without_zero)
final_criteria.append(compute_result_majority)


def result_compatto(selection_list, criteria):
    compact_tuple = final_criteria[criteria](selection_list)
    return compact_tuple
