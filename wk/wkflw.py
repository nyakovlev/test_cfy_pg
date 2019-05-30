from cloudify.decorators import workflow
from cloudify.workflows import ctx

@workflow
def test_wkflw(**kwargs):
    ctx.logger.info("Workflow successfully executed!!!")
