import win32api, win32gui, win32com.client, win32con, ctypes, configparser
import pywinauto, pyautogui, pygetwindow, pyperclip
import uiautomation
import os, winreg, time, datetime, math, threading, logging
from filecmp import cmp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

uiautomation.SetGlobalSearchTimeout(10)

def reg_check(hkey_constant, path, value_name):
    reg = winreg.ConnectRegistry(None, hkey_constant)
    key = winreg.OpenKey(reg, path)
    return winreg.QueryValueEx(key, value_name)[0]

def reg_edit(hkey_constant, path, value_name, value):
    reg = winreg.ConnectRegistry(None, hkey_constant)
    key = winreg.OpenKey(reg, path, 0, winreg.KEY_WRITE)
    return winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value)

def find_drive(volume_name):
    path_list = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\', 'Q:\\', 'R:\\', 'S:\\', 'T:\\','U:\\','V:\\','W:\\' ,'X:\\', 'Y:\\','Z:\\']
    for path in path_list:
        if volume_name=="온라인 보안 디스크":            
            try:
                nodrive_num = int(math.log2(reg_check(winreg.HKEY_LOCAL_MACHINE, r'Software\Microsoft\Windows\CurrentVersion\Policies\Explorer', 'NoDrives'))-2)
                if win32api.GetVolumeInformation(path)[0] == volume_name and path!=path_list[nodrive_num]:
                    return path
            except:
                try:
                    if win32api.GetVolumeInformation(path)[0] == volume_name:
                        return path
                except:
                    pass
        else:
            try:
                if win32api.GetVolumeInformation(path)[0] == volume_name:
                    return path
            except:
                pass

def move_file(id, a, b, overwrite):
    # 원본 경로에서 파일 복사
    os.startfile(a)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass     
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, True)
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.typewrite(id+'movefile', interval=0.1)
    pyautogui.hotkey('ctrl', 'x', interval=0.5)
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

    # 목적지 경로에 파일 붙여넣기
    os.startfile(b)
    for i in range(10):
        time.sleep(1)
        try:
            win2 = pygetwindow.getActiveWindow()
            break
        except:
            time.sleep(1)
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win2._hWnd)
    win32gui.ShowWindow(win2._hWnd, True)
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.hotkey('ctrl', 'v', interval=0.5)
    if overwrite==True:
        window = uiautomation.WindowControl(searchDepth=2, Name='파일 바꾸기 확인')
        window.ButtonControl(Name="예(Y)").Click()
    win32gui.PostMessage(win2._hWnd, win32con.WM_CLOSE, 0, 0)

def copy_file(id, a, b, overwrite):
    # 원본 경로에서 파일 복사
    os.startfile(a)
    win_a = uiautomation.WindowControl(searchDepth=2, RegexName='.*'+a+'.*')
    win_a.SetFocus()
    time.sleep(0.5)
    pyautogui.typewrite(id+'copyfile', interval=0.1)
    pyautogui.hotkey('ctrl', 'c', interval=0.5)
    win_a.GetWindowPattern().Close()

    # 목적지 경로에 파일 붙여넣기
    os.startfile(b)
    try:
        win_b = uiautomation.WindowControl(searchDepth=2, RegexName='.*'+a+'.*')
        win_b.SetFocus()
    except:
        win_b = uiautomation.WindowControl(searchDepth=2, RegexName=b[3:len(b)-1])
        win_b.SetFocus()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v', interval=0.5)
    if overwrite==True:
        window = uiautomation.WindowControl(searchDepth=2, Name='파일 바꾸기 확인')
        window.ButtonControl(Name="예(Y)").Click()
    win_b.GetWindowPattern().Close()

