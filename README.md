# practice_playwright
Playwright 연습용 저장소

이 저장소는 Playwright를 사용한 기본적인 웹 자동화 연습을 위해 만들어졌습니다.

## 환경 설정

- Python 3.12.0
- 필요한 패키지는 `requirements.txt`에 명시되어 있습니다.

패키지 설치:

```
pip install -r requirements.txt
```

Playwright 브라우저 설치:

```
playwright install
```

## 기본 사용법

이 저장소는 https://naver.com 을 기준으로 다음과 같은 기본적인 Playwright 동작을 포함합니다:

1. 웹페이지 실행
2. 'Naver' 텍스트 확인
3. 특정 버튼 클릭
4. 계정 정보 입력
5. 페이지 스크롤

### 샘플 코드

`naver_test.py` 파일에 다음과 같은 샘플 코드가 포함되어 있습니다:

```python
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 1. 웹페이지 실행
    page.goto("https://www.naver.com")
    
    # 2. 'Naver' 텍스트 확인
    assert page.inner_text("h1.logo_naver") == "NAVER"
    
    # 3. 특정 버튼 클릭 (예: '메일' 버튼)
    page.click("a.nav_item:has-text('메일')")
    
    # 4. 계정 정보 입력 (로그인 페이지)
    page.fill("#id", "your_username")
    page.fill("#pw", "your_password")
    
    # 5. 페이지 스크롤
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

## 실행 방법

```
python naver_test.py
```

이 스크립트는 Naver 웹사이트를 열고, 로고를 확인하고, '메일' 버튼을 클릭하고, 로그인 페이지에서 계정 정보를 입력한 다음, 페이지를 스크롤합니다.

주의: 실제 계정 정보를 사용할 때는 보안에 주의하세요. 테스트 목적으로만 사용하십시오.

## 추가 예제

### 버튼 클릭
```python
# ID로 버튼 클릭
page.click("#button-id")

# 텍스트로 버튼 클릭
page.click("text=클릭하세요")

# CSS 선택자로 버튼 클릭
page.click("button.submit-button")
```

### 텍스트 입력
```python
# ID로 입력 필드 찾아 텍스트 입력
page.fill("#input-id", "입력할 텍스트")

# 이름 속성으로 입력 필드 찾아 텍스트 입력
page.fill("input[name='username']", "사용자이름")
```

### 텍스트 가져오기
```python
# 요소의 텍스트 가져오기
text = page.inner_text("#element-id")
print(text)

# 입력 필드의 값 가져오기
value = page.input_value("#input-id")
print(value)
```

### 페이지 스크롤
```python
# 페이지 맨 아래로 스크롤
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

# 특정 요소로 스크롤
page.scroll_into_view_if_needed("#element-id")

# 특정 위치로 스크롤
page.evaluate("window.scrollTo(0, 500)")
```

이 예제들을 참고하여 각자의 필요에 맞게 스크립트를 수정하고 실행해볼 수 있습니다. Playwright의 더 자세한 사용법은 [공식 문서](https://playwright.dev/python/docs/intro)를 참조하세요.
