from selene import browser, be, have


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_should_find_nothing():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asddgghfhs').press_enter()
    browser.element("//p[@role='heading']").should(have.text('По запросу asddgghfhs ничего не найдено'))
    browser.element("//p[contains(text(),'Рекомендации:')]").should(be.visible)

