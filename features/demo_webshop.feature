Feature: Test Demo webshop
  Scenario Outline: Test Login functionality of Demo webshop
    Given user opens the Demo web shop url
    When user enter the "<email>" and "<password>"
    And click on the LOG IN button
    Then user is able to sucessfully landed on Dashboard page
    And verify the page title is matching "<home_page_title>"
    Examples:
      | email               | password  | home_page_title                        |
      | admin@yourstore.com | admin     | Dashboard / nopCommerce administration |
      | test@email.com      | Welcome@1 | Dashboard / nopCommerce administration |