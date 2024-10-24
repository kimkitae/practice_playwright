from playwright.sync_api import sync_playwright, expect

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # 각 테스트 전에 네이버 홈페이지로 이동
            page.goto("https://www.naver.com")

            # 테스트 1: 네이버 홈페이지 URL 확인
            test_naver_homepage(page)

            # 테스트 2: 메일 버튼 테스트
            test_mail_button(page)

            # 테스트 3: 로그인 테스트 (주의: 실제 로그인 정보 필요)
            # test_login(page)

            # 테스트 4: 푸터 링크 테스트
            test_footer_links(page)

            print("모든 테스트가 성공적으로 완료되었습니다.")
        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")
        finally:
            browser.close()

def test_naver_homepage(page):
    assert page.url == "https://www.naver.com/", "네이버 홈페이지 URL이 일치하지 않습니다."

def test_mail_button(page):
    mail_button = page.locator("span.service_name:text('메일')")
    assert mail_button.is_visible(), "메일 버튼이 보이지 않습니다."
    mail_button.click()
    
    assert page.url.startswith("https://nid.naver.com/nidlogin.login"), "메일 로그인 페이지로 이동하지 않았습니다."
    
    logo = page.locator("a.logo h1.blind:text('NAVER')")
    assert logo.is_visible(), "네이버 로고가 보이지 않습니다."

def test_login(page):
    login_button = page.locator("a.MyView-module__link_login___HpHMW")
    login_button.click()
    
    page.fill("#id", "your_username")
    page.fill("#pw", "your_password")
    
    submit_button = page.locator("button#log\\.login")
    submit_button.click()
    
    # 로그인 성공 여부를 확인하는 assert 추가 필요
    # 예: assert page.locator("로그인 성공 요소").is_visible(), "로그인에 실패했습니다."

def test_footer_links(page):
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    company_link = page.locator("a[href='https://www.navercorp.com/']").first
    recruit_link = page.locator("a[href='https://recruit.navercorp.com/']")
    
    assert company_link.is_visible(), "회사소개 링크가 보이지 않습니다."
    assert recruit_link.is_visible(), "인재채용 링크가 보이지 않습니다."
    
    assert company_link.inner_text() == "회사소개", "회사소개 링크 텍스트가 일치하지 않습니다."
    assert recruit_link.inner_text() == "인재채용", "인재채용 링크 텍스트가 일치하지 않습니다."

if __name__ == "__main__":
    run_tests()