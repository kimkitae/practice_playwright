from playwright.sync_api import sync_playwright, Page, expect
import pytest

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function", autouse=True)
def before_each_test(page: Page):
    page.goto("https://www.naver.com")
    yield page

def test_naver_homepage(page: Page):
    expect(page).to_have_url("https://www.naver.com/")

def test_mail_button(page: Page):
    mail_button = page.locator("span.service_name:text('메일')")
    expect(mail_button).to_be_visible()
    mail_button.click()
    
    expect(page).to_have_url(starting_with="https://nid.naver.com/nidlogin.login", timeout=5000)
    
    logo = page.locator("a.logo h1.blind:text('NAVER')")
    expect(logo).to_be_visible()

def test_login(page: Page):
    login_button = page.locator("a.MyView-module__link_login___HpHMW")
    login_button.click()
    
    page.fill("#id", "your_username")
    page.fill("#pw", "your_password")
    
    submit_button = page.locator("button#log\\.login")
    submit_button.click()
    
    # 로그인 성공 여부를 확인하는 assert 추가 필요

def test_footer_links(page: Page):
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    # 더 구체적인 선택자 사용
    company_link = page.locator("a[href='https://www.navercorp.com/']").first
    recruit_link = page.locator("a[href='https://recruit.navercorp.com/']")
    
    expect(company_link).to_be_visible()
    expect(recruit_link).to_be_visible()
    
    expect(company_link).to_have_text("회사소개")
    expect(recruit_link).to_have_text("인재채용")