# option=0 del 삭제 // option=1 서버 삭제 // option=2 shift+서버 삭제
def delete_file(path, file, option):
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)
    # window.Maximize()
    # time.sleep(0.5)

    if option == 0:
        for i in range(3):
            try:
                window.ListItemControl(Name=file).Click()
                break
            except LookupError:
                window.MoveCursorToMyCenter()
                pyautogui.scroll(-1000)
                time.sleep(0.5)

        time.sleep(0.5)
        pyautogui.press('del')
        time.sleep(0.5)
        try:
            delwin = uiautomation.WindowControl(searchDepth=1, ClassName="#32770")
            delwin.ButtonControl(AutomationId='6').Click()
        except LookupError:
            pass
  
    elif option == 1:
        for i in range(3):
            try:
                window.ListItemControl(Name=file).Click()
                pyautogui.hotkey('shift', 'f10')
                time.sleep(3)
                break
            except LookupError:
                window.MoveCursorToMyCenter()
                pyautogui.scroll(-1000)
                time.sleep(0.5)        
        
        time.sleep(1)
        pyautogui.typewrite(['v', 'right', 'q', 'y'], interval=0.1)

    elif option == 2:
        for i in range(3):
            try:
                window.ListItemControl(Name=file).Click()
                pyautogui.hotkey('shift', 'f10')
                time.sleep(3)
                break
            except LookupError:
                window.MoveCursorToMyCenter()
                pyautogui.scroll(-1000)
                time.sleep(0.5)

        time.sleep(1)
        pyautogui.typewrite(['v', 'right'], interval=0.1)
        # pyautogui.hotkey('shift', 'q')
        pyautogui.keyDown('shift')
        pyautogui.press('q')
        pyautogui.keyUp('shift')
        time.sleep(0.5)
        pyautogui.press('y')
    time.sleep(0.5)
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

def empty_recycle(path):
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, True)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)
    window.ListItemControl(Name="RECYCLER").Click()
    pyautogui.hotkey('shift', 'f10')
    time.sleep(3)
    pyautogui.typewrite('by', interval=0.5)
    time.sleep(0.5)
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

def rename(a, name):
    os.startfile(a)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, True)
    time.sleep(0.5)
    pyautogui.press('esc')
    pyautogui.typewrite(name, interval=0.01)
    time.sleep(0.5)
    pyautogui.press('F2')
    time.sleep(1)
    pyautogui.typewrite("rename_"+name, interval=0.1)
    time.sleep(0.5)
    pyautogui.press('enter')
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)
    time.sleep(1)

def excel_create(path, cells):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True
    wb = excel.Workbooks.Add()
    ws = wb.Worksheets("Sheet1")
    ws.Cells(cells, 1).Value = "file write 1st"
    wb.SaveAs(path)
    excel.Quit()
    os.system('taskkill /F /IM EXCEL.EXE /T')

def excel_edit(path, cells):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True
    wb = excel.Workbooks.Open(path)
    ws = wb.ActiveSheet
    ws.Cells(cells, 1).Value = "file write 2nd"
    wb.Save()
    excel.Quit()
    os.system('taskkill /F /IM EXCEL.EXE /T')

def excel_read(path, cells):
    excel = win32com.client.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(path)
    ws = wb.ActiveSheet
    value = ws.Cells(cells, 1).Value
    excel.Quit()
    return value
    os.system('taskkill /F /IM EXCEL.EXE /T')

def winword_create(path, text):
    winword = win32com.client.Dispatch("Word.Application")
    winword.Visible = True
    doc = winword.Documents.Add()
    doc.Content.Text = text+'\n'
    doc.SaveAs(path)
    winword.Quit()
    # os.system('taskkill /F /IM WINWORD.EXE')

def winword_edit(path, text):
    winword = win32com.client.Dispatch("Word.Application")
    winword.Visible = True
    doc = winword.Documents.Open(path)
    doc.Content.InsertAfter(text+'\n')
    doc.Save()
    winword.Quit()
    # os.system('taskkill /F /IM WINWORD.EXE')

def winword_read(path):
    winword = win32com.client.Dispatch("Word.Application")
    winword.Visible = False
    doc = winword.Documents.Open(path)
    value = str(doc.Content.Text)
    winword.Quit()
    # os.system('taskkill /F /IM WINWORD.EXE')
    return value

def powerpnt_create(path, text):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    prs = ppt.Presentations.Add()
    slide = prs.Slides.Add(1, 1)
    # slide.Shapes.Title.TextFrame.TextRange.Text = text
    slide.Shapes.placeholders[0].TextFrame.TextRange.Text = text
    # thread 방식으로 30초 대기 후 종료
    thread = threading.Thread(target=prs.SaveAs, args=(path, ))
    thread.start()
    thread.join(30)
    # prs.Close()
    ppt.Quit()
    os.system('taskkill /F /IM POWERPNT.EXE /T')

