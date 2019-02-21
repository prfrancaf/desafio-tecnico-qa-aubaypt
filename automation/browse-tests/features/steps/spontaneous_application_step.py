
from hamcrest import assert_that, is_

from pages.spontaneous_application_page import SpontaneousApplicationPage

@given(u'I am on Spontaneous Application Page')
def step_impl(context):
    context.page_object = SpontaneousApplicationPage(context.driver)
    context.page_object.open_spontaneaus_application(context.base_url)

@when(u'I submit a default application without set the captcha')
def step_impl(context):
    context.page_object.set_name_text("Paulo Franca")
    context.page_object.set_seniority_combo("Junior")
    context.page_object.set_idd_combo("+55 (Brazil)")
    context.page_object.set_telephone_text("81999999999")
    context.page_object.set_technology_option("Phyton")
    context.page_object.set_email_text("nypyqela@getnada.com")
    context.page_object.set_linkedin_text("https://www.linkedin.com/in/paulo-roberto-fran%C3%A7a-filho-b013298b/")
    context.page_object.click_on_autorize_recrut_check()
    context.page_object.click_on_autorize_jobopp_check()
    context.page_object.click_on_autorize_policy_check()
    context.page_object.click_on_save_button()

@then(u'I verify that email field is still filled')
def step_impl(context):
    assert_that(context.page_object.get_email_text(), is_("nypyqela@getnada.com"))
