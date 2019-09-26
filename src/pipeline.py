from dagster import execute_pipeline, pipeline, solid


@solid
def solid_one(_):
    return 'foo'


@solid
def solid_two(_, arg_one):
    return arg_one * 2


@pipeline
def hello_dagster_pipeline():
    return solid_two(solid_one())


if __name__ == '__main__':
    result = execute_pipeline(hello_dagster_pipeline)
    assert result.success