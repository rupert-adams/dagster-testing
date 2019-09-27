from dagster import pipeline, solid


@solid
def debug_message(context):
    context.log.debug('A Debug Message')


@solid
def error_message(context):
    context.log.error('An Error Message')


@pipeline
def execution_context_pipeline():
    debug_message()
    error_message()