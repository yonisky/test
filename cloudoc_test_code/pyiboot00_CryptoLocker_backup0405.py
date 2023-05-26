# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from http import server
import os, shutil, winreg, datetime, time, sys, winshell, requests, tkinter, platform, csv, configparser
import unittest, HtmlTestRunner
from pyiboot6 import *

# %%
# testid 딕셔너리 정의
testid_dic = {1:'test_001_reg_check_dwMajorVersion'}
testid_dic[2]='test_002_reg_check_dwMinorVersion'
testid_dic[3]='test_003_reg_check_InstallPath'
testid_dic[4]='test_004_reg_check_ProductName'
testid_dic[5]='test_005_reg_check_npStartup'
testid_dic[6]='test_006_free_policy_excel_file_create_in_desktop'
testid_dic[7]='test_007_free_policy_winword_file_create_in_desktop'
testid_dic[8]='test_008_free_policy_powerpnt_file_create_in_desktop'
testid_dic[9]='test_009_excel_file_create_in_personal_drive'
testid_dic[10]='test_010_excel_file_edit_in_personal_drive'
testid_dic[11]='test_011_winword_file_create_in_personal_drive'
testid_dic[12]='test_012_winword_file_edit_in_personal_drive'
testid_dic[13]='test_013_powerpnt_file_create_in_personal_drive'
testid_dic[14]='test_014_powerpnt_file_edit_in_personal_drive'
testid_dic[15]='test_015_excel_file_create_in_team_drive'
testid_dic[16]='test_016_excel_file_edit_in_team_drive'
testid_dic[17]='test_017_winword_file_create_in_team_drive'
testid_dic[18]='test_018_winword_file_edit_in_team_drive'
testid_dic[19]='test_019_powerpnt_file_create_in_team_drive'
testid_dic[20]='test_020_powerpnt_file_edit_in_team_drive'
testid_dic[21]='test_021_copy_file_from_personal_drive_to_subpath'
testid_dic[22]='test_022_copy_file_from_personal_drive_to_team_drive'
testid_dic[23]='test_023_overwrite_copy_file_from_personal_drive_to_subpath'
testid_dic[24]='test_024_overwrite_copy_file_from_personal_drive_to_team_drive'
testid_dic[25]='test_025_delete_file_in_personal_drive'
testid_dic[26]='test_026_delete_file_in_team_drive'
testid_dic[27]='test_027_empty_recycle_in_personal_drive'
testid_dic[28]='test_028_empty_recycle_in_team_drive'
testid_dic[29]='test_029_server_delete_file_in_personal_drive'
testid_dic[30]='test_030_move_file_from_personal_drive_to_subpath'
testid_dic[31]='test_031_move_file_from_personal_drive_to_team_drive'
testid_dic[32]='test_032_overwrite_move_file_from_personal_drive_to_team_drive'
testid_dic[33]='test_033_shift_server_delete_file_in_team_drive'
testid_dic[34]='test_034_rename_file_in_personal_drive'
testid_dic[35]='test_035_rename_file_in_team_drive'
testid_dic[36]='test_036_ext_upload_from_local_drive_to_personal_drive'
testid_dic[37]='test_037_ext_download_from_personal_drive_to_local_drive'
testid_dic[38]='test_038_weblink_in_personal_drive'
testid_dic[39]='test_039_after_export_in_personal_drive'
testid_dic[40]='test_040_pre_export_in_personal_drive'
testid_dic[41]='test_041_export_drive_when_cloudoc_login'
testid_dic[42]='test_042_web_export_from_doc_export'
testid_dic[43]='test_043_secure_export_from_doc_export_to_web'
testid_dic[44]='test_044_secure_export_from_export_drive_to_web'
testid_dic[45]='test_045_whitelist_policy_excel_file_edit_in_desktop'
testid_dic[46]='test_046_whitelist_policy_winword_file_edit_in_desktop'
testid_dic[47]='test_047_whitelist_policy_powerpnt_file_edit_in_desktop'
testid_dic[48]='test_048_whitelist_save_excel_to_desktop'
testid_dic[49]='test_049_whitelist_save_winword_to_desktop'
testid_dic[50]='test_050_whitelist_save_powerpnt_to_desktop'
testid_dic[51]='test_051_excel_file_create_in_online_secure_drive'
testid_dic[52]='test_052_excel_file_edit_in_online_secure_drive'
testid_dic[53]='test_053_winword_file_create_in_online_secure_drive'
testid_dic[54]='test_054_winword_file_edit_in_online_secure_drive'
testid_dic[55]='test_055_powerpnt_file_create_in_online_secure_drive'
testid_dic[56]='test_056_powerpnt_file_edit_in_online_secure_drive'
testid_dic[57]='test_057_rename_file_in_online_secure_drive'
testid_dic[58]='test_058_delete_file_in_online_secure_drive'
testid_dic[59]='test_059_restore_file_to_online_secure_drive'
testid_dic[60]='test_060_check_mount_offline_secure_drive'
testid_dic[61]='test_061_excel_file_create_in_offline_secure_drive'
testid_dic[62]='test_062_excel_file_edit_in_offline_secure_drive'
testid_dic[63]='test_063_winword_file_create_in_offline_secure_drive'
testid_dic[64]='test_064_winword_file_edit_in_offline_secure_drive'
testid_dic[65]='test_065_powerpnt_file_create_in_offline_secure_drive'
testid_dic[66]='test_066_powerpnt_file_edit_in_offline_secure_drive'
testid_dic[67]='test_067_rename_file_in_offline_secure_drive'
testid_dic[68]='test_068_upload_offline_secure_drive'
testid_dic[69]='test_069_internal_network_allowed_IP_bands'
testid_dic[70]='test_070_internal_network_rejected_IP_bands'
testid_dic[71]='test_071_switch_to_external_network_mode'
testid_dic[72]='test_072_external_network_unmount_drive'
testid_dic[73]='test_073_external_network_rejected_IP_bands'
testid_dic[74]='test_074_external_network_allowed_IP_bands'
testid_dic[75]='test_075_excel_file_create_in_export_secure_drive'
testid_dic[76]='test_076_excel_file_edit_in_export_secure_drive'
testid_dic[77]='test_077_winword_file_create_in_export_secure_drive'
testid_dic[78]='test_078_winword_file_edit_in_export_secure_drive'
testid_dic[79]='test_079_powerpnt_file_create_in_export_secure_drive'
testid_dic[80]='test_080_powerpnt_file_edit_in_export_secure_drive'
testid_dic[81]='test_081_rename_file_in_export_secure_drive'
testid_dic[82]='test_082_internal_network_mount_drive'

