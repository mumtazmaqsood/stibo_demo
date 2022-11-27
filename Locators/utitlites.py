
#storing window ids
window_store = []


def switch_window(driver, i):
    '''
    Switch to other browser window
    :param i: int (0, 1)
    :return: window id
    '''
    return driver.switch_to.window(window_store[i])


def verify_text(driver, selector, locator):
    '''
    This function getting selector & locator & return attritubes' text
    :param selector: By.XPATH, By.CSS_SELECTOR, etc
    :param locator: xpath,id,css_selector etc
    :return: Book a free product demo today, field is empty etc
    '''
    get_text = driver.find_element(selector, locator).text
    return get_text


def scroll_window(driver, flag):
    return driver.execute_script("argument[0].scrollIntoView();", flag)