# 매체 호감 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# TV - 영상 / 라디오 - 라디오 / 인쇄 - 인쇄 / 옥외 - 옥외 / SNS / 커뮤니티
data_tv = pd.read_csv('./csv/한국방송광고진흥공사_광고박물관 소장 광고소재(영상광고) 현황_20220311 (1).csv', encoding='cp949', low_memory=False)
# print(data_tv)  # [17852 rows x 12 columns]

# 안쓰는 컬럼들 정리
data_tv_colums = data_tv.columns
# print(data_tv_colums)
# Index(['번호', '제작년도', '제작월', '초수', '대분류', '중분류', '소분류', '광고주', '제품', '제목',
#        '대행사', '제작프로덕션'],
#       dtype='object')
tv = data_tv[['번호', '제작년도','대분류', '중분류', '소분류','제품', '제목']].drop_duplicates()
print(tv)  # [17851 rows x 7 columns]

# 제작년도에 Nan인 것은 3000으로 전처리
for _, item in tv.iterrows():
    if pd.isna(item['제작년도']):
        item['제작년도'] = 3000
        # print(item)

# 제작년도로 정렬
tv = tv[tv['제작년도'] >= 1990]
# print(tv)  # [13620 rows x 7 columns]

# 대분류/중분류/소분류 우리꺼 맞춰서 수정 *** 중요 ***
tv_options = tv.drop_duplicates(subset=['대분류', '중분류', '소분류'])
tv_options = tv_options.sort_values(by=['대분류', '중분류', '소분류'])
# print(tv_options)  # [464 rows x 7 columns]
# for _, item in tv_options.iterrows():
    # print(item['대분류'], ",", item['중분류'], ",", item['소분류'], sep="")
    # print(item['소분류'])

