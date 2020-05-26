# Created by Volodymyr Burmitskyi at 2019-06-25
Feature: Home page

  Scenario: Verify the Home page can be opened
    Given User is on the Home page
    When Header - Click Pickup & delivery header tab
    When Header - Click Walmart.com header tab
    When Header - Click on Hamburger menu header tab
    When Header - Click on Home page
    When Header - Click on dropdown toggle
    And Header - Click on Baby from dropdown menu
    When Header - Click on search field
    And Type in "Liza"
    When Header - Click on Account header tab
    When Header - Click on Reorder header tab
    When Header - Click on Cart icon
    When Header - Click on Cart tooltip