def powerpnt_edit(path, text):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True
    prs = ppt.Presentations.Open(path)
    slide = prs.Slides[1]
    slide.Shapes.placeholders[1].TextFrame.TextRange.Text = text
    prs.Save()
    # prs.Close()
    ppt.Quit()
    os.system('taskkill /F /IM POWERPNT.EXE /T')

def powerpnt_read(path, place):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    prs = ppt.Presentations.Open(path, WithWindow=False)
    slide = prs.Slides[place]
    value = slide.Shapes.placeholders[place].TextFrame.TextRange.Text
    # prs.Close()
    ppt.Quit()
    os.system('taskkill /F /IM POWERPNT.EXE /T')
    return value

def upload(path, file):
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)

    for i in range(3):
        try:
            window.ListItemControl(Name=file).Click()
            pyautogui.hotkey('shift', 'f10')
            time.sleep(3)
            break
        except LookupError:
            window.MoveCursorToMyCenter()
            pyautogui.scroll(-1000)
            time.sleep(0.5)

    time.sleep(0.5)
    uiautomation.MenuItemControl(searchDepth=2, Name='업로드(U)').Click()
    window = uiautomation.WindowControl(searchDepth=2, Name='업로드 경로 선택')
    window.ButtonControl(AutomationId="9220").Click()
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

def download(path, file):
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)

    for i in range(3):
        try:
            window.ListItemControl(Name=file).Click()
            pyautogui.hotkey('shift', 'f10')
            time.sleep(3)
            break
        except LookupError:
            window.MoveCursorToMyCenter()
            pyautogui.scroll(-1000)
            time.sleep(0.5)

    time.sleep(0.5)
    # uiautomation.MenuItemControl(searchDepth=2, AutomationId='31062').Click()
    uiautomation.MenuItemControl(searchDepth=2, Name='다운로드(W)').Click()
    window = uiautomation.WindowControl(searchDepth=2, Name='폴더 찾아보기')
    window.TreeItemControl(Name="바탕 화면").Click()
    window.ButtonControl(Name="확인").Click()
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

def weblink(web_version, path, file):
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)

    for i in range(3):
        try:
            window.ListItemControl(Name=file).Click()
            pyautogui.hotkey('shift', 'f10')
            time.sleep(3)
            break
        except LookupError:
            window.MoveCursorToMyCenter()
            pyautogui.scroll(-1000)
            time.sleep(0.5)

    uiautomation.MenuItemControl(searchDepth=2, Name='웹링크(L)').MoveCursorToInnerPos()
    uiautomation.MenuItemControl(searchDepth=3, Name='웹링크 복사(Y)...').Click()
    time.sleep(1)

    for i in range(30):
        try:
            weblink_win = uiautomation.WindowControl(searchDepth=2, ClassName='#32770')
            weblink_win.ButtonControl(AutomationId='1').Click()
            window.ButtonControl(searchDepth=3, Name='확인(O)').Click()
            break
        except:
            time.sleep(1)

    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    print('Google Chrome version is '+driver.capabilities['browserVersion']+'<BR>')
    driver.get(pyperclip.paste())
    if web_version=='3':
        driver.find_element_by_xpath('//*[@id="BodyWrap"]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td/a').click() #81번 서버 전용 xpath
    elif web_version=='2':
        driver.find_element_by_xpath('//*[@id="BodyWrap"]/table/tbody/tr[2]/td/a').click() #183번 서버 전용 xpath

    for i in range(30):
        if os.path.exists(os.path.join(os.path.expanduser('~'), 'Downloads', 'weblink.txt')):
            driver.close()
            driver.quit()
            break
        else:
            time.sleep(1)
    
    chrome_result = cmp(find_drive('개인문서함')+'weblink.txt', os.path.join(os.path.expanduser('~'), 'Downloads', 'weblink.txt'))
    os.remove(os.path.join(os.path.expanduser('~'), 'Downloads', 'weblink.txt'))

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    print('MS Edge version is '+driver.capabilities['browserVersion'])
    driver.get(pyperclip.paste())
    if web_version=='3':
        driver.find_element_by_xpath('//*[@id="BodyWrap"]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td/a').click() #81번 서버 전용 xpath
    elif web_version=='2':
        driver.find_element_by_xpath('//*[@id="BodyWrap"]/table/tbody/tr[2]/td/a').click() #183번 서버 전용 xpath

    for i in range(30):
        if os.path.exists(os.path.join(os.path.expanduser('~'), 'Downloads', 'weblink.txt')):
            driver.close()
            driver.quit()
            break
        else:
            time.sleep(1)

    msedge_result = cmp(find_drive('개인문서함')+'weblink.txt', os.path.join(os.path.expanduser('~'), 'Downloads', 'weblink.txt'))
    os.remove(os.path.join(os.path.expanduser('~'), 'Downloads', 'weblink.txt'))

    return chrome_result, msedge_result

