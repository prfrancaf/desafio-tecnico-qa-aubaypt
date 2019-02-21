from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SpontaneousApplicationPage(BasePage):
    SPONTANEAUS_APPLICATION_URL = "/Home/SpontaneausApp?culture=en-us"
    NAME_TEXT = (By.ID, "Nome")
    SENIORITY_COMBO = (By.ID, "NivelProfissionalId")
    IDD_COMBO = (By.ID, "TelemovelList")
    TELEPHONE_TEXT = (By.ID, "Telemovel")
    TECHNOLOGIES_OPTIONS = (By.ID, "Tecnologias")
    EMAIL_TEXT = (By.ID, "Email")
    LINKEDIN_TEXT = (By.ID, "Linkedin")
    AUTORIZE_RECRUT_CHECK = (By.ID, "AutorizeRecrut")
    AUTORIZE_JOBOPP_CHECK = (By.ID, "AutorizeJobOpp")
    AUTORIZE_POLICY_CHECK = (By.ID, "AutorizePolicy")
    SAVE_BUTTON = (By.ID, "Save")

    def open_spontaneaus_application(self, base_url):
        url = base_url + self.SPONTANEAUS_APPLICATION_URL
        super().open_url(url)

    def set_name_text(self, text):
        super().type_in(self.NAME_TEXT, text)

    def set_seniority_combo(self, text):
        super().select_by_visible_text(self.SENIORITY_COMBO, text)

    def set_idd_combo(self, text):
        super().select_by_visible_text(self.IDD_COMBO, text)

    def set_telephone_text(self, text):
        super().type_in(self.TELEPHONE_TEXT, text)

    def set_technology_option(self, text):
        super().select_by_visible_text(self.TECHNOLOGIES_OPTIONS, text)

    def set_email_text(self, text):
        super().type_in(self.EMAIL_TEXT, text)

    def get_email_text(self):
        return super().find(self.EMAIL_TEXT).get_attribute("value")

    def set_linkedin_text(self, text):
        super().type_in(self.LINKEDIN_TEXT, text)

    def click_on_autorize_recrut_check(self):
        super().click(self.AUTORIZE_RECRUT_CHECK)

    def click_on_autorize_jobopp_check(self):
        super().click(self.AUTORIZE_JOBOPP_CHECK)

    def click_on_autorize_policy_check(self):
        super().click(self.AUTORIZE_POLICY_CHECK)

    def click_on_save_button(self):
        super().click(self.SAVE_BUTTON)
