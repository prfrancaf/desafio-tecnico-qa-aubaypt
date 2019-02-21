Feature: Spontaneous Application

    Scenario: Submiting an application without set the captcha
        Given I am on Spontaneous Application Page
        When  I submit a default application without set the captcha
        Then  I verify that email field is still filled
