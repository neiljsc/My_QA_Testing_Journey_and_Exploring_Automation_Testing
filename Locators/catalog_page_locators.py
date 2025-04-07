from selenium.webdriver.common.by import By

class CatalogPageLocators:

    """ Catalog Page Data """
    catalog_page_title = "JPetStore Demo"

    catalog_page_signin_text = "Sign In"
    catalog_page_help_text = "?"
    catalog_page_search_text = "Search"

    catalog_page_fish_subtext = " Saltwater, Freshwater "
    catalog_page_dogs_subtext = " Various Breeds "
    catalog_page_cats_subtext = " Various Breeds, Exotic Varieties "
    catalog_page_reptiles_subtext = " Lizards, Turtles, Snakes "
    catalog_page_birds_subtext = " Exotic Varieties "

    """ Catalog Page Locators """
    catalog_page_title_locator = (By.TAG_NAME, "title")

    catalog_page_header_logo_button_locator = (By.ID, "LogoContent")
    catalog_page_header_cart_icon_button_locator = (By.NAME, "img_cart")
    catalog_page_header_sign_in_link_button_locator = (By.LINK_TEXT, "Sign In")
    catalog_page_header_help_link_button_locator = (By.LINK_TEXT, "?")

    catalog_page_header_search_textbox_locator = (By.NAME, "keyword")
    catalog_page_header_search_button_locator = (By.NAME, "searchProducts")

    catalog_page_fish_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=FISH']")
    catalog_page_dogs_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=DOGS']")
    catalog_page_reptiles_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=REPTILES']")
    catalog_page_cats_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=CATS']")
    catalog_page_birds_image_link_button_locator = (By.CSS_SELECTOR, "a[href='/actions/Catalog.action?viewCategory=&categoryId=BIRDS']")

    catalog_page_fish_icon_button_locator = \
        (By.CSS_SELECTOR, "a[href='/actions/Catalog.action;jsessionid=9CE551515549DE3A3E292AED6C38F040?viewCategory=&categoryId=FISH']")
    catalog_page_dogs_icon_button_locator = \
        (By.CSS_SELECTOR,"a[href='/actions/Catalog.action;jsessionid=9CE551515549DE3A3E292AED6C38F040?viewCategory=&categoryId=DOGS']")
    catalog_page_cats_icon_button_locator = \
        (By.CSS_SELECTOR,"a[href='/actions/Catalog.action;jsessionid=9CE551515549DE3A3E292AED6C38F040?viewCategory=&categoryId=CATS']")
    catalog_page_reptiles_icon_button_locator = \
        (By.CSS_SELECTOR,"a[href='/actions/Catalog.action;jsessionid=9CE551515549DE3A3E292AED6C38F040?viewCategory=&categoryId=REPTILES']")
    catalog_page_birds_icon_button_locator = \
        (By.CSS_SELECTOR,"a[href='/actions/Catalog.action;jsessionid=9CE551515549DE3A3E292AED6C38F040?viewCategory=&categoryId=BIRDS']")