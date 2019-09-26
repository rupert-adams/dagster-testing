from dagster import Field, execute_pipeline, pipeline, solid


@solid(config={'language': Field(str, is_optional=True, default_value='en-us')})
def hello_with_config(context):
    if context.solid_config['language'] == 'haw':
        return 'Aloha honua!'
    elif context.solid_config['language'] == 'cn':
        return '你好, 世界!'
    else:
        return 'Hello, world!'


@pipeline
def hello_with_config_pipeline():
    hello_with_config()