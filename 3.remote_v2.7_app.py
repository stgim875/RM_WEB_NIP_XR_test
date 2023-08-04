from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from appium import webdriver

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import KeyInput
from selenium.webdriver.common.actions.action_builder import PointerActions
from selenium.webdriver.common.actions.action_builder import PointerInput

import time

desired_caps = UiAutomator2Options()
desired_caps = {
"appium:deviceName": "Galaxy S22",
"platformName": "Android",
"appium:platformVersion": "13",
"appium:automationName": "Appium",
"appium:app": "C:\\XR_Remote v2.7_private\\remote_mobile_2700012.apk",
"appium:noReset": 'false',
"appium:appWaitActivity": "*",
"newCommandTimeout": 5000
}

driver= webdriver.Remote(
    "http://127.0.0.1:4723/wd/hub", desired_caps)

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 접근 권한 허용 종류 다이얼 로그창 출력 확인
try:
    permission = driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2:id/mobile_permission_fragment")
    if permission.is_displayed():
        print("접근 권한 허용 다이얼 로그창 출력되었습니다.")
    else:
        print("접근 권한 허용 다이얼 로그창이 출력되지 않았습니다.")
        
    # 접근 권한 허용 다이얼 로그창 > 확인 버튼 클릭
    permission_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.virnect.remote.mobile2:id/permission_btn_confirm")))
    actions = ActionChains(driver)\
        .move_to_element(permission_btn)\
        .click(permission_btn)\
        .perform()
    print("권한 허용 다이얼 로그창에서 확인 버튼을 클릭했습니다.")
