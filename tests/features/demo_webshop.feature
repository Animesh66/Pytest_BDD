@sanity
Feature: Test Demo Web Shop

    Examples:
    |email               |password  |
    |admin@yourstore.com |admin     |
    |test@email.com      |Welcome@1 |

    Background:
      Given user opens the Demo Web Shop url
      When user enter the <email> and <password>
      And click on the LOG IN button
    @login-test
    Scenario Outline: Test Login functionality of Demo webshop
      Then verify the page title is matching <home_page_title>

      Examples:
      |home_page_title                        |
      |Dashboard / nopCommerce administration |
      |Dashboard / nopCommerce administration |
    @verify-product
    Scenario Outline: Verify product review page
      Given user click on Catalog menu
      When user click on Product Review submenu
      Then user navigated to <product_review_page> title

      Examples:
      | product_review_page                         |
      | Product reviews / nopCommerce administration|
      | Product reviews / nopCommerce administration|


