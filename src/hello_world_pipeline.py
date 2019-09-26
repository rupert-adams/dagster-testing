from dagster import String, execute_pipeline, pipeline, solid


@solid
def add_hello_to_world(_, word: String) -> String:
    return 'Hello, ' + word + '!'


@pipeline
def hello_inputs_pipeline():
    add_hello_to_world()