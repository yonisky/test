<테스트 파일 위치>
RPA 파일 위치 : 문서\Uipath\ClouDoc
배치 파일 위치 : 문서\Uipath\ClouDoc\batch
테스트 케이스 위치 : C:\RPA_TEST\RPA_Client_TC.xlsx

<테스트 전 최초 1회 실행 필요>
1. Uipath 실행>홈>도구>Chrome Extension 설치 후 크롬 확장 프로그램 사용 설정
2. 문서\Uipath\ClouDoc\batch\network_rule_add.bat 최초 1회 실행 필요, 이후 실행안해도 됨
3. 로컬 휴지통 속성에서 "삭제 확인 대화 상자 표시" 체크 설정 필요("B.08.온라인 보안디스크" 테스트 시 필요)

<Uipath Get Password 재입력_복사된 프로젝트 실행 시 최초 1회 수행>
1. "B.11.보안반출 선결재"에서 Get Password 액티비티 내 비밀번호 재입력 필요
2. "A.02.보안디스크"에서 Get Password 액티비티 내 비밀번호 재입력 필요