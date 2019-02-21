Feature: Spontaneous Application

    Scenario: Submiting an application successfully
        When I submit a default application
        Then I verify the application response is "200"

    Scenario: Submiting an application withou the name field
        When I submit a application without a name
        Then I verify the application response is "400"
    