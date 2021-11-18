Feature: Test Demo Web Shop
  Scenario Outline: Test Login functionality of Demo webshop
    Given user opens the Demo Web Shop url
    When user enter the <email> and <password>
    And click on the LOG IN button
    Then verify the page title is matching <home_page_title>
    Examples:
      |email               |password  |home_page_title                        |
      |admin@yourstore.com |admin     |Dashboard / nopCommerce administration |
      |test@email.com      |Welcome@1 |Dashboard / nopCommerce administration |