tv['code'] = 0
for idx, item in tv.iterrows():
    if item['대분류'] == "가정용 전기전자" and item['중분류'] == "가사용 전기전자":
        tv.at[idx, 'code'] = 3101
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "가정용 전기전자 기타":
        tv.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기 청정기":
        tv.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "영상기기":
        tv.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "음향기기":
        tv.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "조명 및 전기소품":
        tv.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "주방용 전기전자":
        tv.at[idx, 'code'] = 3203
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류" and item['소분류'] == "주방용 가구":
        tv.at[idx, 'code'] = 3203
        continue
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류":
        tv.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용 인테리어":
        tv.at[idx, 'code'] = 3404
    elif item['대분류'] == "가정용품" and item['중분류'] == "난방기기":
        tv.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용품" and item['중분류'] == "방취 및 방균제":
        tv.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "생활잡화 및 기기":
        tv.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "세제류":
        tv.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "식품 기타":
        tv.at[idx, 'code'] = 2499
    elif item['대분류'] == "가정용품" and item['중분류'] == "악기류":
        tv.at[idx, 'code'] = 6100
    elif item['대분류'] == "가정용품" and item['중분류'] == "주방용품":
        tv.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "취미,레저용품":
        tv.at[idx, 'code'] = 6099
    elif item['대분류'] == "가정용품" and item['중분류'] == "컴퓨터S/W":
        tv.at[idx, 'code'] = 6104
    elif item['대분류'] == "가정용품" and item['중분류'] == "완구류":
        tv.at[idx, 'code'] = 6204
    elif item['대분류'] == "건설, 건재 및 부동산":
        tv.at[idx, 'code'] = 8210
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "관공서 및 단체 기타":
        tv.at[idx, 'code'] = 4202
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "단체":
        tv.at[idx, 'code'] = 6101
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "중앙 및 지방 관공서":
        tv.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육 및 복지후생 기타":
        tv.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육기관":
        tv.at[idx, 'code'] = 4202
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "그룹광고":
        tv.at[idx, 'code'] = 9001
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "기타광고":
        tv.at[idx, 'code'] = 9001
    elif item['대분류'] == "금융, 보험 및 증권":
        tv.at[idx, 'code'] = 8099
    elif item['대분류'] == "기초재" and item['중분류'] == "기초재 기타":
        tv.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "농축수산 기초재":
        tv.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄,석유 및 가스":
        tv.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "개인서비스":
        tv.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "문화 및 공연":
        tv.at[idx, 'code'] = 6210
    elif item['대분류'] == "서비스" and item['중분류'] == "서비스 기타":
        tv.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "스포츠 및 오락시설":
        tv.at[idx, 'code'] = 6001
    elif item['대분류'] == "서비스" and item['중분류'] == "여행":
        tv.at[idx, 'code'] = 5301
    elif item['대분류'] == "서비스" and item['중분류'] == "운송":
        tv.at[idx, 'code'] = 5399
    elif item['대분류'] == "서비스" and item['중분류'] == "음식 및 숙박":
        tv.at[idx, 'code'] = 5103
    elif item['대분류'] == "서비스" and item['중분류'] == "전문서비스":
        tv.at[idx, 'code'] = 8211
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 기타":
        tv.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 부품 및 용품":
        tv.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수입자동차":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승용자동차":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승합차":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "오토바이":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "트럭":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "특수자동차":
        tv.at[idx, 'code'] = 9099
    elif item['대분류'] == "식품" and item['중분류'] == "건강식품":
        tv.at[idx, 'code'] = 2404
    elif item['대분류'] == "식품" and item['중분류'] == "농산품":
        tv.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "대용식품":
        tv.at[idx, 'code'] = 2199
    elif item['대분류'] == "식품" and item['중분류'] == "면류":
        tv.at[idx, 'code'] = 2104
    elif item['대분류'] == "식품" and item['중분류'] == "수산품":
        tv.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "식품 기타":
        tv.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "아이스크림":
        tv.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "유제품":
        tv.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제과":
        tv.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제빵":
        tv.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "조미향신료":
        tv.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "축산품":
        tv.at[idx, 'code'] = 2406
    elif item['대분류'] == "유통" and item['중분류'] == "대형유통":
        tv.at[idx, 'code'] =  4123
    elif item['대분류'] == "유통" and item['중분류'] == "소형, 소매유통":
        tv.at[idx, 'code'] = 4107
    elif item['대분류'] == "유통" and item['중분류'] == "유통 기타":
        tv.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "특수유통":
        tv.at[idx, 'code'] = 4123
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "기호식품":
        tv.at[idx, 'code'] = 2406
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "비알콜음료":
        tv.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "알콜음료":
        tv.at[idx, 'code'] = 2407
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "음료 및 기호식품 기타":
        tv.at[idx, 'code'] = 2499
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "문구류":
        tv.at[idx, 'code'] = 6114
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "사무기기":
        tv.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "시계":
        tv.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "이광학기기":
        tv.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "정밀기기 및 사무기기 기타":
        tv.at[idx, 'code'] = 3101
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "감기약":
        tv.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "근육 및 신경통제":
        tv.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "농축산약제":
        tv.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "대사성의약":
        tv.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "두피 및 피부용제":
        tv.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신,구충 및 살충제":
        tv.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신, 구충 및 살충제":
        tv.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "생리피임 및 치질용약":
        tv.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "소화위장약":
        tv.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "순환기관용제":
        tv.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료기기":
        tv.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료용품":
        tv.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "이비인후, 치과 및 안과용제":
        tv.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "제약 및 의료 기타":
        tv.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "진통제 및 안정제":
        tv.at[idx, 'code'] = 7005
    elif item['대분류'] == "출판" and item['중분류'] == "서적":
        tv.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "신문":
        tv.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "여가용 S/W":
        tv.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "유아용 교재":
        tv.at[idx, 'code'] = 8114
    elif item['대분류'] == "출판" and item['중분류'] == "일반용 교재":
        tv.at[idx, 'code'] = 8111
    elif item['대분류'] == "출판" and item['중분류'] == "잡지":
        tv.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "중고생용 교재":
        tv.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "초등학생용 교재":
        tv.at[idx, 'code'] = 8199
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "방송":
        tv.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터":
        tv.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 및 정보통신 기타":
        tv.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 출력장치":
        tv.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 카드류":
        tv.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터S/W":
        tv.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신기기":
        tv.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신망":
        tv.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보 서비스":
        tv.at[idx, 'code'] = 6102
    elif item['대분류'] == "패션" and item['중분류'] == "가방류":
        tv.at[idx, 'code'] = 1205
    elif item['대분류'] == "패션" and item['중분류'] == "내의류":
        tv.at[idx, 'code'] = 1008
    elif item['대분류'] == "패션" and item['중분류'] == "스포츠 전문복":
        tv.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "신발류":
        tv.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "원사 및 원단":
        tv.at[idx, 'code'] = 1199
    elif item['대분류'] == "패션" and item['중분류'] == "유아 및 아동복":
        tv.at[idx, 'code'] = 1007
    elif item['대분류'] == "패션" and item['중분류'] == "정장의류":
        tv.at[idx, 'code'] = 1001
    elif item['대분류'] == "패션" and item['중분류'] == "캐주얼의류":
        tv.at[idx, 'code'] = 1004
    elif item['대분류'] == "패션" and item['중분류'] == "패션 신변용품":
        tv.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션기타":
        tv.at[idx, 'code'] = 1299
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정 및 보건용 제지":
        tv.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "구강용품":
        tv.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "남성 화장품":
        tv.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모발 및 목욕용제":
        tv.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "방향 화장품":
        tv.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "세제류":
        tv.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 기초화장품":
        tv.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 색조화장품":
        tv.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 썬탠류":
        tv.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유,아동용 화장 및 세제":
        tv.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장도구":
        tv.at[idx, 'code'] = 7108
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장품 및 보건용품 기타":
        tv.at[idx, 'code'] = 7199
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틴":
        tv.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학공업 기타":
        tv.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학제품":
        tv.at[idx, 'code'] = 9001
    else:
        print(item)


# 광고 사용률 - 그룹화


