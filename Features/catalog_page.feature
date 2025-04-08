Feature: Catalog Page
  As a user who is not logged in,
  I want to verify that the JPet Store Catalog Page displays the correct and visible elements
  So that I can ensure the page is functioning properly and the UI is as expected.

Background:
  Given user is on the catalog page

Scenario: Verify Catalog Page title
  Then user should see the Catalog page title as "JPetStore Demo"

Scenario: Verify visibility of key elements on the Catalog Page
  Then user should see the following elements in the Header:
    | JPetStore logo button |
    | Cart icon button       |
    | Sign In link button    |
    | Help link button       |
    | Search textbox         |
    | Search button          |

  Then user should see the following image buttons in the QuickLinks:
    | Fish image link button      |
    | Dogs image link button      |
    | Reptiles image link button  |
    | Cats image link button      |
    | Birds image link button     |

  Then user should see the following elements in the SidebarContent:
    | Fish icon button   | Fish subtext   |
    | Dogs icon button   | Dogs subtext   |
    | Reptiles icon button | Reptiles subtext |
    | Cats icon button   | Cats subtext   |
    | Birds icon button  | Birds subtext  |

#  Then user should see the following image buttons in the MainImageContent:
#    | Fish image button   |
#    | Dogs image button    |
#    | Reptiles image button|
#    | Cats image button    |
#    | Birds image button   |

#  Then user should see the following elements in the Separator:
#    | CTA message         |
#    | CTA link button     |

#  Then user should see the following elements in the Footer:
#    | Hosted by text      |
#    | Hosted by link button|
#    | Powered by text     |
#    | Powered by link button|

#Scenario: Verify user redirection to the Catalog Page
#  When user clicks on JPetStore logo button
#  Then user should be redirected to the Catalog Page with URL "https://petstore.octoperf.com/actions/Catalog.action"
#Scenario: Verify user redirection to the Cart Page
#  When user clicks on Cart icon button
#  Then user should be redirected to the Cart Page with URL "https://petstore.octoperf.com/actions/Cart.action?viewCart="
#Scenario: Verify user redirection to the Sign In Page
#  When user clicks on Sign In link button
#  Then user should be redirected to the Sign In Page with URL "https://petstore.octoperf.com/actions/Account.action?signonForm="
#Scenario: Verify user redirection to the Help Page
#  When user clicks on Help link button
#  Then user should be redirected to the Help Page with URL "https://petstore.octoperf.com/help.html"
#Scenario: Verify user redirection to Fish category from QuickLinks
#  When user clicks on Fish image button in the QuickLinks
#  Then user should be redirected to the Fish Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=FISH"
#Scenario: Verify user redirection to Dogs category from QuickLinks
#  When user clicks on Dogs image button in the QuickLinks
#  Then user should be redirected to the Dogs Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOGS"
#Scenario: Verify user redirection to Reptiles category from QuickLinks
#  When user clicks on Reptiles image button in the QuickLinks
#  Then user should be redirected to the Reptiles Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=REPTILES"
#Scenario: Verify user redirection to Cats category from QuickLinks
#  When user clicks on Cats image button in the QuickLinks
#  Then user should be redirected to the Cats Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=CATS"
#Scenario: Verify user redirection to Birds category from QuickLinks
#  When user clicks on Birds image button in the QuickLinks
#  Then user should be redirected to the Birds Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=BIRDS"
#Scenario: Verify user redirection to Fish category from SidebarContent
#  When user clicks on Fish icon button in the SidebarContent
#  Then user should be redirected to the Fish Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=FISH"
#Scenario: Verify user redirection to Dogs category from SidebarContent
#  When user clicks on Dogs icon button in the SidebarContent
#  Then user should be redirected to the Dogs Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOGS"
#Scenario: Verify user redirection to Reptiles category from SidebarContent
#  When user clicks on Reptiles icon button in the SidebarContent
#  Then user should be redirected to the Reptiles Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=REPTILES"
#Scenario: Verify user redirection to Cats category from SidebarContent
#  When user clicks on Cats icon button in the SidebarContent
#  Then user should be redirected to the Cats Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=CATS"
#Scenario: Verify user redirection to Birds category from SidebarContent
#  When user clicks on Birds icon button in the SidebarContent
#  Then user should be redirected to the Birds Category Page with URL "https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=BIRDS"
#Scenario: Verify user redirection to the OctoPerf page from Footer
#  When user clicks on OctoPerf CTA link button in the Footer
#  Then user should be redirected to the Hosted By Page with URL "https://www.octoperf.com"
#Scenario: Verify user redirection to the Hosted By page from Footer
#  When user clicks on Hosted by link button in the Footer
#  Then user should be redirected to the Hosted By Page with URL "https://www.octoperf.com" in a new tab
#Scenario: Verify user redirection to the Powered By page from Footer
#  When user clicks on Powered by link button in the Footer
#  Then user should be redirected to the Powered By Page with URL "https://www.mybatis.org" in a new tab