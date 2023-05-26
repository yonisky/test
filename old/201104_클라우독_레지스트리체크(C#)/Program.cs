using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Win32;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            bool HKLM_Reg(string path, string name, string data)
            {
                bool result = false;
                RegistryKey rk = Registry.LocalMachine.OpenSubKey(@path);
                string[] valueNames = rk.GetValueNames();
                if (Array.Exists(valueNames, element => element == name))
                {
                    RegistryValueKind rvk = rk.GetValueKind(name);
                    switch (rvk)
                    {
                        case RegistryValueKind.MultiString:
                            string[] values = (string[])rk.GetValue(name);
                            for (int i = 0; i < values.Length; i++)
                            {
                                if (i != 0) Console.Write(",");
                                Console.Write("{0}", values[i]);
                                if (i == values.Length - 1) Console.WriteLine();
                            }
                            if (Array.Exists(values, element => element == data))
                            {
                                Console.WriteLine("Pass : " + name + "에 npDevFlt가 등록되어 있습니다.");
                                result = true;
                            }
                            else
                            {
                                Console.WriteLine("Fail : " + "npDevFlt 값이 존재하지 않습니다.");
                                result = false;
                            }
                            rk.Close();
                            break;

                        case RegistryValueKind.String:
                            if ((string)rk.GetValue(name) == data)
                            {
                                result = true;
                                Console.WriteLine("Pass : "+name + " 레지스트리 데이터 값은 " + rk.GetValue(name) + "입니다.");
                            }                                
                            else
                            {
                                result = false;
                                Console.WriteLine("Fail : " + name + " 레지스트리 데이터 값은 " + rk.GetValue(name) + "입니다.");
                            }
                            rk.Close();
                            break;

                        default:
                            break;
                    }
                }
                else
                    Console.WriteLine("Fail : "+name+"값이 존재하지 않습니다.");
                return result;
            }

            bool HKLM_Reg_Dword(string path, string name, int data)
            {
                bool result = false;
                RegistryKey rk = Registry.LocalMachine.OpenSubKey(@path);
                int rk_vaule = (int)rk.GetValue(name);
                string[] valueNames = rk.GetValueNames();
                if (Array.Exists(valueNames, element => element == name))
                {
                    if(rk_vaule == data)
                    {
                        Console.WriteLine("Pass : "+name + "에 "+data+"값이 등록되어 있습니다.");
                        result = true;
                    }
                    else
                    {
                        Console.WriteLine("Fail : "+name + "에 "+rk_vaule+ "값이 등록되어 있습니다");
                        result = false;
                    }
                }
                else
                    Console.WriteLine(name + "값이 존재하지 않습니다.");
                return result;
            }

            bool HKCR_Reg(string path, string name, string data)
            {
                bool result = false;
                RegistryKey rk = Registry.ClassesRoot.OpenSubKey(@path);
                string[] valueNames = rk.GetValueNames();
                if (Array.Exists(valueNames, element => element == name))
                {
                    RegistryValueKind rvk = rk.GetValueKind(name);
                    switch (rvk)
                    {
                        case RegistryValueKind.MultiString:
                            string[] values = (string[])rk.GetValue(name);
                            for (int i = 0; i < values.Length; i++)
                            {
                                if (i != 0) Console.Write(",");
                                Console.Write("{0}", values[i]);
                                if (i == values.Length - 1) Console.WriteLine();
                            }
                            if (Array.Exists(values, element => element == data))
                            {
                                Console.WriteLine("Pass : " + name + "에 npDevFlt가 등록되어 있습니다.");
                                result = true;
                            }
                            else
                            {
                                Console.WriteLine("Fail : " + "npDevFlt 값이 존재하지 않습니다.");
                                result = false;
                            }
                            rk.Close();
                            break;

                        case RegistryValueKind.String:
                            if ((string)rk.GetValue(name) == data)
                            {
                                result = true;
                                Console.WriteLine("Pass : " + name + " 레지스트리 데이터 값은 " + rk.GetValue(name) + "입니다.");
                            }
                            else
                            {
                                result = false;
                                Console.WriteLine("Fail : " + name + " 레지스트리 데이터 값은 " + rk.GetValue(name) + "입니다.");
                            }
                            rk.Close();
                            break;

                        default:
                            break;
                    }
                }
                else
                    Console.WriteLine("Fail : " + name + "값이 존재하지 않습니다.");
                return result;
            }


            bool x;

            Console.Write("dwMajorVersion을 입력하세요 : ");
            string s_major = Console.ReadLine();
            int i_major = Convert.ToInt32(s_major);

            Console.Write("dwMinorVersion을 입력하세요 : ");
            string s_minor = Console.ReadLine();
            int i_minor = Convert.ToInt32(s_minor);
            System.Console.WriteLine();

            System.Console.WriteLine("<dwMajorVersion>");
            x = HKLM_Reg_Dword(@"SOFTWARE\NetID\PlusDrive", "dwMajorVersion", i_major);
            System.Console.WriteLine(x);

            System.Console.WriteLine("<dwMajorVersion>");
            x = HKLM_Reg_Dword(@"SOFTWARE\NetID\PlusDrive", "dwMinorVersion", i_minor);
            System.Console.WriteLine(x);

            System.Console.WriteLine("<InstallPath>");
            x = HKLM_Reg(@"SOFTWARE\NetID\PlusDrive", "InstallPath", @"C:\Program Files\NetID\PlusDrive");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<ProductName>");
            x = HKLM_Reg(@"SOFTWARE\NetID\PlusDrive", "ProductName", "ClouDoc");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<npStartup>");
            x = HKLM_Reg(@"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "npStartup", @"C:\Program Files\NetID\PlusDrive\npStartup.exe");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<InstallLocation>");
            x = HKLM_Reg(@"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\ClouDoc", "InstallLocation", @"C:\Program Files\NetID\PlusDrive");
            System.Console.WriteLine(x);

            Console.ReadLine();

        }
    }
}
