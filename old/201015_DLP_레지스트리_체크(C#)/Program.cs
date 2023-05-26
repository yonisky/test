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
            bool Reg(string path, string name, string data)
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
                                Console.WriteLine(name + "에 npDevFlt가 등록되어 있습니다.");
                                result = true;
                            }
                            else
                            {
                                Console.WriteLine(name + "에 npDevFlt 값이 존재하지 않습니다.");
                                result = false;
                            }
                            break;

                        case RegistryValueKind.String:
                            Console.WriteLine(name + " 레지스트리 데이터 값은 " + rk.GetValue(name) + "입니다.");
                            if ((string)rk.GetValue(name) == data)
                                result = true;
                            else
                                result = false;
                            break;

                        default:
                            break;
                    }

                }
                else
                    Console.WriteLine(name + "값이 존재하지 않습니다.");
                return result;

            }

            bool x;
            System.Console.WriteLine("<시리얼&LPT포트>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{4d36e978-e325-11ce-bfc1-08002be10318}", "UpperFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<모뎀>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{4d36e96d-e325-11ce-bfc1-08002be10318}", "UpperFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<USB>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{36fc9e60-c465-11cf-8056-444553540000}", "LowerFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<PCMCIA 장치>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{4d36e971-e325-11ce-bfc1-08002be10318}", "LowerFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<FireWire(1394) 저장 장치1>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{6bdd1fc1-810f-11d0-bec7-08002be2092f}", "LowerFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<FireWire(1394) 저장 장치2>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{D48179BE-EC20-11D1-B6B8-00C04FA372A7}", "LowerFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<적외선 포트 장치>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{6bdd1fc5-810f-11d0-bec7-08002be2092f}", "LowerFilters", "npDevFlt");
            System.Console.WriteLine(x);

            System.Console.WriteLine("<블루투스>");
            x = Reg(@"SYSTEM\CurrentControlSet\Control\Class\{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}", "LowerFilters", "npDevFlt");
            System.Console.WriteLine(x);

            Console.ReadLine();
        }
    }
}
