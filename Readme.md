![](readme-assets/cover_image.png)

# 빅데이터 기반의 <br>고객 맞춤형 광고 매체 및 컨텐츠 추천 서비스

<img src="readme-assets/logo_1.png" width="300" />

### 프로젝트 개발 기간

`2023.08.21` ~ `2023.10.06` (7주)

### 시연 영상

> https://youtu.be/UOcts68R_CU

<br>

### 목차

- [기술 스택](#-기술-스택)
- [서비스 소개](#-서비스-소개)
    + [사용 데이터](#사용-데이터)
- [데모](#-데모)
- [기능 소개](#-기능-소개)
- [시연 시나리오 & 영상](#-시연-시나리오--영상)
  * [메인 페이지](#메인-페이지)
  * [회원가입, 로그인](#회원가입-로그인)
  * [매체 추천](#매체-추천)
  * [키워드 추천](#키워드-추천)
  * [컨텐츠 추천](#컨텐츠-추천)
  * [마이페이지](#마이페이지)
- [산출물](#-산출물)
    + [1. Figma](#1-figma)
    + [2. ERD](#2-erd)
    + [3. API 명세서](#3-api-명세서)
    + [4. 기능 명세서](#4-기능-명세서)
    + [5. 시스템 아키텍처](#5-시스템-아키텍처)
    + [6. User Flow](#6-user-flow)
    + [7. Git Flow 브랜치 전략](#7-git-flow-브랜치-전략)
    + [7. Jira](#7-jira)
    + [8. WBS](#8-wbs)
    + [9. 프로젝트 구조](#9-프로젝트-구조)
- [팀원 소개](#-팀원-소개)

<br>

# 📌 기술 스택

### Back-End

<div>
  <img src="https://img.shields.io/badge/Java [11.0.15]-007396?style=for-the-badge&logo=openjdk&logoColor=white" />
  <img src="https://img.shields.io/badge/Spring Boot [2.7.15]-6DB33F?style=for-the-badge&logo=Spring Boot&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradle [8.2.1]-02303A?style=for-the-badge&logo=gradle&logoColor=white" />
</div>
<div>
  <img src="https://img.shields.io/badge/Python [3.11.5]-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/fastapi [0.103.1]-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/uvicorn [0.23.2]-499848?style=for-the-badge&logo=gunicorn&logoColor=white">
</div>

### Front-End

<div>
  <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=Redux&logoColor=white">
  <img src="https://img.shields.io/badge/node.js [18.16.1]-339933?style=for-the-badge&logo=Node.js&logoColor=white">
</div>

### Database

<div>
  <img src="https://img.shields.io/badge/mysql[8.0.29]-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
</div>

### VCS

<div>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" />
</div>

### IDE

<div>
  <img src="https://img.shields.io/badge/Visual Studio Code [1.80.1]-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" />
  <img src="https://img.shields.io/badge/IntelliJ IDEA [2023.1.4]-000000?style=for-the-badge&logo=intellijidea&logoColor=white" />
  <img src="https://img.shields.io/badge/pycharm [2023.2.1]-000000?style=for-the-badge&logo=pycharm&logoColor=white" />
</div>

### CI/CD

<div>
  <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <img src="https://img.shields.io/badge/ec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white">
  <img src="https://img.shields.io/badge/Docker [24.0.4]-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white">
</div>

### Environment

<div>
  <img src="https://img.shields.io/badge/jira-0052CC?style=for-the-badge&logo=jira&logoColor=white">
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
  <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">
  <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">
  <img src="https://img.shields.io/badge/Mattermost [5.3.1]-0058CC?style=for-the-badge&logo=mattermost&logoColor=white" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" />
  <img src="https://img.shields.io/badge/termius [8.0.2]-000000?style=for-the-badge&logo=termius&logoColor=white" />
</div>

<br>

# 📌 서비스 소개

### 개요

- 서비스 명: SHERPA
  - 히말라야 산맥에서 등반을 할 때 등산객을 안내하고 보호하는 역할을 하는 사람을 "셰르파"라고 부른다. 셰르파들은 히말라야 지역에서 주로 활동하며 고산 지대에서의 경험과 지식을 가지고 있어 등반을 안전하게 이끌어주는 중요한 역할을 한다. 히말라야 등반은 고도와 악천후와 같은 위험 요소가 존재하기 때문에 셰르파들의 전문적인 도움이 필요하다.
  - 빅데이터를 활용해 기업 홍보, 제품 광고의 목표를 이끌어주는 역할을 한다는 의미
  - 나침반 + 눈꽃송이(셰르파)

### 기획 배경

- 같은 SNS 채널의 가게들과 차별성이 없는 광고로 홍보 효과 없음
  > 사용자 맟춤형으로 광고 전략을 분석하고 내용을 구성하여 제작사와 매칭해주는 서비스 필요

- 광고 진행 상황과 단가 내역을 파악하기 어려움
  > 광고 타겟층, 지역, 매체, 컨텐츠, 가격대를 직접 확인할 수 있는 서비스 필요

### 사용 데이터

- SSAFY 제공 카드사 데이터 (6천5백만 건)
- [광고 박물관 소장 광고 소재 데이터 (3만 건)](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=TOTAL&keyword=한국방송광고진흥공사+소장&operator=AND&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=)
- [광고 호감도 데이터 (4천 건)](https://adstat.kobaco.co.kr/mcr/portal/dataSet/statsInfoPage.do?clsId=&orderState=regDt&pageSize=10&pageIndex=1&datasetNm=호감&datasetId=DS_MST_0000000183)
- [행정안전부_지역별(시도/시군구/읍면동) 연령별 주민등록 인구현황](https://www.bigdata-lifelog.kr/portal/find/dataList?mode=detail&name=lgu20221017080216)
- [AISAC 광고소재명별 광고 정보 데이터](https://www.data.go.kr/data/15105570/fileData.do)
- [광주광역시 시내버스 노선별 승하차 인원정보](https://www.data.go.kr/data/15088456/fileData.do)
- [광주광역시 현수막 게시대 현황 데이터](https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword=광주광역시+현수막)
- [성별/연령별 방송 프로그램 유형별 시청여부, 이용 시간대 데이터](https://www.mediastat.or.kr/kor/tblInfo/TblInfoList.html?vw_cd=MT_ATITLE)
- [성별/연령별 라디오 유형별 시청률, 청취 시간 데이터](https://www.mediastat.or.kr/kor/tblInfo/TblInfoList.html?vw_cd=MT_ATITLE)
- [성별/연령대별 블로그 사용하는 매체 통계 데이터](https://kosis.kr/statHtml/statHtml.do?orgId=405&tblId=DT_405001_I124&conn_path=I2)
- [성별/연령대별 SNS 사용하는 매체 통계 데이터](https://kosis.kr/statHtml/statHtml.do?orgId=405&tblId=DT_405001_I127&conn_path=I2)
- [언론수용자 조사 통계표](https://www.kpf.or.kr/front/mediaStats/mediaStatsDetail.do)
- [업종별 광고비 데이터](https://www.adic.or.kr/stat/main/getStats.do?className=IndustryAdOutlay)
- 네이버 블로그 크롤링 데이터
- 광고 제작사 데이터

<br>

# 📌 데모

### 필수 사항

```bash
Node.js 18.16.1
SpringBoot 2.7.15

```

### 권고 사항

- Chorme Browser

### 설치

```bash
# git clone
git clone https://lab.ssafy.com/s09-bigdata-recom-sub2/S09P22C107.git

```

### Back-End

```bash
# backend 폴더로 이동
cd backend
./gradlew build
cd build/libs
ls -arlth
java -jar adrec-0.0.1-SNAPSHOT.jar

```

### Front-End

```bash
# frontend 폴더로 이동
cd frontend
npm i
npm start

```

<br>

# 📌 기능 소개

### 주요 기능

- 협업 필터링 알고리즘을 이용한 오프라인 매체 추천 기능
- 협업 필터링 알고리즘을 이용한 맞춤형 키워드 추천 기능
- Word2Vec을 이용한 커뮤니티 세부 주제별 추천
- 회원 관리 (회원 정보 관리, 품목 정보 관리, 추천 결과 보관함 관리)
- ChatGPT - 키워드 추천, 시나리오 추천
- Kakao Map - 현수막 게시장소 추천
- react-chartjs-2 - 차트 UX/UI


### 세부 기능

1. 추천 기능
   - 품목별 자주 사용된 광고 매체 추천
   - 커뮤니티 세부 주제별 추천
   - TV/라디오/신문에서 자주 이용하는 채널이나 신문사 분야를 추천
   - AI를 활용한 광고 컨텐츠 생성
2. 분석 기능
   - 품목 선택을 통한 타겟팅 광고의 성별/연령대 분석
   - 성별/연령대가 많이 모여있는 지역을 분석
   - 워드 클라우드 형식으로 광고 키워드 시각화
3. 회원 관리
   - 추천 받은 데이터 관리
   - 고객 정보 관리
4. 부가 기능
   - 광고 매체에 따른 제작사 매칭
   - 좋아요한 키워드와 컨텐츠를 보관

<br>

# 📌 시연 시나리오 & 영상

## 메인 페이지

- 셰르파의 기획의도, 이용 안내 페이지 입니다.

![최종-메인페이지.gif](readme-assets/메인페이지.gif)

## 회원가입, 로그인

- 아이디를 입력하고 중복 확인을 합니다. 중복되지 않은 아이디면 '사용 가능한 아이디입니다.' 라는 메시지가 뜹니다.
- 비밀번호 확인을 위해 입력한 비밀번호를 똑같이 작성합니다.
- 이메일을 입력하고 중복 확인을 합니다. 중복되지 않은 이메일이면 '사용 가능한 이메일입니다.' 라는 메시지가 뜹니다.
- 모든 정보를 작성한 후 회원가입 버튼을 클릭하면 회원가입이 성공하였다는 알림창이 뜨고 로그인 창으로 넘어갑니다.
- 회원가입한 아이디와 비밀번호를 맞게 입력하고 로그인 버튼을 클릭하면 로그인 성공과 함께 메인 페이지로 이동합니다.
- 이메일 또는 비밀번호가 틀렸을 경우 로그인이 실패했다는 알림창이 뜹니다.

![최종-회원가입로그인.gif](./readme-assets/로그인회원가입.gif)

## 매체 추천

- 광고할 물품이나 서비스, 광고 예산, 거주 지역, 온라인/오프라인 광고를 입력합니다.
- 광고 타겟을 추천 받습니다.
- 추천 받은 타겟이 자주 이용하는 광고 매체를 광고 예산, 거주 지역을 감안하여 추천합니다.
- 추천에 적합한 제작사를 매칭해줍니다.
- 원하는 결과를 보관함에 저장할 수 있습니다.

![최종-매체추천.gif](readme-assets/매체추천.gif)

## 키워드 추천

- 광고할 품목을 입력받아 광고 키워드, 트렌드 키워드를 워드클라우드 형태로 추천받습니다.
- 다른 사용자가 좋아요한 키워드를 추천받습니다.
- 원하는 키워드를 보관함에 저장할 수 있습니다.

![최종-키워드추천.gif](readme-assets/키워드추천.gif)

## 컨텐츠 추천

- 광고 매체와 광고 품목, 키워드를 입력 받습니다.
- TV, 라디오의 경우 시나리오를, 그 외의 매체는 광고를 추천받습니다.
- 원하는 컨텐츠를 보관함에 저장할 수 있습니다.

![최종-컨텐츠추천.gif](readme-assets/컨텐츠추천.gif)

## 마이페이지

- 본인의 이메일과 닉네임을 확인할 수 있습니다.
- 회원 정보 수정 버튼을 클릭하면 정보를 수정할 수 있는 모달창이 뜹니다.
- 이메일과 비밀번호를 변경하고 싶은 경우 수정할 수 있습니다.
- 본인이 선택한 품목을 확인하고 수정할 수 있습니다.
- 매체 추천, 키워드 추천 시 보관함에 저장한 결과를 확인할 수 있습니다.
- 보관함에 저장한 결과는 삭제가 가능합니다.

![최종-마이페이지.gif](readme-assets/마이페이지.gif)

<br>

# 📌 산출물

### 1. Figma

![Untitled](readme-assets/Untitled.png)

### 2. ERD

![20231006_023818.png](readme-assets/20231006_023818.png)

### 3. API 명세서

👉 [API 명세서](https://scalloped-beech-b86.notion.site/API-d442b66cb89049ff9c6a5d4a7eb6bc13)

![최종-API명세서.gif](readme-assets/api명세서.gif)

### 4. 기능 명세서

👉 [기능 명세서](https://scalloped-beech-b86.notion.site/45e6121f5aa04c039e9266e019800f70?v=02b32ae1fc584bf5b3cd57dd1d82d49b)

![최종-기능명세서.gif](readme-assets/기능명세서.gif)

### 5. 시스템 아키텍처

![Untitled](readme-assets/Untitled%201.png)

### 6. User Flow

![Untitled](readme-assets/Untitled%202.png)

### 7. Git Flow 브랜치 전략

| Git Graph | Contributor Statistics |
| --- | --- |
| ![git_flow_gif.gif](readme-assets/git_flow_gif.gif) | ![contributor statistics](readme-assets/Contributor_statistics.png) |

- Git branch 컨벤션
  - `[BE/FE/AL]_[feature/release/hotfix]/기능명`
  - `BE_feature/기능명`, `FE_release/기능명`, `FE_hotfix/기능명`
  - `DATA_feature/기능명`, `DATA_release/기능명`, `DATA_hotfix/기능명`
  - feature, release, hotfix 사용
  - AL: 빅데이터 관련
- Git commit 메시지 컨벤션
  - <타입> 리스트
    - 💡 **Feat**: 새로운 기능 추가
    - 🐛 **Fix**: 오류에 대한 문제 해결
    - ⚡ **Patch**: 기능 개선
    - 📝 **Docs**: 문서 작업
    - 🎨 **Design**: CSS 등 사용자 UI 디자인 변경
    - ✏️ **Style**: 간단한 코드 작업 (코드 형식, 세미콜론 추가: 비즈니스 로직 변경 없음)
    - 🔍 **Merge**: develop 머지 충돌시 수정후 커밋
    - 🏷️ **Rename**: 파일 혹은 폴더명을 수정하거나 옮기는 작업만 한 경우
    - 🔥 **Remove**: 파일을 삭제하는 작업만 수행한 경우
  - git commit -m “Feat: 간단한 설명”
    - 예시 `💡 Feat: 로그인 추가`
  - 제목 첫 글자 대문자, 명령문으로 작성

### 7. Jira

| 2주차 | 3주차 | 4주차 |
| ----- | ----- | ----- |
| ![jira_번다운차트_2주차](./readme-assets/jira_번다운차트_2주차.png) | ![jira_번다운차트_3주차](./readme-assets/jira_번다운차트_3주차.png) | ![jira_번다운차트_4주차](./readme-assets/jira_번다운차트_4주차.png) |

| 5주차 | 7주차 |
| ----- | ----- |
| ![jira_번다운차트_5주차](./readme-assets/jira_번다운차트_5주차.png) | ![jira_번다운차트_7주차](./readme-assets/jira_번다운차트_7주차.png) |

- 목적: 협업, 일정, 업무 관리
- 방법
  1. 월요일 오전에 주 단위 계획
  2. 백로그 생성
  3. 스프린트 시작
- 스프린트: 일주일 단위

**에픽**

- 에픽은 반드시 생성하고 작업을 연동
- 기능의 에픽 이름은 `기능 명세서의 주 기능`
- 컴포넌트가 통합인 에픽들은 해당하는 개발 단계에 맞춰서 작성

**작업**

- 작업 생성 시 기능에 따라 컴포넌트를 연동
  - 스토리 포인트는 최대 4시간으로 제한
    - 스토리 포인트는 중요도 순서로 할당 (4 → 3 → 2 → 1 **시간**)
- 작업을 완료할 때 작업 설명에 자세히 작성

**컴포넌트**

- 작업의 유형에 따라 `FE` / `BE` / `통합` 컴포넌트를 선택
- `FE` : 프론트엔드
- `BE` : 백엔드 - spring, fastapi 폴더
- `DATA` : 빅데이터 데이터 전처리 - bigdata 폴더
- `통합` : 기획, 설계, 최종, 발표 준비 등등

### 8. WBS

[📊 WBS 구글시트](https://docs.google.com/spreadsheets/d/1hcbCjCL8dCyVNqgF-HfabzcfaH545BLqa04mMLta3I8/edit#gid=0)

![WBS](./readme-assets/WBS.gif)

### 9. 프로젝트 구조

**Front-End (React)**

```
📁frontend
├── 📁public
└── 📁src
    ├── 📁assets
    │   ├── 📁fonts
    │   └── 📁img
    ├── 📁components
    │   ├── 📁atoms
    │   ├── 📁organisms
    │   └── 📁pages
    │       ├── 📁Auth
    │       ├── 📁ContentRecommendPage
    │       ├── 📁KeywordRecommendPage
    │       ├── 📁MainPage
    │       ├── 📁MediaRecommendPage
    │       ├── 📁MyPage
    │       ├── 📁NewspaperRecommendation
    │       ├── 📁OnlineRecommendation
    │       ├── 📁OutdoorRecommendation
    │       ├── 📁RadioRecommendation
    │       └── 📁TvRecommendation
    ├── 📁routes
    ├── 📁slices
    └── 📁store
```

**Back-End (Spring Boot, FastAPI)**

```
📁spring
├── 📁gradle
│   └── 📁wrapper
└── 📁src
    └── 📁main
        ├── 📁java
        │   └── 📁com
        │       └── 📁ssafy
        │           └── 📁adrec
        │               ├── 📁jwt
        │               │   └── 📁service
        │               ├── 📁area
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁response
        │               │   └── 📁service
        │               ├── 📁content
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁request
        │               │   ├── 📁response
        │               │   └── 📁service
        │               ├── 📁keyword
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁request
        │               │   ├── 📁response
        │               │   └── 📁service
        │               ├── 📁media
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁response
        │               │   └── 📁service
        │               ├── 📁member
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁request
        │               │   └── 📁service
        │               ├── 📁myPage
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁request
        │               │   ├── 📁response
        │               │   └── 📁service
        │               ├── 📁product
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁response
        │               │   └── 📁service
        │               ├── 📁targetAnalyze
        │               │   ├── 📁controller
        │               │   ├── 📁repository
        │               │   ├── 📁request
        │               │   ├── 📁response
        │               │   └── 📁service
        │               └── 📁offline
        │                   ├── 📁controller
        │                   └── 📁outdoor
        │                       ├── 📁repository
        │                       ├── 📁request
        │                       ├── 📁response
        │                       └── 📁service
        └── 📁resources
```

```
📁fastapi
└── 📁app
    ├── 📁algorithm
    └── 📁routers

```

<br>

# 📌 팀원 소개

| 연주원 | 손효민 | 최다해 | 이민규 | 이정찬 | 양수완 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| ![joo1yeon](https://avatars.githubusercontent.com/u/50977497?v=4) | ![SonHyoMin00](https://avatars.githubusercontent.com/u/68097374?v=4) | ![dahae8](https://avatars.githubusercontent.com/u/109636793?v=4) | ![lmg386411](https://avatars.githubusercontent.com/u/122497435?v=4)| ![jeongchanim](https://avatars.githubusercontent.com/u/117694504?v=4) | ![kjjs2670](https://avatars.githubusercontent.com/u/74890445?v=4) |
| [joo1yeon](https://github.com/joo1yeon)          | [SonHyoMin00](https://github.com/SonHyoMin00)        | [dahae8](https://github.com/dahae8)  | [lmg3864](https://github.com/lmg3864)    | [jeongchanim](https://github.com/jeongchanim) | [kjjs2670](https://github.com/kjjs2670) |
| 팀장<br> PM<br> Back-end<br> Infra<br> 기획 발표 | BE-Leader<br> Back-end<br> Data 분석 & 추천 | Back-end<br> Data 분석 & 추천 | FE-Leader<br> Front-end<br> 최종 발표 | Front-end<br> Data 분석           | Front-end<br> UCC 제작         |
