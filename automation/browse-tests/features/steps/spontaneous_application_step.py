
from hamcrest import assert_that, is_

from pages.spontaneous_application_page import SpontaneousApplicationPage
from models.spontaneous_application_model import SpontaneousApplication

@given(u'I am on Spontaneous Application Page')
def step_impl(context):
    context.page_object = SpontaneousApplicationPage(context.driver)
    context.page_object.open_spontaneaus_application(context.base_url)

@when(u'I submit a default application without set the captcha')
def step_impl(context):
    context.spontaneous_application = SpontaneousApplication()
    context.page_object.set_name_text(context.spontaneous_application.name)
    context.page_object.set_seniority_combo(context.spontaneous_application.seniority)
    context.page_object.set_idd_combo(context.spontaneous_application.idd)
    context.page_object.set_telephone_text(context.spontaneous_application.telephone)
    context.page_object.set_technology_option(context.spontaneous_application.technology)
    context.page_object.set_email_text(context.spontaneous_application.email)
    context.page_object.set_linkedin_text(context.spontaneous_application.linkedin)
    context.page_object.click_on_autorize_recrut_check()
    context.page_object.click_on_autorize_jobopp_check()
    context.page_object.click_on_autorize_policy_check()
    context.page_object.click_on_save_button()

@then(u'I verify that email field is still filled')
def step_impl(context):
    assert_that(context.page_object.get_email_text(), is_(context.spontaneous_application.email))

@then(u'I verify the toast message is "{toast_message}"')
def step_impl(context, toast_message):
    assert_that(context.page_object.get_toast_message_text(), is_(toast_message))
