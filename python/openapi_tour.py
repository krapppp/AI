import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd


ServiceKey = "본인 서비스 키 사용"

# [CODE 1] - HTTP 요청을 보내고 응답을 반환하는 유틸리티 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f"[{datetime.datetime.now()}] Url Request Success: {url}")
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Error for URL: {url}")
        print(e)
        return None


# [CODE 2] - 특정 월의 관광 통계 데이터를 API에서 가져와 JSON으로 파싱하여 반환하는 함수
def getTourismStatsItem(yyyymm, national_code, ed_cd):
    # service_url 한 줄로
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters = "?_type=json&serviceKey=" + ServiceKey
    parameters += "&YM=" + str(yyyymm)  # YM은 문자열이어야 함
    parameters += "&NAT_CD=" + str(national_code)  # NAT_CD도 문자열이어야 함
    parameters += "&ED_CD=" + str(ed_cd)  # ED_CD도 문자열이어야 함

    url = service_url + parameters

    retData = getRequestUrl(url)  # [CODE 1] 호출

    if retData is None:
        return None
    else:
        return json.loads(retData)  # JSON 문자열을 파이썬 딕셔너리로 변환하여 반환


# [CODE 3] - 지정된 기간 동안의 관광 통계 데이터를 수집하는 함수
def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []  # JSON 데이터를 저장할 리스트
    result = []  # Pandas DataFrame 생성을 위한 리스트
    last_valid_natName = "Unknown"  # 마지막으로 성공적으로 가져온 국가명
    last_valid_ed = "Unknown"  # 마지막으로 성공적으로 가져온 구분 코드
    last_data_month_in_loop = ""  # 루프 내에서 마지막으로 데이터가 있었던 연월 (yyyymm)

    for year in range(nStartYear, nEndYear + 1):
        for month in range(1, 13):
            yyyymm = f"{year}{month:0>2}"  # f-string으로 yyyymm 형식화

            # API 호출 결과 가져오기
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)  # [CODE 2] 호출

            if jsonData is None:  # API 호출 자체 실패 (네트워크 등)
                print(f"[{datetime.datetime.now()}] API 호출 실패: {yyyymm}. 다음 월로 넘어갑니다.")
                continue  # 다음 월로 넘어감

            # API 응답 헤더 확인
            header = jsonData.get('response', {}).get('header', {})
            result_msg = header.get('resultMsg', 'ERROR')
            if result_msg != 'OK':
                print(f"[{datetime.datetime.now()}] API 응답 메시지 오류: {result_msg} for {yyyymm}. 다음 월로 넘어갑니다.")
                continue  # 오류 메시지가 'OK'가 아니면 해당 월 건너

            # 'items' 키가 있는지, 그리고 비어있지 않은지 확인
            body = jsonData.get('response', {}).get('body', {})
            items_body = body.get('items', '')  # 'items'가 없을 경우 빈 문자열 반환

            if items_body == '' or not items_body:  # 'items'가 빈 문자열이거나 None, 또는 빈 딕셔너리/리스트일 경우
                # 데이터가 없는 경우
                print(f"[{datetime.datetime.now()}] 데이터 없음: {year}년 {month}월 통계 데이터를 찾을 수 없습니다.")
                # 더 이상 데이터가 없는 것으로 판단하고 현재 연도의 월별 루프를 중단
                # (API가 특정 시점 이후 데이터를 제공하지 않는 경우를 대비)
                break  # 월별 루프만 종료 (다음 연도로 넘어감)

            # 데이터가 있는 경우 처리
            try:
                # 'item'이 리스트가 아닌 단일 딕셔너리로 올 수 있으므로 안전하게 처리
                item_data = items_body.get('item')
                if item_data is None:  # 'item' 키 자체가 없는 경우
                    print(f"[{datetime.datetime.now()}] 'item' 키가 없습니다: {yyyymm}")
                    continue
                if isinstance(item_data, list):  # 만약 'item'이 리스트로 온다면 첫 번째 항목을 사용
                    item = item_data[0]
                else:
                    item = item_data

                # 올바른 따옴표 사용 및 공백 제거
                natName = item.get('natKorNm', 'N/A').replace(' ', '')
                num = item.get('num', 0)
                ed = item.get('ed', 'N/A')

                print(f'[ {natName}_{yyyymm} : {num} ]')
                print('-----------------------------------------------------')

                # 결과 리스트에 추가 (ed_cd도 포함)
                jsonResult.append({'nat_name': natName, 'nat_cd': nat_cd,
                                   'yyyymm': yyyymm, 'visit_cnt': num, 'ed_cd': ed})
                result.append([natName, nat_cd, yyyymm, num, ed])  # ed_cd도 추가

                last_valid_natName = natName  # 마지막으로 유효한 국가명 업데이트
                last_valid_ed = ed  # 마지막으로 유효한 구분 코드 업데이트
                last_data_month_in_loop = yyyymm  # 마지막으로 데이터가 있었던 연월 업데이트

            except KeyError as ke:
                print(f"[{datetime.datetime.now()}] JSON 파싱 오류 (필수 키 없음): {ke} for {yyyymm}")
                print(f"디버깅용 JSON 구조: {json.dumps(jsonData, indent=4, ensure_ascii=False)}")
                continue  # 오류 발생 시 다음 월로 넘어감
            except Exception as ex:
                print(f"[{datetime.datetime.now()}] 데이터 처리 중 알 수 없는 오류 발생: {ex} for {yyyymm}")
                continue
        # 한 해의 월별 루프가 끝났을 때 텀을 줌 (API 호출 빈도 조절)
        time.sleep(0.5)  # 0.5초 대기

    # 루프 종료 후 최종 반환 값
    # natName, ed는 루프 내에서 마지막으로 성공한 값
    # dataEND는 마지막으로 데이터가 있었던 월. 데이터가 없었다면 nEndYear의 마지막 월.
    final_data_end_for_filename = last_data_month_in_loop if last_data_month_in_loop else f"{nEndYear}12"

    # natName, ed도 마지막으로 성공한 값 또는 기본값으로 반환
    return (jsonResult, result, last_valid_natName, last_valid_ed, final_data_end_for_filename)


# [CODE 0] - 메인 실행 함수
def main():
    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")

    nat_cd = input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) : ')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    ed_cd = "E"  # E : 방한외래관광객, D : 해외 출국

    jsonResult, result, natName_final, ed_final, dataEND_final = \
        getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)  # [CODE 3]

    # 파일저장 1: json 파일
    json_filename = f'./{natName_final}_{ed_final}_{nStartYear}_{dataEND_final}.json'
    with open(json_filename, 'w', encoding='utf8') as outfile:
        # json.dumps 호출 시 줄바꿈 제거
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
    print(f"JSON 파일 '{json_filename}' SAVED")

    # 파일저장 2: csv 파일
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수", "방문객구분"]  # 'ed_cd' 컬럼 추가
    result_df = pd.DataFrame(result, columns=columns)

    csv_filename = f'./csv/{natName_final}_{ed_final}_{nStartYear}_{dataEND_final}.csv'
    result_df.to_csv(csv_filename, index=False, encoding='cp949')  # Excel 호환을 위해 cp949 인코딩 사용
    print(f"CSV 파일 '{csv_filename}' SAVED")


if __name__ == '__main__':
    main()