except NoSuchElementException:
    print("접근 권한 허용 다이얼 로그창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 동영상 녹화 허용 다이얼 로그창 출력 확인
try:
    recording = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
    if recording.is_displayed():
        print("동영상 녹화 허용 다이얼 로그창이 출력되었습니다.")
    else:
        print("동영상 녹화 허용 다이얼 로그창이 출력되지 않았습니다.")
        
    # 녹화 허용 다이얼 로그창 > 앱 사용 중에만 허용 클릭
    recording_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    actions = ActionChains(driver)\
        .move_to_element(recording_btn)\
        .click(recording_btn)\
        .perform()
    print("동영상 녹화 허용 다이얼 로그창에서 앱 사용 중에서만 허용을 클릭했습니다.")
except NoSuchElementException:
    print("동영상 녹화 허용 다이얼 로그창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 내 기기의 위치 정보에 액세스 하도록 허용 다이얼 로그창 출력 확인
try:
    recording = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
    if recording.is_displayed():
        print("내 기기의 위치 정보에 액세스 하도록 허용 다이얼 로그창이 출력되었습니다.")
    else:
        print("내 기기의 위치 정보에 액세스 하도록 허용 다이얼 로그창이 출력되지 않았습니다.")
        
    # 녹화 허용 다이얼 로그창 > 앱 사용 중에만 허용 클릭
    recording_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    actions = ActionChains(driver)\
        .move_to_element(recording_btn)\
        .click(recording_btn)\
        .perform()
    print("내 기기의 위치 정보에 액세스 하도록 허용 다이얼 로그창에서 앱 사용 중에서만 허용을 클릭했습니다.")
except NoSuchElementException:
    print("내 기기의 위치 정보에 액세스 하도록 허용 다이얼 로그창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 오디오 녹음 허용 다이얼 로그창 출력 확인
try:
    audio = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
    if audio.is_displayed():
        print("오디오 녹음 허용 다이얼 로그창이 출력되었습니다.")
    else:
        print("오디오 녹음 다이얼 로그창이 출력되지 않았습니다.")
        
    # 오디오 녹음 허용 다이얼 로그창 > 앱 사용 중에만 허용 클릭
    audio_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
    actions = ActionChains(driver)\
        .move_to_element(audio_btn)\
        .click(audio_btn)\
        .perform()
    print("오디오 녹음 허용 다이얼 로그창에서 앱 사용 중에만 허용을 클릭했습니다.")
except NoSuchElementException:
    print("오디오 녹음 허용 다이얼 로그창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Remote에서 근처 기기를 찾을 수 있도록 상대적 위치 파악 허용 다이얼 로그창 출력 확인
try:
    agree = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
    if agree.is_displayed():
        print("상대적 위치 파악 허용 다이얼 로그창이 출력되었습니다.")
    else:
        print("상대적 위치 파악 허용 다이얼 로그창이 출력되지 않았습니다.")
        
    # 상대적 위치 파악 허용 다이얼 로그창 > 허용 클릭
    agree_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")))
    actions = ActionChains(driver)\
        .move_to_element(agree_btn)\
        .click(agree_btn)\
        .perform()
    print("상대적 위치 파악 허용 다이얼 로그창에서 허용을 클릭했습니다.")
except NoSuchElementException:
    print("상대적 위치 파악 허용 다이얼 로그창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# VIRNECT Remote에서 기기의 사진, 동영상, 음악, 오디오에 액세스 허용 다이얼 로그창 출력 확인
try:
    picture = driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/grant_dialog")
    if picture.is_displayed():
        print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창이 출력되었습니다.")
    else:
        print("기기의 사진, 동영상, 음악, 오디오 액세스 허용 다이얼 로그창이 출력되지 않았습니다.")
        
    # 기기의 사진 및 미디어 액세스 허용 다이얼 로그창 > 허용 클릭
    picture_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")))
    actions = ActionChains(driver)\
        .move_to_element(picture_btn)\
        .click(picture_btn)\
        .perform()
    print("기기의 사진, 동영상, 음악, 오디오에 액세스 허용 다이얼 로그창에서 허용을 클릭했습니다.")
except NoSuchElementException:
    print("기기의 사진, 동영상, 음악, 오디오에 액세스 허용 다이얼 로그창을 찾을 수 없습니다.")

# 30초동안 타임 슬립
time.sleep(30)

# SERVER INFO 출력 확인
try:
    server_info = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout')
    if server_info.is_displayed():
        print("SERVER INFO 모달창이 출력되었습니다.")
    else:
        print("SERVER INFO 모달창이 출력되지 않았습니다.")
except NoSuchElementException:
    print("SERVER INFO 모달창을 찾을 수 없습니다.")

# "com.virnect.remote.mobile2:id/action_bar_root"
# '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout'
# '*//[@resource-id="com.virnect.remote.mobile2:id/action_bar_root"]'

# 5초동안 타임 슬립
time.sleep(5)

# SERVER IP 입력하기
try:
    server_ip = driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/server_url_setting_et_ip']")
    if server_ip.is_displayed():
        print("IP 입력 필드가 존재합니다.")
        
        # SERVER IP 입력하기
        server_ip.clear()
        server_ip.send_keys('61.98.205.242')
        print("SERVER IP를 입력했습니다.")
    else:
        print("IP 입력 필드가 존재하지 않습니다.")
except NoSuchElementException:
    print("IP 입력 필드를 찾을 수 없습니다.")

# SERVER PORT 입력하기
# 현재 port는 디폴트로 입력되어 있음 : 8073

# 5초동안 타임 슬립
time.sleep(5)

# SERVER INFO에서 확인 버튼 클릭
try:
    check = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]')
    if check.is_displayed():
        print("SERVER INFO 모달창에 IP 입력 필드가 존재합니다.")
    else:
        print("SERVER INFO 모달창에 IP 입력 필드가 존재하지 않습니다.")
    check_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]')))
    actions = ActionChains(driver)\
        .move_to_element(check_btn)\
        .click(check_btn)\
        .perform()
    print("SERVER INFO 모달창에서 확인 버튼을 클릭했습니다.")
except NoSuchElementException:
    print("SERVER INFO 모달창에서 확인 버튼을 클릭하지 못했습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Remote v2.7 로그인창 출력 확인
try:
    login_frame = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout')
    if login_frame.is_displayed():
        print("로그인창이 출력되었습니다.")
    else:
        print("로그인창이 출력되지 않았습니다.")
except NoSuchElementException:
    print("로그인창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Remote v2.7 로그인창 > 아이디 입력 필드 존재 확인 > 아이디 입력(user2)
try:
    login_id = driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2:id/login_tl_id")
    if login_id.is_displayed():
        print("로그인창에 아이디 입력 필드가 존재합니다.")
        
        # 로그인창 > ID 입력
        login_id_input = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.AutoCompleteTextView")
        login_id_input.clear()
        login_id_input.send_keys('user2')
        print("아이디를 입력했습니다.")
    else:
        print("로그인창에 아이디 입력 필드가 존재하지 않습니다.")
except NoSuchElementException:
    print("로그인창에서 아이디 입력 필드를 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Remote v2.7 로그인창 > 비밀번호 입력 필드 존재 확인 > 비밀번호 입력(Admin1324)
try:
    login_pwd = driver.find_element(AppiumBy.ID, "com.virnect.remote.mobile2:id/login_input_et_pwd")
    if login_pwd.is_displayed():
        print("로그인창에 비밀번호 입력 필드가 존재합니다.")
        
        # 로그인창 > 비밀번호 입력
        login_pwd_input = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        login_pwd_input.clear()
        login_pwd_input.send_keys('Admin1324')
        print("비밀번호를 입력했습니다.")
    else:
        print("로그인창에 비밀번호 입력 필드가 존재하지 않습니다.")
except NoSuchElementException:
    print("로그인창에 비밀번호 입력 필드를 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Remote v2.7 로그인 아이디 및 패스워드 입력 > 로그인 버튼 선택
try:
    login_btn = driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/login_btn_login']")
    if login_btn.is_displayed():
        print("로그인 버튼이 존재합니다.")
        
        # 로그인 버튼 클릭
        login_btn_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/login_btn_login']")))
        actions = ActionChains(driver)\
            .move_to_element(login_btn_click)\
            .click(login_btn_click)\
            .perform()
        print("로그인 버튼을 클릭했습니다.")
    else:
        print("로그인 버튼이 존재하지 않습니다.")
except NoSuchElementException:
    print("로그인 버튼을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 워크스페이스 선택 모달창 출력 확인 > 워크스페이스 선택
try:
    workspace_modal = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
    if workspace_modal.is_displayed():
        print("워크스페이스 선택 모달창이 존재합니다.")
        
        # 워크스페이스 선택
        workspace_select = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/rc_item_tv_title']")))
        actions = ActionChains(driver)\
            .move_to_element(workspace_select)\
            .click(workspace_select)\
            .perform()
        print("워크스페이스를 클릭했습니다.")
    else:
        print("워크스페이스 모달창이 존재하지 않습니다.")
except NoSuchElementException:
    print("워크스페이스 모달창을 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 메뉴 존재 확인
try:
    remote_room = driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/action_bar_root']")
    if remote_room.is_displayed():
        print("원격 협업 룸이 존재합니다.")
    else:
        print("원격 협업 룸이 존재하지 않습니다.")
except NoSuchElementException:
    print("원격 협업 룸이 존재하지 않습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 룸에서 새로고침
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(529, 856)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(521, 1299)
actions.w3c_actions.pointer_action.release()
actions.perform()

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 > 협업 요청 메시지 리스트 존재 확인(XR 건설_3차_E2E 테스트) > 협업 요청 메시지 클릭
try:
    remote_collaboration = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup')
    if remote_collaboration.is_displayed():
        print("XR 건설_3차_E2E 테스트 원격 협업 요청 메시지가 존재합니다.")
        
        # 협업 요청 메시지 클릭(XR 건설_3차_E2E 테스트)
        message_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//*[@resource-id="com.virnect.remote.mobile2:id/rc_item_tv_title" and @text="XR 건설_3차_E2E 테스트"]')))
        actions = ActionChains(driver)\
            .move_to_element(message_click)\
            .click(message_click)\
            .perform()
        print("XR 건설_3차_E2E 테스트 협업 메시지를 클릭했습니다.")
    else:
        print("XR 건설_3차_E2E 테스트 원격 협업 요청 메시지가 존재하지 않습니다.")
except NoSuchElementException:
    print("XR 건설_3차_E2E 테스트 원격 협업 메시지를 찾을 수 없습니다.")

# 3초동안 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 진행 중인 원격 협업 메시지 선택 > 원격 협업 참가 모달창 존재 확인 > 참가하기 클릭
try:
    collaboration_modal = driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/cl_title_wrapper']")
    if collaboration_modal.is_displayed():
        print("원격협업 참가 모달창이 존재합니다.")
        
        # 참가하기 클릭
        attend_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//*[@resource-id='com.virnect.remote.mobile2:id/cl_detail_wrapper']")))
        actions = ActionChains(driver)\
            .move_to_element(attend_click)\
            .click(attend_click)\
            .perform()
        print("XR 건설_3차_E2E 테스트 원격 협업 참가하기를 클릭하였습니다.")
    else:
        print("원격 협업 참가 모달창이 존재하지 않습니다.")
except NoSuchElementException:
    print("원격 협업 참가 모달창을 찾을 수 없습니다.")