def after_export(path, file):
    export_time = datetime.datetime.now()
    print(export_time)
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)

    for i in range(3):
        try:
            window.ListItemControl(Name=file).Click()
            pyautogui.hotkey('shift', 'f10')
            time.sleep(3)
            break
        except LookupError:
            window.MoveCursorToMyCenter()
            pyautogui.scroll(-1000)
            time.sleep(0.5)

    time.sleep(0.5)
    uiautomation.MenuItemControl(searchDepth=2, Name='반출 신청(X)').Click()

    for i in range(60):
        try:
            export_win = uiautomation.WindowControl(searchDepth=2, Name='반출 신청')
            export_win.SetFocus()
            export_win.RadioButtonControl(AutomationId='9227').Click()
            break
        except:
            time.sleep(3)
    time.sleep(1)

    export_win.RadioButtonControl(AutomationId='9228').Click()
    export_win.ButtonControl(AutomationId='1').Click()
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

    time.sleep(10)

    os.startfile(path+'DOC_EXPORT')
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)

    for i in range(60):
        try:
            export_folder = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 0)
            break
        except:
            time.sleep(1)
    
    for i in range(60):    
        if export_folder > export_time.strftime("%Y-%m-%d[%H.%M.%S]"):
            pyautogui.press('f5')
            time.sleep(1)
            break
        else:
            time.sleep(1)
            export_folder = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 0)

    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)

    for i in range(60):
        try:
            pyautogui.press('f5')
            window.ListItemControl(Name=export_folder).Click()
            pyautogui.hotkey('shift', 'f10')
            time.sleep(3)
            break
        except:
            pyautogui.press('f5')
            window.MoveCursorToMyCenter()
            pyautogui.scroll(-1000)
            time.sleep(1)

    time.sleep(0.5)
    # uiautomation.MenuItemControl(searchDepth=2, AutomationId='31078').Click()
    uiautomation.MenuItemControl(searchDepth=2, Name='문서 반출(R)').Click()
    find_win = uiautomation.WindowControl(searchDepth=1, Name='폴더 찾아보기')
    find_win.TreeItemControl(searchDepth=4, Name='바탕 화면').Click()
    find_win.ButtonControl(AutomationId='1').Click()
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)

