from selenium.webdriver.common.by import By

class CatalogPageLocators:
    """ Catalog Page Locators """
    #WebTitle
    catalog_page_title = "JPetStore Demo"
    catalog_page_title_locator = (By.TAG_NAME, "title")
    #SideBarContent
    SIDEBAR_CONTENT = (By.ID, "SidebarContent")
    #SeparatorCTA
    SEPARATOR_CTA_MESSAGE = (By.ID, "CTA")
    #Footer
    FOOTER_TEXTS = (By.ID, "PoweredBy")

    #Header
    catalog_page_header_logo_button_locator = (By.ID, "LogoContent")
    catalog_page_header_cart_icon_button_locator = (By.NAME, "img_cart")
    catalog_page_header_sign_in_link_button_locator = (By.LINK_TEXT, "Sign In")
    catalog_page_header_help_link_button_locator = (By.LINK_TEXT, "?")
    catalog_page_header_search_textbox_locator = (By.NAME, "keyword")
    catalog_page_header_search_button_locator = (By.NAME, "searchProducts")

    #Quicklinks
    catalog_page_fish_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=FISH']")
    catalog_page_dogs_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=DOGS']")
    catalog_page_reptiles_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=REPTILES']")
    catalog_page_cats_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=CATS']")
    catalog_page_birds_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=BIRDS']")

    #SideBarContent Images
    catalog_page_fish_icon_button_locator = (
        By.CSS_SELECTOR, "a[href*='Catalog.action?viewCategory=&categoryId=FISH'] img[src='../images/fish_icon.gif']")
    catalog_page_dogs_icon_button_locator = (
        By.CSS_SELECTOR, "a[href*='Catalog.action?viewCategory=&categoryId=DOGS'] img[src='../images/dogs_icon.gif']")
    catalog_page_cats_icon_button_locator = (
        By.CSS_SELECTOR, "a[href*='Catalog.action?viewCategory=&categoryId=CATS'] img[src='../images/cats_icon.gif']")
    catalog_page_reptiles_icon_button_locator = (
        By.CSS_SELECTOR, "a[href*='Catalog.action?viewCategory=&categoryId=REPTILES'] img[src='../images/reptiles_icon.gif']")
    catalog_page_birds_icon_button_locator = (
        By.CSS_SELECTOR, "a[href*='Catalog.action?viewCategory=&categoryId=BIRDS'] img[src='../images/birds_icon.gif']")