# %%
class Client_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global now, ext_reg_flag, web_version, addr, dwMajorVersion, dwMinorVersion, team_drive, team_folder, id, pw

        if reg_check(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'HideFileExt') == 1:
            reg_edit(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'HideFileExt', 0)
            ext_reg_flag = 1
            os.startfile("explorer.exe")
            for i in range(60):
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
            time.sleep(0.5)
            pyautogui.hotkey('F5')
            time.sleep(0.5)
            win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)
        else:
            ext_reg_flag = 0

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")

        config = configparser.ConfigParser()    
        config.read('config.ini', encoding='cp949')
        web_version = config['test_conf']['web_version']
        addr = config['test_conf']['addr']
        dwMajorVersion = config['test_conf']['dwMajorVersion']
        dwMinorVersion = config['test_conf']['dwMinorVersion']
        team_drive = config['test_conf']['team_drive']
        team_folder = config['test_conf']['team_folder']
        id = config['test_conf']['id']
        pw = config['test_conf']['pw']

    @classmethod
    def tearDownClass(cls):
        if ext_reg_flag == 1:
            reg_edit(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'HideFileExt', 1)
            os.startfile("explorer.exe")
            for i in range(60):
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
            time.sleep(0.5)
            pyautogui.hotkey('F5')
            time.sleep(0.5)
            win32gui.PostMessage(win._hWnd, win32con.WM_CLOSE, 0, 0)
        else:
            pass

    def test_001_reg_check_dwMajorVersion(self):
        r1 = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\NetID\PlusDrive', 'dwMajorVersion')
        self.assertEqual(r1, int(dwMajorVersion))

    def test_002_reg_check_dwMinorVersion(self):
        r1 = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\NetID\PlusDrive', 'dwMinorVersion')
        self.assertEqual(r1, int(dwMinorVersion))

    def test_003_reg_check_InstallPath(self):
        r1 = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\NetID\PlusDrive', 'InstallPath')
        self.assertEqual(r1, r"C:\Program Files\NetID\PlusDrive")
    
    def test_004_reg_check_ProductName(self):
        r1 = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\NetID\PlusDrive', 'ProductName')
        self.assertEqual(r1, 'ClouDoc')
    
    def test_005_reg_check_npStartup(self):
        r1 = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 'npStartup')
        self.assertEqual(r1, r"C:\Program Files\NetID\PlusDrive\npStartup.exe")

    def test_006_free_policy_excel_file_create_in_desktop(self):      
        pyautogui.alert("QA_Free 정책을 적용해주세요")
        excel_create(os.path.join(os.path.expanduser('~'), 'Desktop', now), 1)
        t1 = excel_read(os.path.join(os.path.expanduser('~'), 'Desktop', now), 1)
        self.assertEqual(t1, "file write 1st")

    def test_007_free_policy_winword_file_create_in_desktop(self):      
        winword_create(os.path.join(os.path.expanduser('~'), 'Desktop', now), 'file write 1st')
        t1 = winword_read(os.path.join(os.path.expanduser('~'), 'Desktop', now) + '.docx')
        self.assertEqual(t1, "file write 1st\r\r")

    def test_008_free_policy_powerpnt_file_create_in_desktop(self):      
        powerpnt_create(os.path.join(os.path.expanduser('~'), 'Desktop', now), 'file write 1st')
        t1 = powerpnt_read(os.path.join(os.path.expanduser('~'), 'Desktop', now) + '.pptx', 0)
        self.assertEqual(t1, "file write 1st")

    def test_009_excel_file_create_in_personal_drive(self):      
        excel_create(find_drive('개인문서함')+now, 1)
        t1 = excel_read(find_drive('개인문서함')+now, 1)
        self.assertEqual(t1, "file write 1st")

    def test_010_excel_file_edit_in_personal_drive(self):
        excel_edit(find_drive('개인문서함')+now, 2)
        t1 = excel_read(find_drive('개인문서함')+now, 1)
        t2 = excel_read(find_drive('개인문서함')+now, 2)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_011_winword_file_create_in_personal_drive(self):      
        winword_create(find_drive('개인문서함')+now, 'file write 1st')
        t1 = winword_read(find_drive('개인문서함')+now + '.docx')
        self.assertEqual(t1, "file write 1st\r\r")

    def test_012_winword_file_edit_in_personal_drive(self):      
        winword_edit(find_drive('개인문서함')+now + '.docx', 'file write 2nd')
        t1 = winword_read(find_drive('개인문서함')+now + '.docx')
        self.assertEqual(t1, "file write 1st\rfile write 2nd\r\r")

    def test_013_powerpnt_file_create_in_personal_drive(self):      
        powerpnt_create(find_drive('개인문서함')+now + '.pptx', 'file write 1st')
        t1 = powerpnt_read(find_drive('개인문서함')+now + '.pptx', 0)
        self.assertEqual(t1, "file write 1st")

    def test_014_powerpnt_file_edit_in_personal_drive(self):      
        powerpnt_edit(find_drive('개인문서함')+now + '.pptx', 'file write 2nd')
        t1 = powerpnt_read(find_drive('개인문서함')+now + '.pptx', 0)
        t2 = powerpnt_read(find_drive('개인문서함')+now + '.pptx', 1)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_015_excel_file_create_in_team_drive(self):      
        excel_create(find_drive(team_drive)+team_folder+'\\'+id+'_'+now, 1)
        t1 = excel_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now, 1)
        self.assertEqual(t1, "file write 1st")

    def test_016_excel_file_edit_in_team_drive(self):
        excel_edit(find_drive(team_drive)+team_folder+'\\'+id+'_'+now, 2)
        t1 = excel_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now, 1)
        t2 = excel_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now, 2)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_017_winword_file_create_in_team_drive(self):      
        winword_create(find_drive(team_drive)+team_folder+'\\'+id+'_'+now, 'file write 1st')
        t1 = winword_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.docx')
        self.assertEqual(t1, "file write 1st\r\r")

    def test_018_winword_file_edit_in_team_drive(self):      
        winword_edit(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.docx', 'file write 2nd')
        t1 = winword_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.docx')
        self.assertEqual(t1, "file write 1st\rfile write 2nd\r\r")

    def test_019_powerpnt_file_create_in_team_drive(self):      
        powerpnt_create(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.pptx', 'file write 1st')
        t1 = powerpnt_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.pptx', 0)
        self.assertEqual(t1, "file write 1st")

    def test_020_powerpnt_file_edit_in_team_drive(self):      
        powerpnt_edit(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.pptx', 'file write 2nd')
        t1 = powerpnt_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.pptx', 0)
        t2 = powerpnt_read(find_drive(team_drive)+team_folder+'\\'+id+'_'+now + '.pptx', 1)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_021_copy_file_from_personal_drive_to_subpath(self):
        if os.path.exists(find_drive('개인문서함')+'1depth'):
            if os.path.isfile(find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt'):
                os.remove(find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt')
            else:
                pass
        else:
            os.mkdir(find_drive('개인문서함')+'1depth')
        f = open(find_drive('개인문서함')+id+'copyfile.txt', 'w')
        f.write('file copy test')
        f.close()
        copy_file(id, find_drive('개인문서함'), find_drive('개인문서함')+'1depth', 0)
        time.sleep(1)
        for i in range(40):
            try:
                self.assertTrue(cmp(find_drive('개인문서함')+id+'copyfile.txt', find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt'))
                break
            except FileNotFoundError:
                time.sleep(3)

    def test_022_copy_file_from_personal_drive_to_team_drive(self):
        if os.path.isfile(find_drive(team_drive)+team_folder+'\\'+id+'copyfile.txt'):
            os.remove(find_drive(team_drive)+team_folder+'\\'+id+'copyfile.txt')
        else:
            pass
        copy_file(id, find_drive('개인문서함'), find_drive(team_drive)+team_folder+'\\', 0)
        time.sleep(1)
        for i in range(40):
            try:
                self.assertTrue(cmp(find_drive('개인문서함')+id+'copyfile.txt', find_drive(team_drive)+team_folder+'\\'+id+'copyfile.txt'))
                break
            except FileNotFoundError:
                time.sleep(3)

    def test_023_overwrite_copy_file_from_personal_drive_to_subpath(self):
        f = open(find_drive('개인문서함')+id+'copyfile.txt', 'w')
        f.write('overwrite test')
        f.close()
        copy_file(id, find_drive('개인문서함'), find_drive('개인문서함')+'1depth', 1)
        time.sleep(1)
        for i in range(40):
            try:
                self.assertTrue(cmp(find_drive('개인문서함')+id+'copyfile.txt', find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt'))
                break
            except FileNotFoundError:
                time.sleep(3)

    def test_024_overwrite_copy_file_from_personal_drive_to_team_drive(self):
        copy_file(id, find_drive('개인문서함'), find_drive(team_drive)+team_folder+'\\', 1)
        time.sleep(1)
        for i in range(40):
            try:
                self.assertTrue(cmp(find_drive('개인문서함')+id+'copyfile.txt', find_drive(team_drive)+team_folder+'\\'+id+'copyfile.txt'))
                break
            except FileNotFoundError:
                time.sleep(3)

    def test_025_delete_file_in_personal_drive(self):
        delete_file(find_drive('개인문서함'), id+'copyfile.txt', 0)
        time.sleep(3)
        self.assertTrue(os.path.exists(find_drive('개인문서함')+id+'copyfile.txt')==0 and os.path.exists(find_drive('개인문서함')+"RECYCLER\\"+id+"copyfile.txt")==1)

    def test_026_delete_file_in_team_drive(self):
        delete_file(find_drive(team_drive)+team_folder+'\\', id+'copyfile.txt', 0)
        time.sleep(3)
        self.assertTrue(os.path.exists(find_drive(team_drive)+team_folder+'\\'+id+'copyfile.txt')==0 and os.path.exists(find_drive(team_drive)+'RECYCLER\\'+team_folder+'\\'+id+'copyfile.txt')==1)

    def test_027_empty_recycle_in_personal_drive(self):
        empty_recycle(find_drive('개인문서함'))
        self.assertFalse(os.path.exists(find_drive('개인문서함')+"RECYCLER\\"+id+"copyfile.txt"))

    def test_028_empty_recycle_in_team_drive(self):
        empty_recycle(find_drive(team_drive))
        self.assertFalse(os.path.exists(find_drive(team_drive)+'RECYCLER\\'+team_folder+'\\'+id+'copyfile.txt'))

    def test_029_server_delete_file_in_personal_drive(self):
        delete_file(find_drive('개인문서함')+'1depth', id+'copyfile.txt', 1)
        time.sleep(3)
        self.assertTrue(os.path.exists(find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt')==0 and os.path.exists(find_drive('개인문서함')+"RECYCLER\\1depth\\"+id+"copyfile.txt")==1)
        # test 18~21 teardown
        shutil.rmtree(find_drive('개인문서함')+r"RECYCLER\1depth")

    def test_030_move_file_from_personal_drive_to_subpath(self):
        f = open(find_drive('개인문서함')+id+'movefile.txt', 'w')
        f.write('file move test')
        f.close()
        if os.path.exists(find_drive('개인문서함')+'1depth'):
            if os.path.isfile(find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt'):
                os.remove(find_drive('개인문서함')+'1depth\\'+id+'copyfile.txt')
            else:
                pass
        else:
            os.mkdir(find_drive('개인문서함')+'1depth')
        move_file(id, find_drive('개인문서함'), find_drive('개인문서함')+'1depth', 0)
        time.sleep(3)
        scr_path = os.path.exists(find_drive('개인문서함')+id+'movefile.txt')
        des_path = os.path.exists(find_drive('개인문서함')+'1depth\\'+id+'movefile.txt')
        f = open(find_drive('개인문서함')+'1depth\\'+id+'movefile.txt', 'r')
        data = f.read()
        f.close()
        for i in range(40):
            try:
                self.assertTrue(scr_path==0 and des_path==1 and data=='file move test')
                break
            except FileNotFoundError:
                time.sleep(3)

    def test_031_move_file_from_personal_drive_to_team_drive(self):
        if os.path.isfile(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt'):
            os.remove(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt')
        else:
            pass
        move_file(id, find_drive('개인문서함')+'1depth', find_drive(team_drive)+team_folder+'\\', 0)
        time.sleep(3)   
        for i in range(40):
            try:
                scr_path = os.path.exists(find_drive('개인문서함')+'1depth\\'+id+'movefile.txt')
                des_path = os.path.exists(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt')
                f = open(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt', 'r')
                data = f.read()
                f.close()
                self.assertTrue(scr_path==0 and des_path==1 and data=='file move test')
                break
            except FileNotFoundError:
                time.sleep(3)

    def test_032_overwrite_move_file_from_personal_drive_to_team_drive(self):
        f = open(find_drive('개인문서함')+id+'movefile.txt', 'w')
        f.write('overwrite test')
        f.close()
        move_file(id, find_drive('개인문서함'), find_drive(team_drive)+team_folder+'\\', 1)
        time.sleep(3)
        scr_path = os.path.exists(find_drive('개인문서함')+id+'movefile.txt')
        des_path = os.path.exists(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt')
        f = open(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt', 'r')
        data = f.read()
        f.close()
        self.assertTrue(scr_path==0 and des_path==1 and data=='overwrite test')

    def test_033_shift_server_delete_file_in_team_drive(self):
        delete_file(find_drive(team_drive)+team_folder+'\\', id+'movefile.txt', 2)
        time.sleep(1)
        for i in range(10):
            if os.path.exists(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt') == False:
                break
            else:
                time.sleep(1)
        self.assertFalse(os.path.exists(find_drive(team_drive)+team_folder+'\\'+id+'movefile.txt') or os.path.exists(find_drive(team_drive)+'RECYCLER\\'+team_folder+'\\'+id+'movefile.txt'))

    def test_034_rename_file_in_personal_drive(self):
        f = open(find_drive('개인문서함')+'file_rename.txt', 'w')
        f.write('rename test')
        f.close()
        rename(find_drive('개인문서함'), 'file_rename')
        old_name = os.path.exists(find_drive('개인문서함')+'file_rename.txt')
        new_name = os.path.exists(find_drive('개인문서함')+'rename_file_rename.txt')
        f = open(find_drive('개인문서함')+'rename_file_rename.txt', 'r')
        data = f.read()
        f.close()
        self.assertTrue(old_name==0 and new_name==1 and data=='rename test')
        os.remove(find_drive('개인문서함')+'rename_file_rename.txt')

    def test_035_rename_file_in_team_drive(self):
        f = open(find_drive(team_drive)+team_folder+'\\'+id+'file.txt', 'w')
        f.write('rename test')
        f.close()
        rename(find_drive(team_drive)+team_folder+'\\', id+'file')
        old_name = os.path.exists(find_drive(team_drive)+team_folder+'\\'+id+'file.txt')
        new_name = os.path.exists(find_drive(team_drive)+team_folder+'\\rename_'+id+'file.txt')
        f = open(find_drive(team_drive)+team_folder+'\\rename_'+id+'file.txt', 'r')
        data = f.read()
        f.close()
        self.assertTrue(old_name==0 and new_name==1 and data=='rename test')
        os.remove(find_drive(team_drive)+team_folder+'\\rename_'+id+'file.txt')

    def test_036_ext_upload_from_local_drive_to_personal_drive(self):
        f = open(os.path.join(os.path.expanduser('~'), 'Downloads', 'upload.txt'), 'w')
        f.write('ext updown test')
        f.close()
        upload(os.path.join(os.path.expanduser('~'), 'Downloads'), 'upload.txt')
        time.sleep(3)
        self.assertTrue(cmp(os.path.join(os.path.expanduser('~'), 'Downloads', 'upload.txt'), find_drive('개인문서함')+r'Downloads\upload.txt'))
        os.remove(os.path.join(os.path.expanduser('~'), 'Downloads', 'upload.txt'))
        shutil.rmtree(find_drive('개인문서함')+'Downloads')

    def test_037_ext_download_from_personal_drive_to_local_drive(self):
        f = open(find_drive('개인문서함')+'download.txt', 'w')
        f.write('ext download test')
        f.close()
        download(find_drive('개인문서함'), 'download.txt')
        time.sleep(3)
        self.assertTrue(cmp(find_drive('개인문서함')+'download.txt', os.path.join(os.path.expanduser('~'), 'Desktop', 'download.txt')))        
        os.remove(find_drive('개인문서함')+'download.txt')
        os.remove(os.path.join(os.path.expanduser('~'), 'Desktop', 'download.txt'))

    def test_038_weblink_in_personal_drive(self):
        f = open(find_drive('개인문서함')+'weblink.txt', 'w')
        f.write('weblink test')
        f.close()
        chrome_result, msedge_result = weblink(web_version, find_drive('개인문서함'), 'weblink.txt')
        self.assertTrue(chrome_result and msedge_result)        
        os.remove(find_drive('개인문서함')+'weblink.txt')

    def test_039_after_export_in_personal_drive(self):
        f = open(find_drive('개인문서함')+'after_export.txt', 'w')
        f.write(now)
        f.close()
        after_export(find_drive('개인문서함'), 'after_export.txt')
        exp_folder_name = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 0)
        print("후결재 일반반출 : "+exp_folder_name)

        compare_doc_export = cmp(find_drive('개인문서함')+'after_export.txt', find_drive('개인문서함')+"DOC_EXPORT\\"+exp_folder_name+'\\after_export.txt')
        
        for i in range(30):
            try:
                compare_local_export = cmp(find_drive('개인문서함')+"DOC_EXPORT\\"+exp_folder_name+'\\after_export.txt', os.path.join(os.path.expanduser('~'), 'Desktop', exp_folder_name, 'after_export.txt'))
                break
            except:
                time.sleep(1)

        self.assertTrue(compare_doc_export and compare_local_export)
        os.remove(find_drive('개인문서함')+'after_export.txt')
        shutil.rmtree(os.path.join(os.path.expanduser('~'), 'Desktop', exp_folder_name))

    def test_040_pre_export_in_personal_drive(self):
        f = open(find_drive('개인문서함')+'pre_export.txt', 'w')
        f.write(now)
        f.close()
        pre_export(web_version, addr, id, pw, find_drive('개인문서함'), 'pre_export.txt') #반출신청 -> 승인 요청(웹뷰알람) -> 자가 승인(웹로그인) -> 내려받기 //크로미움 동작
        exp_folder_name = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 0)       
        exist_doc_export = os.path.exists(find_drive('개인문서함')+"DOC_EXPORT\\"+exp_folder_name+'\\pre_export.txt') #Return True
        compare_export_drive = cmp(find_drive('개인문서함')+'pre_export.txt', find_drive('반출 보안 디스크')+exp_folder_name+'\\pre_export.txt') #cmp -> Return True x permission denied , os.path 동일 실행
        self.assertTrue(exist_doc_export and compare_export_drive) #(True and True)
        os.remove(find_drive('개인문서함')+'pre_export.txt') # 개인문서함 문서 삭제

    def test_041_export_drive_when_cloudoc_login(self):
        export_drive = find_drive('반출 보안 디스크')
        read_permission = False
        write_permission = False
        delete_permission = False
        try:
            f = open(export_drive+recent_file_name(export_drive, 0)+'\\pre_export.txt', 'r')
            f.close()
            read_permission = True
        except PermissionError:
            pass
        try:
            f = open(export_drive+recent_file_name(export_drive, 0)+'\\pre_export.txt', 'w')
            f.close()
            write_permission = True
        except PermissionError:
            pass
        try:
            os.remove(export_drive+recent_file_name(export_drive, 0)+'\\desktop.ini')
            delete_permission = True
        except PermissionError:
            pass
        self.assertTrue(export_drive!=None and read_permission and write_permission==False and delete_permission)

    def test_042_web_export_from_doc_export(self):
        pyautogui.alert("QA_Whitelist 정책을 적용해주세요")
        exp_folder_name = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 1)
        doc_export_file = find_drive('개인문서함')+"DOC_EXPORT\\"+exp_folder_name+'\\after_export.txt'
        chrome_result = web_export(doc_export_file, "chrome")
        msedge_result = web_export(doc_export_file, "msedge")
        self.assertTrue(chrome_result and msedge_result)

    def test_043_secure_export_from_doc_export_to_web(self):
        exp_folder_name = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 0)
        doc_export_file = find_drive('개인문서함')+"DOC_EXPORT\\"+exp_folder_name+'\\pre_export.txt'
        chrome_result = web_export(doc_export_file, "chrome")
        msedge_result = web_export(doc_export_file, "msedge")  
        self.assertFalse(chrome_result and msedge_result)

    def test_044_secure_export_from_export_drive_to_web(self):
        exp_folder_name = recent_file_name(find_drive('개인문서함')+"DOC_EXPORT", 0)
        export_drive_file = find_drive('반출 보안 디스크')+exp_folder_name+'\\pre_export.txt'
        chrome_result = web_export(export_drive_file, "chrome")
        msedge_result = web_export(export_drive_file, "msedge")
        self.assertFalse(chrome_result and msedge_result)

    def test_045_whitelist_policy_excel_file_edit_in_desktop(self):
        try:
            excel_edit(os.path.join(os.path.expanduser('~'), 'Desktop', now), 2)
            edit_fail = False
        except:
            os.system('taskkill /F /IM EXCEL.EXE /T')
            edit_fail = True            
        self.assertTrue(edit_fail)

    def test_046_whitelist_policy_winword_file_edit_in_desktop(self):
        try:
            winword_edit(os.path.join(os.path.expanduser('~'), 'Desktop', now)+'docx', 2)
            edit_fail = False
        except:
            os.system('taskkill /F /IM WINWORD.EXE /T')
            edit_fail = True            
        self.assertTrue(edit_fail)

    def test_047_whitelist_policy_powerpnt_file_edit_in_desktop(self):
        try:
            powerpnt_edit(os.path.join(os.path.expanduser('~'), 'Desktop', now)+'pptx', 2)
            edit_fail = False
        except:
            os.system('taskkill /F /IM POWERPNT.EXE /T')
            edit_fail = True            
        self.assertTrue(edit_fail)

    def test_048_whitelist_save_excel_to_desktop(self):
        try:
            excel_create(os.path.join(os.path.expanduser('~'), 'Desktop', now+"_2"), 1)
            save_fail = False
        except:
            os.system('taskkill /F /IM EXCEL.EXE /T')
            save_fail = True
        self.assertTrue(save_fail)

    def test_049_whitelist_save_winword_to_desktop(self):
        try:
            winword_create(os.path.join(os.path.expanduser('~'), 'Desktop', now+"_2"), 1)
            save_fail = False
        except:
            os.system('taskkill /F /IM WINWORD.EXE /T')
            save_fail = True
        self.assertTrue(save_fail)

    def test_050_whitelist_save_powerpnt_to_desktop(self):
        try:
            powerpnt_create(os.path.join(os.path.expanduser('~'), 'Desktop', now+"_2"), 1)
        except:
            os.system('taskkill /F /IM POWERPNT.EXE /T')
        finally:
            result = os.path.exists(os.path.join(os.path.expanduser('~'), 'Desktop', now+"_2.pptx"))
        self.assertFalse(result)

    def test_051_excel_file_create_in_online_secure_drive(self):      
        excel_create(find_drive('온라인 보안 디스크')+now, 1)
        t1 = excel_read(find_drive('온라인 보안 디스크')+now, 1)
        self.assertEqual(t1, "file write 1st")

    def test_052_excel_file_edit_in_online_secure_drive(self):
        excel_edit(find_drive('온라인 보안 디스크')+now, 2)
        t1 = excel_read(find_drive('온라인 보안 디스크')+now, 1)
        t2 = excel_read(find_drive('온라인 보안 디스크')+now, 2)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_053_winword_file_create_in_online_secure_drive(self):      
        winword_create(find_drive('온라인 보안 디스크')+now, 'file write 1st')
        t1 = winword_read(find_drive('온라인 보안 디스크')+now + '.docx')
        self.assertEqual(t1, "file write 1st\r\r")

    def test_054_winword_file_edit_in_online_secure_drive(self):      
        winword_edit(find_drive('온라인 보안 디스크')+now + '.docx', 'file write 2nd')
        t1 = winword_read(find_drive('온라인 보안 디스크')+now + '.docx')
        self.assertEqual(t1, "file write 1st\rfile write 2nd\r\r")

    def test_055_powerpnt_file_create_in_online_secure_drive(self):      
        powerpnt_create(find_drive('온라인 보안 디스크')+now + '.pptx', 'file write 1st')
        t1 = powerpnt_read(find_drive('온라인 보안 디스크')+now + '.pptx', 0)
        self.assertEqual(t1, "file write 1st")

    def test_056_powerpnt_file_edit_in_online_secure_drive(self):      
        powerpnt_edit(find_drive('온라인 보안 디스크')+now + '.pptx', 'file write 2nd')
        t1 = powerpnt_read(find_drive('온라인 보안 디스크')+now + '.pptx', 0)
        t2 = powerpnt_read(find_drive('온라인 보안 디스크')+now + '.pptx', 1)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_057_rename_file_in_online_secure_drive(self):
        f = open(find_drive('온라인 보안 디스크')+'file_rename.txt', 'w')
        f.write('rename test')
        f.close()
        rename(find_drive('온라인 보안 디스크'), 'file_rename')
        old_name = os.path.exists(find_drive('온라인 보안 디스크')+'file_rename.txt')
        new_name = os.path.exists(find_drive('온라인 보안 디스크')+'rename_file_rename.txt')
        f = open(find_drive('온라인 보안 디스크')+'rename_file_rename.txt', 'r')
        data = f.read()
        f.close()
        self.assertTrue(old_name==0 and new_name==1 and data=='rename test')
        os.remove(find_drive('온라인 보안 디스크')+'rename_file_rename.txt')

    def test_058_delete_file_in_online_secure_drive(self):
        f = open(find_drive('온라인 보안 디스크')+'recyclebin_test.txt', 'w')
        f.write('delte and recycle test')
        f.close()
        delete_file(find_drive('온라인 보안 디스크'), 'recyclebin_test.txt', 0)
        time.sleep(1)

        recyclebin_move = False
        recyclebin_list = list(winshell.recycle_bin()) # returns list of objects of recycle-bin items 
        for value in recyclebin_list:
            if value.original_filename() == find_drive("온라인 보안 디스크")+"recyclebin_test.txt":
                recyclebin_move = True
            elif value.original_filename() == find_drive("온라인 보안 디스크")+"recyclebin_test":
                recyclebin_move = True
            else:
                pass
        self.assertTrue(os.path.exists(find_drive("온라인 보안 디스크")+"recyclebin_test.txt")==0 and os.path.exists(find_drive("온라인 보안 디스크")+"recyclebin_test")==0 and recyclebin_move==1)

    def test_059_restore_file_to_online_secure_drive(self):
        try:
            winshell.undelete(find_drive("온라인 보안 디스크")+"recyclebin_test.txt")
        except:
            winshell.undelete(find_drive("온라인 보안 디스크")+"recyclebin_test")
        recyclebin_restore = True
        drive_file_exist = os.path.exists(find_drive("온라인 보안 디스크")+"recyclebin_test.txt")==1 or os.path.exists(find_drive("온라인 보안 디스크")+"recyclebin_test")==1
        recyclebin_list = list(winshell.recycle_bin()) # returns list of objects of recycle-bin items 
        for value in recyclebin_list:
            if value.original_filename() == find_drive("온라인 보안 디스크")+"recyclebin_test.txt":
                recyclebin_restore = False
            elif value.original_filename() == find_drive("온라인 보안 디스크")+"recyclebin_test":
                recyclebin_restore = False
            else:
                pass
        self.assertTrue(drive_file_exist==1 and recyclebin_restore==1)
        try:
            os.remove(find_drive("온라인 보안 디스크")+"recyclebin_test.txt")
        except:
            os.remove(find_drive("온라인 보안 디스크")+"recyclebin_test")

    def test_060_check_mount_offline_secure_drive(self):
        add_rule('ClouDoc_'+addr, addr)
        modify_rule('ClouDoc_'+addr, 'yes')
        while True:
            try:
                requests.get('http://'+addr).status_code
            except:
                break
        os.startfile(find_drive("개인문서함"))
        time.sleep(3)
        uiautomation.ButtonControl(searchDepth=4, Name='확인').Click()
        if not find_drive('오프라인 보안 디스크') == None:
            offline_drive_mount = True
        else:
            offline_drive_mount = False
        self.assertTrue(offline_drive_mount)

    def test_061_excel_file_create_in_offline_secure_drive(self):      
        excel_create(find_drive('오프라인 보안 디스크')+"offline_"+now, 1)
        t1 = excel_read(find_drive('오프라인 보안 디스크')+"offline_"+now, 1)
        self.assertEqual(t1, "file write 1st")

    def test_062_excel_file_edit_in_offline_secure_drive(self):
        excel_edit(find_drive('오프라인 보안 디스크')+"offline_"+now, 2)
        t1 = excel_read(find_drive('오프라인 보안 디스크')+"offline_"+now, 1)
        time.sleep(1)
        t2 = excel_read(find_drive('오프라인 보안 디스크')+"offline_"+now, 2)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_063_winword_file_create_in_offline_secure_drive(self):      
        winword_create(find_drive('오프라인 보안 디스크')+"offline_"+now, 'file write 1st')
        t1 = winword_read(find_drive('오프라인 보안 디스크')+"offline_"+now + '.docx')
        self.assertEqual(t1, "file write 1st\r\r")

    def test_064_winword_file_edit_in_offline_secure_drive(self):      
        winword_edit(find_drive('오프라인 보안 디스크')+"offline_"+now + '.docx', 'file write 2nd')
        t1 = winword_read(find_drive('오프라인 보안 디스크')+"offline_"+now + '.docx')
        self.assertEqual(t1, "file write 1st\rfile write 2nd\r\r")

    def test_065_powerpnt_file_create_in_offline_secure_drive(self):
        powerpnt_create(find_drive('오프라인 보안 디스크')+"offline_"+now + '.pptx', 'file write 1st')
        time.sleep(1)
        t1 = powerpnt_read(find_drive('오프라인 보안 디스크')+"offline_"+now + '.pptx', 0)
        time.sleep(1)
        self.assertEqual(t1, "file write 1st")

    def test_066_powerpnt_file_edit_in_offline_secure_drive(self):      
        powerpnt_edit(find_drive('오프라인 보안 디스크')+"offline_"+now + '.pptx', 'file write 2nd')
        time.sleep(1)
        t1 = powerpnt_read(find_drive('오프라인 보안 디스크')+"offline_"+now + '.pptx', 0)
        time.sleep(1)
        t2 = powerpnt_read(find_drive('오프라인 보안 디스크')+"offline_"+now + '.pptx', 1)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_067_rename_file_in_offline_secure_drive(self):
        f = open(find_drive('오프라인 보안 디스크')+'file_rename.txt', 'w')
        f.write('rename test')
        f.close()
        rename(find_drive('오프라인 보안 디스크'), 'file_rename')
        old_name = os.path.exists(find_drive('오프라인 보안 디스크')+'file_rename.txt')
        new_name = os.path.exists(find_drive('오프라인 보안 디스크')+'rename_file_rename.txt')
        f = open(find_drive('오프라인 보안 디스크')+'rename_file_rename.txt', 'r')
        data = f.read()
        f.close()
        self.assertTrue(old_name==0 and new_name==1 and data=='rename test')
        os.remove(find_drive('오프라인 보안 디스크')+'rename_file_rename.txt')

    def test_068_upload_offline_secure_drive(self):
        modify_rule('ClouDoc_'+addr, 'no')
        while True:
            if addr == "192.168.1.6":
                try:
                    if requests.get('http://'+addr+':23899').status_code == 200:
                        break
                    else:
                        pass
                except:
                    pass
            else:
                try:
                    if requests.get('http://'+addr).status_code == 200:
                        break
                    else:
                        pass
                except:
                    pass
        
        time.sleep(3)
        uiautomation.ButtonControl(searchDepth=2, AutomationId='1').Click()
        time.sleep(0.5)
        uiautomation.ButtonControl(searchDepth=2, AutomationId='1').Click()
        uiautomation.ButtonControl(searchDepth=2, Name='....').Click()
        uiautomation.TreeItemControl(searchDepth=5, RegexName='개인문서함.*').Click()
        uiautomation.ButtonControl(searchDepth=3, AutomationId='1').Click()
        uiautomation.ButtonControl(searchDepth=2, AutomationId='1').Click()
        uiautomation.ButtonControl(searchDepth=2, AutomationId='2').Click()

        a = os.path.exists(find_drive('개인문서함')+"offline_"+now + '.docx')
        b = os.path.exists(find_drive('개인문서함')+"offline_"+now + '.xlsx')
        c = os.path.exists(find_drive('개인문서함')+"offline_"+now + '.pptx')
        
        for i in range(100):
            if find_drive('오프라인 보안 디스크') == None:
                offline_drive_unmount = True
                break
            else:
                offline_drive_unmount = False
                time.sleep(1)
        
        self.assertTrue(a and b and c and offline_drive_unmount)

    def test_069_internal_network_allowed_IP_bands(self):
        pyautogui.alert("네트워크락 Default_QA 정책 적용해주세요")
        s_100 = requests.get('http://192.168.1.100').status_code
        s_google = requests.get('https://www.google.com').status_code
        self.assertTrue(s_100==200 and s_google==200)

    def test_070_internal_network_rejected_IP_bands(self):
        try:
            s_naver = requests.get('https://www.naver.com').status_code
        except:
            s_naver = 408
        try:
            s_daum = requests.get('https://www.daum.net').status_code
        except:
            s_daum = 408
        self.assertTrue(s_naver==408 and s_daum==408)

    def test_071_switch_to_external_network_mode(self):
        pyperclip.copy("change networklock externel mode")
        os.startfile(find_drive('개인문서함')+'ㅎ.networklock.xlsx')
        time.sleep(3)
        for i in range(60):
            if "ㅎ.networklock.xlsx - Excel" in pygetwindow.getAllTitles():
                break
            else:
                time.sleep(1)
        pyautogui.hotkey('ctrl', 'shift', 'alt', 'f10')
        uiautomation.ButtonControl(searchDepth=2, AutomationId='1').Click()
        uiautomation.ButtonControl(searchDepth=2, AutomationId='7089').Click()
        time.sleep(60)
        self.assertEqual(pyperclip.paste(), '')

    def test_072_external_network_unmount_drive(self):
        p_drive = find_drive('개인문서함')
        t_drive = find_drive(team_drive)
        o_drive = find_drive('온라인 보안 디스크')
        self.assertTrue(p_drive == t_drive == o_drive == None)

    def test_073_external_network_rejected_IP_bands(self):
        try:
            s_100 = requests.get('http://192.168.1.100').status_code
        except:
            s_100 = 408
        try:
            s_nate = requests.get('https://www.nate.com').status_code
        except:
            s_nate = 408
        self.assertTrue(s_100==408 and s_nate==408)

    def test_074_external_network_allowed_IP_bands(self):
        s_naver = requests.get('https://www.naver.com').status_code
        s_google = requests.get('https://www.google.com').status_code
        self.assertTrue(s_naver==200 and s_google==200)

    def test_075_excel_file_create_in_export_secure_drive(self):      
        excel_create(find_drive('반출 보안 디스크')+now, 1)
        t1 = excel_read(find_drive('반출 보안 디스크')+now, 1)
        self.assertEqual(t1, "file write 1st")

    def test_076_excel_file_edit_in_export_secure_drive(self):
        excel_edit(find_drive('반출 보안 디스크')+now, 2)
        t1 = excel_read(find_drive('반출 보안 디스크')+now, 1)
        t2 = excel_read(find_drive('반출 보안 디스크')+now, 2)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_077_winword_file_create_in_export_secure_drive(self):      
        winword_create(find_drive('반출 보안 디스크')+now, 'file write 1st')
        t1 = winword_read(find_drive('반출 보안 디스크')+now + '.docx')
        self.assertEqual(t1, "file write 1st\r\r")

    def test_078_winword_file_edit_in_export_secure_drive(self):      
        winword_edit(find_drive('반출 보안 디스크')+now + '.docx', 'file write 2nd')
        t1 = winword_read(find_drive('반출 보안 디스크')+now + '.docx')
        self.assertEqual(t1, "file write 1st\rfile write 2nd\r\r")

    def test_079_powerpnt_file_create_in_export_secure_drive(self):      
        powerpnt_create(find_drive('반출 보안 디스크')+now + '.pptx', 'file write 1st')
        t1 = powerpnt_read(find_drive('반출 보안 디스크')+now + '.pptx', 0)
        self.assertEqual(t1, "file write 1st")

    def test_080_powerpnt_file_edit_in_export_secure_drive(self):      
        powerpnt_edit(find_drive('반출 보안 디스크')+now + '.pptx', 'file write 2nd')
        t1 = powerpnt_read(find_drive('반출 보안 디스크')+now + '.pptx', 0)
        t2 = powerpnt_read(find_drive('반출 보안 디스크')+now + '.pptx', 1)
        self.assertTrue(t1=="file write 1st" and t2=="file write 2nd")

    def test_081_rename_file_in_export_secure_drive(self):
        f = open(find_drive('반출 보안 디스크')+'file_rename.txt', 'w')
        f.write('rename test')
        f.close()
        rename(find_drive('반출 보안 디스크'), 'file_rename')
        old_name = os.path.exists(find_drive('반출 보안 디스크')+'file_rename.txt')
        new_name = os.path.exists(find_drive('반출 보안 디스크')+'rename_file_rename.txt')
        f = open(find_drive('반출 보안 디스크')+'rename_file_rename.txt', 'r')
        data = f.read()
        f.close()
        self.assertTrue(old_name==0 and new_name==1 and data=='rename test')
        os.remove(find_drive('반출 보안 디스크')+'rename_file_rename.txt')

    def test_082_internal_network_mount_drive(self):
        pyautogui.hotkey('ctrl', 'shift', 'alt', 'f10')
        uiautomation.ButtonControl(searchDepth=2, AutomationId='1').Click()
        time.sleep(10)
        p_drive_check = find_drive('개인문서함') != None
        t_drive_check = find_drive(team_drive) != None
        o_drive_check = find_drive('온라인 보안 디스크') != None
        self.assertTrue(p_drive_check and t_drive_check and o_drive_check)
        pyautogui.alert("네트워크락 정책을 해제하세요")

# %%
window=tkinter.Tk()
window.title("NETID_SQA_TEAM")
window.geometry("480x265+640+360")
window.resizable(True, True)
testcaseid=[]
row_num = 0
CheckVariety = {}
Checkbutton = {}

def ok():
    for i in range(82):
        if i==20 and CheckVariety[i].get()==1:
            testcaseid.extend([21,22,23,24,25,26,27,28,29])
        elif i==29 and CheckVariety[i].get()==1:
            testcaseid.extend([30, 31, 32, 33])
        elif i==59 and CheckVariety[i].get()==1:
            testcaseid.extend([60, 61, 62, 63, 64, 65, 66, 67, 68])
        elif CheckVariety[i].get()==1:
            testcaseid.append(i+1)
    window.destroy()

def basic_select():
    for i in range(68):
        Checkbutton[i].select()

def networklock_select():
    for i in range(68, 82):
        Checkbutton[i].select()

def toggle_all():
    for i in range(82):
        Checkbutton[i].toggle()
    Checkbutton[29].toggle()

def settings():
    window2=tkinter.Toplevel()
    window2.grab_set()
    window2.title("설정")
    window2.geometry("270x230+740+390")
    window2.resizable(False, False)

    radioValue = tkinter.IntVar()

    def radCall():
        radSel = radioValue.get()
        if radSel == 2:
            entry_1.delete(0, 20)
            entry_1.insert(0, '192.168.1.183')
        elif radSel == 3:
            entry_1.delete(0, 20)
            entry_1.insert(0, '192.168.3.81')

    label_0=tkinter.Label(window2, text="web-version")
    label_0.grid(row=0, column=0)
    radio_0 = tkinter.Radiobutton(window2, text='2.0', variable=radioValue, value=2, command=radCall)
    radio_0.place(x=100, y=0)
    radio_1 = tkinter.Radiobutton(window2, text='3.0', variable=radioValue, value=3, command=radCall)
    radio_1.place(x=150, y=0)

    label_1=tkinter.Label(window2, text="server-addr")
    label_1.grid(row=1, column=0)
    entry_1=tkinter.Entry(window2)
    entry_1.grid(row=1, column=1)

    label_2=tkinter.Label(window2, text="dwMajorVersion")
    label_2.grid(row=2, column=0)
    entry_2=tkinter.Entry(window2)
    entry_2.grid(row=2, column=1)
    
    label_3=tkinter.Label(window2, text="dwMinorVersion")
    label_3.grid(row=3, column=0)
    entry_3=tkinter.Entry(window2)
    entry_3.grid(row=3, column=1)

    label_4=tkinter.Label(window2, text="team_drive")
    label_4.grid(row=4, column=0)
    entry_4=tkinter.Entry(window2)
    entry_4.grid(row=4, column=1)

    label_5=tkinter.Label(window2, text="team_folder")
    label_5.grid(row=5, column=0)
    entry_5=tkinter.Entry(window2)
    entry_5.grid(row=5, column=1)

    label_6=tkinter.Label(window2, text="ID")
    label_6.grid(row=6, column=0)
    entry_6=tkinter.Entry(window2)
    entry_6.grid(row=6, column=1)

    label_7=tkinter.Label(window2, text="Password")
    label_7.grid(row=7, column=0)
    entry_7=tkinter.Entry(window2)
    entry_7.grid(row=7, column=1)

    config = configparser.ConfigParser()
    try:
        config.read('config.ini', encoding='cp949')
        if config['test_conf']['web_version'] == '2':
            radio_0.select()
        elif config['test_conf']['web_version'] == '3':
            radio_1.select()
        entry_1.insert(0, config['test_conf']['addr'])
        entry_2.insert(0, config['test_conf']['dwMajorVersion'])
        entry_3.insert(0, config['test_conf']['dwMinorVersion'])
        entry_4.insert(0, config['test_conf']['team_drive'])
        entry_5.insert(0, config['test_conf']['team_folder'])
        entry_6.insert(0, config['test_conf']['id'])
        entry_7.insert(0, config['test_conf']['pw'])
    except:
        radio_1.select()
        entry_1.insert(0, '192.168.3.81')
        entry_2.insert(0, '3')
        entry_3.insert(0, '141')
        entry_4.insert(0, '부서문서함')
        entry_5.insert(0, '품질보증팀')
        entry_6.insert(0, 'autotester3')
        entry_7.insert(0, 'netid000')

    def conf_fix():
        config = configparser.ConfigParser()
        config['test_conf'] = {}
        config['test_conf']['web_version'] = str(radioValue.get())
        config['test_conf']['addr'] = entry_1.get()
        config['test_conf']['dwMajorVersion'] = entry_2.get()
        config['test_conf']['dwMinorVersion'] = entry_3.get()
        config['test_conf']['team_drive'] = entry_4.get()
        config['test_conf']['team_folder'] = entry_5.get()
        config['test_conf']['id'] = entry_6.get()
        config['test_conf']['pw'] = entry_7.get()
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        window2.destroy()
    ini_fix=tkinter.Button(window2, overrelief="solid", width=15, command=conf_fix, repeatdelay=1000, repeatinterval=100, text='확인').place(x=80, y=190)

for i in range(82):
    CheckVariety[i] = tkinter.IntVar()
    if i<10:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num, column=0)
        row_num = row_num + 1

    elif i<20:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-10, column=1)
        row_num = row_num + 1

    elif i<29:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[20])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-20, column=2)
        row_num = row_num + 1
    
    elif i==29:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[29])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-20, column=2)
        row_num = row_num + 1

    elif i<33:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[29])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-30, column=3)
        row_num = row_num + 1
    
    elif i<40:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-30, column=3)
        row_num = row_num + 1

    elif i<50:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-40, column=4)
        row_num = row_num + 1

    elif i<60:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-50, column=5)
        row_num = row_num + 1

    elif i<68:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[59])
        Checkbutton[i].select()
        Checkbutton[i].grid(row=row_num-60, column=6)
        row_num = row_num + 1

    elif i<70:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].deselect()
        Checkbutton[i].grid(row=row_num-60, column=6)
        row_num = row_num + 1
    
    elif i<80:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].deselect()
        Checkbutton[i].grid(row=row_num-70, column=7)
        row_num = row_num + 1
    
    else:
        Checkbutton[i] = tkinter.Checkbutton(window, text=i+1, variable=CheckVariety[i])
        Checkbutton[i].deselect()
        Checkbutton[i].grid(row=row_num-80, column=8)
        row_num = row_num + 1

button0 = tkinter.Button(window, overrelief="solid", width=15, command=settings, repeatdelay=1000, repeatinterval=100, text='settings').place(x=350, y=100)
button = tkinter.Button(window, overrelief="solid", width=15, command=basic_select, repeatdelay=1000, repeatinterval=100, text='basic').place(x=350, y=130)
button2 = tkinter.Button(window, overrelief="solid", width=15, command=networklock_select, repeatdelay=1000, repeatinterval=100, text='networklock').place(x=350, y=160)
button3 = tkinter.Button(window, overrelief="solid", width=15, command=toggle_all, repeatdelay=1000, repeatinterval=100, text='toggle').place(x=350, y=190)
button4 = tkinter.Button(window, overrelief="solid", width=15, command=ok, repeatdelay=1000, repeatinterval=100, text='test_run').place(x=350, y=220)

window.mainloop()
    
def suite():
    suite = unittest.TestSuite()
    for testcase in testcaseid:
        suite.addTest(Client_Test(testid_dic[testcase]))
    return suite

if __name__ == '__main__':
    try:
        major_v = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\NetID\PlusDrive', 'dwMajorVersion')
        minor_v = reg_check(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\NetID\PlusDrive', 'dwMinorVersion')
    except FileNotFoundError:
        pyautogui.alert("클라우독이 정상 설치되지 않았습니다. 테스트를 종료합니다.")
        sys.exit()

    runner = HtmlTestRunner.HTMLTestRunner(output='ReportTest', report_title='Client_'+str(major_v)+'.'+str(minor_v)+'_'+platform.system()+platform.release()+'_'+platform.machine()+'_Test Results')
    runner.run(suite())

if testcaseid != []:
    test_result = recent_file_name(os.getcwd()+r"\ReportTest", 0)
    os.startfile(os.getcwd()+"\\ReportTest\\"+test_result)

os.system('pause')