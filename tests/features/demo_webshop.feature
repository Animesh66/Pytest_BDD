Feature: Test Demo Web Shop


  Background:
    Given user opens the Demo Web Shop url
    When user enter the <email> and <password>
    And click on the LOG IN button

  Scenario Outline: Test Login functionality of Demo webshop
    Then verify the page title is matching <home_page_title>

    Examples:
      |email               |password  |home_page_title                        |
      |admin@yourstore.com |admin     |Dashboard / nopCommerce administration |
      |test@email.com      |Welcome@1 |Dashboard / nopCommerce administration |

  Scenario Outline: Verify product review page
    Given user click on Catalog menu
    When user click on Product Review submenu
    Then user navigated to product review page with page title
    Examples:
      |email               |password  |home_page_title                        |
      |admin@yourstore.com |admin     |Dashboard / nopCommerce administration |
      |test@email.com      |Welcome@1 |Dashboard / nopCommerce administration |
