import pybithumb
import time

con_key = "d1660c761cb951aad162f1726bfec20e"        # API 신청 페이지에서 발급받은 본인의 Connect Key를 입력합니다.
sec_key = "b4b6cb16cc70df1b31030d8a8a3521d9"        # API 신청 페이지에서 발급받은 본인의 Secret Key를 입력합니다.

# bithumb = pybithumb.Bithumb(con_key, sec_key)       # Bithumb 클래스 객체를 생성하는데 초기화자(__init__)로 두 키값을 전달합니다.

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers() :             # public API인 get_tickers() 함수는 모든 가상화폐의 티커를 리스트로 반환합니다. 반복문의 ticker 변수에는 가상화폐의 티커가 차례로 바인딩됩니다.
    balance = bithumb.get_balance(ticker)           # ticker에 바인딩된 가상화폐를 private API인 get_balance() 메서드로 조회합니다. 결과 값은 balance 변수에 바인딩합니다.
    print(ticker, ":", balance)                     # balance 변수에 저장된 잔고를 화면에 출력합니다.
    time.sleep(0.1)