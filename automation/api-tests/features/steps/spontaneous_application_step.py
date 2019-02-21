from apis.spontaneous_application_api import post_spontaneous_candidate
from models.spontaneous_application_model import SpontaneousApplication

from hamcrest import assert_that, is_

@when(u'I submit a default application')
def step_impl(context):
    spontaneous_application = SpontaneousApplication()
    context.post_spontaneous_candidate_response = post_spontaneous_candidate(context.base_url, spontaneous_application.__dict__)

@when(u'I submit a application without a name')
def step_impl(context):
    spontaneous_application = SpontaneousApplication()
    del spontaneous_application.Name
    context.post_spontaneous_candidate_response = post_spontaneous_candidate(context.base_url, spontaneous_application.__dict__)

@then(u'I verify the application response is "{status_code:d}"')
def step_impl(context, status_code):
    assert_that(context.post_spontaneous_candidate_response.status_code, is_(status_code))