def pre_export(web_version, addr, id, pw, path, file):
    export_time = datetime.datetime.now()
    print(export_time)
    os.startfile(path)
    for i in range(10):
        time.sleep(1)
        try:
            win = pygetwindow.getActiveWindow()
            break
        except:
            pass      
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(win._hWnd)
    win32gui.ShowWindow(win._hWnd, win32con.SW_SHOWMAXIMIZED)
    time.sleep(0.5)
    pyautogui.press('esc')
    window = uiautomation.WindowControl(searchDepth=1, Name=win.title)

    for i in range(3):
        try:
            window.ListItemControl(Name=file).Click()
            pyautogui.hotkey('shift', 'f10')
            time.sleep(3)
            break
        except LookupError:
            window.MoveCursorToMyCenter()
            pyautogui.scroll(-1000)
            time.sleep(0.5)

    time.sleep(0.5)
    uiautomation.MenuItemControl(searchDepth=2, Name='반출 신청(X)').Click()

    for i in range(60):
        try:
            export_win = uiautomation.WindowControl(searchDepth=2, Name='반출 신청')
            export_win.SetFocus()
            export_win.EditControl(Name="승인권자(A):").SendKeys(export_time.strftime("%Y-%m-%d_%H%M%S"))
            break
        except:
            time.sleep(3)
    time.sleep(1)
  
    export_win.RadioButtonControl(AutomationId='9226').Click()
    export_win.RadioButtonControl(AutomationId='9229').Click()
    export_win.ButtonControl(AutomationId='1').Click()
    win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)
    
    for i in range(60):
        try:
            win = pygetwindow.getWindowsWithTitle('알림 관리')[0]
            shell = win32com.client.Dispatch("WScript.Shell")
            win32gui.SetForegroundWindow(win._hWnd)
            win32gui.ShowWindow(win._hWnd, True)
            alarm_win = uiautomation.WindowControl(searchDepth=1, Name='알림 관리')
            alarm_win.TextControl(searchDepth=3, Name=export_time.strftime("%Y-%m-%d_%H%M%S")).Click()
            break
        except IndexError:
            time.sleep(3)
        except LookupError:
            alarm_win.GetWindowPattern().Close()

    time.sleep(1)

    if web_version == '3':
        # 크로미움엣지 드라이버로 승인 진행
        driver = webdriver.Edge(EdgeChromiumDriverManager(log_level=logging.ERROR).install())
        driver.implicitly_wait(10)
        main_window = driver.window_handles[0]
        driver.get("http://"+addr+"/websvc/index/login.jsp")
        driver.implicitly_wait(10)
        driver.find_element_by_class_name('btn.btn-success').click()
        driver.find_element_by_id('id').send_keys(id)
        driver.find_element_by_id('pass').send_keys(pw)
        driver.find_element_by_class_name('btn.btn-success.btn-block.btn-next.d-ib.m-t.login-btn').click()
        driver.get("http://"+addr+"/filtersvc2/approval_doc_export_list.jsp")
        driver.find_element_by_xpath('//*[@id="Approvalsearch"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]/a').click()
        driver.find_element_by_id('approve').click()
        driver.implicitly_wait(10)
        driver.find_element_by_name('reason').send_keys("rpa_"+export_time.strftime("%Y-%m-%d_%H%M%S"))
        driver.find_element_by_id('btnSelect').click()
        time.sleep(10)
        # pyautogui.press('enter')
        alert = driver.switch_to.alert
        alert.accept()
        driver.close()
        driver.quit()
        # os.system('taskkill /F /IM msedge.exe')

    elif web_version == '2':
        driver = webdriver.Edge(EdgeChromiumDriverManager(log_level=logging.ERROR).install())
        driver.implicitly_wait(10)
        driver.get("http://"+addr)
        driver.implicitly_wait(10)
        driver.switch_to.frame(driver.find_element_by_name('bottom'))
        driver.find_element_by_name('id').send_keys(id)
        driver.find_element_by_name('pass').send_keys(pw)
        driver.find_element_by_xpath('//*[@id="Info_Tab_Contents"]/table/tbody/tr/td[9]/input').click()
        driver.find_element_by_id('disklock').click()
        driver.find_element_by_xpath('//*[@id="Doc_Menu"]/table/tbody/tr/td[2]/a/img').click()
        driver.find_element_by_xpath('//*[@id="BodyWrap_2"]/div/div[3]/form/table/tbody/tr/td[3]/a/span').click()
        driver.find_element_by_name('Reason').send_keys("rpa_"+export_time.strftime("%Y-%m-%d_%H%M%S"))
        driver.find_element_by_xpath('//*[@id="BodyWrap_2"]/div/div[3]/div[1]/img[2]').click()
        time.sleep(5)
        alert = driver.switch_to.alert
        alert.accept()
        driver.close()
        driver.quit()
  
        # alarm_win.TextControl(searchDepth=6, Name='결재 페이지로 이동하기').Click()
        # for i in range(120):
        #     try:
        #         IE_win = uiautomation.WindowControl(searchDepth=1, ClassName='IEFrame')
        #         IE_win.Maximize()
        #         IE_win.TabItemControl(searchDepth=6, Name='ClouDoc').Click()
        #         IE_win.PaneControl(searchDepth=5, Name='ClouDoc').Click()
        #         IE_win.MoveCursorToMyCenter()
        #         pyautogui.scroll(-1000)
        #         break
        #     except:
        #         time.sleep(1)
        # for i in range(30):
        #     try:
        #         IE_win.EditControl(searchDepth=10, AutomationId='Reason').SendKeys("rpa_"+export_time.strftime("%Y-%m-%d_%H%M%S"), waitTime=1)
        #         pyautogui.click(pyautogui.locateCenterOnScreen("image_src/btn_approval.png"))
        #         uiautomation.ButtonControl(searchDepth=3, AutomationId='1').Click()
        #         uiautomation.ButtonControl(searchDepth=4, Name='확인').Click()
        #         break
        #     except:
        #         time.sleep(1)
        # time.sleep(3)
        # os.system('taskkill /F /IM iexplore.exe')

    alarm_win.GetWindowPattern().Close()

    for i in range(30):
        try:
            win = pygetwindow.getWindowsWithTitle('알림 관리')[0]
            shell = win32com.client.Dispatch("WScript.Shell")
            win32gui.SetForegroundWindow(win._hWnd)
            win32gui.ShowWindow(win._hWnd, True)
            break
        except IndexError:
            time.sleep(5)

    alarm_win = uiautomation.WindowControl(searchDepth=1, Name='알림 관리')
    alarm_win.TextControl(searchDepth=3, Name="[알림] 반출 승인(선결재)").Click()
    alarm_win.ButtonControl(AutomationId="9221").Click()
    find_win = uiautomation.WindowControl(searchDepth=1, Name='폴더 찾아보기')
    find_win.TreeItemControl(searchDepth=4, RegexName='반출 보안 디스크.*').Click()
    find_win.ButtonControl(AutomationId='1').Click()
    uiautomation.ButtonControl(searchDepth=3, AutomationId='1').Click()
    alarm_win.GetWindowPattern().Close()

