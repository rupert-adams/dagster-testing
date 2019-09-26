from dagster import execute_pipeline, pipeline, solid


@solid
def return_one(_):
    return 1


@solid
def multiply_by_two(_, arg_a):
    return arg_a * 2


@solid
def multiply_by_three(_, arg_a):
    return arg_a * 3


@solid
def multiply(_, arg_b, arg_c):
    return arg_b * arg_c


@pipeline
def actual_dag_pipeline():
    one = return_one()
    multiply(multiply_by_two(one), multiply_by_three(one))


if __name__ == '__main__':
    result = execute_pipeline(actual_dag_pipeline)
    assert result.success