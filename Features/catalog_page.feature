Feature: Catalog Page
  As a user who is not logged in,
  I want to verify that the JPet Store Catalog Page displays the correct elements
  So that I can ensure the page is functioning properly and the UI is as expected.

Background:
  Given user is on the catalog page

Scenario: Verify key title, subtexts, and messages in the Catalog Page
  Then user should see the Catalog page title as "JPetStore Demo"
  Then user should see the correct subtexts in the SidebarContent:
    | Saltwater, Freshwater   |
    | Various Breeds   |
    | Various Breeds, Exotic Varieties |
    | Lizards, Turtles, Snakes   |
    | Exotic Varieties  |
  Then user should see the correct CTA message in the Separator:
    | Elevate you load-testing with |
  Then user should see the correct texts in the Footer:
    | Hosted by |
    | Powered by  |

Scenario: Verify user redirection to the Catalog Page
  When user clicks the JPetStore logo button
  Then page should refresh and display the Catalog Page with URL "https://petstore.octoperf.com/actions/Catalog.action"
Scenario: Verify user redirection to the Cart Page
  When user clicks the Cart icon button
  Then user should be redirected to the Cart Page with URL "https://petstore.octoperf.com/actions/Cart.action?viewCart="
Scenario: Verify user redirection to the Sign In Page
  When user clicks the Sign In link button
  Then user should be redirected to the Sign In Page with URL "https://petstore.octoperf.com/actions/Account.action?signonForm="
Scenario: Verify user redirection to the Help Page
  When user clicks the Help link button
  Then user should be redirected to the Help Page with URL "https://petstore.octoperf.com/help.html"
Scenario: Verify user redirection to Fish category from QuickLinks
  When user clicks the Fish image button in the QuickLinks
  Then user should be redirected to the Fish Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=FISH"
Scenario: Verify user redirection to Dogs category from QuickLinks
  When user clicks the Dogs image button in the QuickLinks
  Then user should be redirected to the Dogs Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOGS"
Scenario: Verify user redirection to Reptiles category from QuickLinks
  When user clicks the Reptiles image button in the QuickLinks
  Then user should be redirected to the Reptiles Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=REPTILES"
Scenario: Verify user redirection to Cats category from QuickLinks
  When user clicks the Cats image button in the QuickLinks
  Then user should be redirected to the Cats Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=CATS"
Scenario: Verify user redirection to Birds category from QuickLinks
  When user clicks the Birds image button in the QuickLinks
  Then user should be redirected to the Birds Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=BIRDS"
Scenario: Verify user redirection to Fish category from SidebarContent
  When user clicks the Fish icon button in the SidebarContent
  Then Fish Category Page should be displayed with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=FISH"
Scenario: Verify user redirection to Dogs category from SidebarContent
  When user clicks the Dogs icon button in the SidebarContent
  Then Dogs Category Page should be displayed with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOGS"
Scenario: Verify user redirection to Reptiles category from SidebarContent
  When user clicks the Reptiles icon button in the SidebarContent
  Then Reptiles Category Page should be displayed with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=REPTILES"
Scenario: Verify user redirection to Cats category from SidebarContent
  When user clicks the Cats icon button in the SidebarContent
  Then Cats Category Page should be displayed with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=CATS"
Scenario: Verify user redirection to Birds category from SidebarContent
  When user clicks the Birds icon button in the SidebarContent
  Then Birds Category Page should be displayed with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=BIRDS"
#Scenario: Verify user redirection to the OctoPerf page from Footer
#  When user clicks on OctoPerf CTA link button in the Footer
#  Then user should be redirected to the Hosted By Page with URL "https://www.octoperf.com"
#Scenario: Verify user redirection to the Hosted By page from Footer
#  When user clicks on Hosted by link button in the Footer
#  Then user should be redirected to the Hosted By Page with URL "https://www.octoperf.com" in a new tab
#Scenario: Verify user redirection to the Powered By page from Footer
#  When user clicks on Powered by link button in the Footer
#  Then user should be redirected to the Powered By Page with URL "https://www.mybatis.org" in a new tab