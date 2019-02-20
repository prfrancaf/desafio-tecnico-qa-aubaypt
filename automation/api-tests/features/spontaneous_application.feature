Feature: Spontaneous Application

    Scenario: Submiting an application successfully
        When I submit a default application
        Then I verify the application response is "200"