def recent_file_name(path, num):
    file_list = []
    for f_name in os.listdir(path):
        written_time = os.path.getmtime(path+"/"+f_name)
        file_list.append((f_name, written_time))
    file_list = sorted(file_list, key=lambda x: x[0], reverse=True)
    if file_list[0][0] != "desktop.ini" and file_list[0][0] != 'System Volume Information':
        recent_file = file_list[num][0]
    else:
        try:
            recent_file = file_list[num+1][0]
        except:
            pass
    return recent_file

def add_rule(rule_name, remoteip):
    """ Add rule to Windows Firewall """
    if os.popen(f'netsh advfirewall firewall show rule name="{rule_name}').read() == '\n지정된 조건과 일치하는 규칙이 없습니다.\n\n':
        ctypes.windll.shell32.ShellExecuteW(None, "runas", 'netsh.exe', f'advfirewall firewall add rule name="{rule_name}" dir=out action=block remoteip="{remoteip}" enable=no', None, 1)
        print(f"Rule {rule_name} for {remoteip} added")
        time.sleep(3)
    else:
        print("Rule already exist")

def modify_rule(rule_name, state):
    """ Enable/Disable specific rule, 0 = Disable / 1 = Enable """
    ctypes.windll.shell32.ShellExecuteW(None, "runas", 'netsh.exe', f'advfirewall firewall set rule name="{rule_name}" dir=out new enable={state}', None, 1)
    if ctypes.windll.shell32.IsUserAnAdmin():
        pass
    else:
        os.system("pause")


def web_export(path, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "msedge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get("https://wormhole.app/")
    result = None
    try:
        driver.find_element_by_css_selector("input[type='file']").send_keys(path)
    except InvalidArgumentException:
        print("InvalidArgumentException")
        web_upload = False

    for i in range(30):
        try:
            result = driver.find_element_by_xpath('//h2[contains(text(), "업로드 완료")]').text
            print("web upload: "+web_upload)
            break
        except:
            time.sleep(1)

    if result == '업로드 완료':
        web_upload = True
    else:
        print('업로드 시간 초과')
        web_upload = False
    
    driver.close()
    driver.quit()
    return web_upload