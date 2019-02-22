Feature: Spontaneous Application

    Scenario: Submiting an application without set the captcha
        Given I am on Spontaneous Application Page
        When  I submit a default application without set the captcha
        Then  I verify the toast message is "Select the Captcha box to continue"
        And   I verify that email field is still filled
