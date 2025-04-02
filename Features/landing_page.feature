Feature: Landing Page
  As a user,
  I want to verify that the JPet Store Landing Page displays the correct elements
  So that I can ensure the page is properly loaded.
Background:
  Given user is on the landing page

  Scenario: Verify elements in the Landing Page
    Then user should see the page title as "JPetStore Demo"
    Then user should see the header text
    Then user should see the link button
    Then user should see the copyright text
  Scenario: Verify user redirection to the Catalog  Page
    When user clicks on link button
    Then user should be redirected to the Catalog Page with URL "https://petstore.octoperf.com/actions/Catalog.action"