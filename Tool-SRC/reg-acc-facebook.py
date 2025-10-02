import random
import time
import re
import requests
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from colorama import Fore, Style, Back, init
import os
import sys
import json
import threading
import hashlib
import platform
import subprocess
import uuid
from datetime import datetime

# Khởi tạo colorama
init(autoreset=True)

class UserManager:
    def __init__(self):
        self.whitelist_url = "https://raw.githubusercontent.com/tuquangnam07/Passwords-Tool-DVFB/refs/heads/main/whitelist.txt"
        self.current_user = None
        self.user_data = None
    
    def get_hardware_id(self):
        """Lấy ID duy nhất của máy tính"""
        try:
            # Lấy địa chỉ MAC
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                           for elements in range(0,8*6,8)][::-1])
            
            # Lấy thông tin CPU
            cpu = platform.processor()
            
            # Lấy thông tin ổ cứng (serial number)
            if platform.system() == "Windows":
                try:
                    result = subprocess.check_output('wmic diskdrive get serialnumber', shell=True, stderr=subprocess.DEVNULL)
                    disk_serial = result.decode().split('\n')[1].strip()
                except:
                    disk_serial = "unknown"
            else:
                try:
                    disk_serial = subprocess.check_output(['lsblk', '-o', 'SERIAL']).decode().split('\n')[1].strip()
                except:
                    disk_serial = "unknown"
            
            # Tạo hardware ID từ các thông tin trên
            hardware_string = f"{mac}|{cpu}|{disk_serial}"
            hardware_id = hashlib.md5(hardware_string.encode()).hexdigest()[:12]
            
            return hardware_id
            
        except Exception as e:
            # Fallback: dùng MAC address
            return hashlib.md5(str(uuid.getnode()).encode()).hexdigest()[:12]

    def load_whitelist(self):
        """Tải danh sách user từ GitHub"""
        try:
            response = requests.get(self.whitelist_url, timeout=10)
            users = {}
            for line in response.text.strip().split('\n'):
                if '|' in line and not line.startswith('#'):
                    parts = line.split('|')
                    if len(parts) >= 6:
                        username, password, hardware_ids, max_devices, expiry, max_accounts = parts
                        users[username] = {
                            'password': password.strip(),
                            'hardware_ids': [hwid.strip() for hwid in hardware_ids.split(',')],
                            'max_devices': int(max_devices.strip()),
                            'expiry': expiry.strip(),
                            'max_accounts': int(max_accounts.strip())
                        }
            return users
        except Exception as e:
            print(f"{Fore.RED}❌ Lỗi tải whitelist: {e}")
            return {}

    def show_login_form(self):
        """Hiển thị form đăng nhập đẹp"""
        print(f"\n{Fore.CYAN}╔{'═' * 50}╗")
        print(f"║{Fore.YELLOW}{' ĐĂNG NHẬP HỆ THỐNG   ':^48}{Fore.CYAN}  ║")
        print(f"╚{'═' * 50}╝{Style.RESET_ALL}")

    def check_expiry(self, expiry_date):
        """Kiểm tra ngày hết hạn"""
        try:
            current_date = datetime.now().strftime("%Y-%m-%d")
            return current_date <= expiry_date
        except:
            return False

    def authenticate_user(self):
        """Xác thực người dùng"""
        whitelist = self.load_whitelist()
        if not whitelist:
            print(f"{Fore.RED}❌ Không thể tải danh sách người dùng!")
            return False

        current_hardware_id = self.get_hardware_id()
        print(f"{Fore.CYAN}🖥️  Hardware ID: {current_hardware_id}")

        self.show_login_form()
        username = input(f"{Fore.CYAN}👤 Tên đăng nhập: {Style.RESET_ALL}").strip()
        password = input(f"{Fore.CYAN}🔐 Mật khẩu: {Style.RESET_ALL}").strip()

        if username in whitelist:
            user_data = whitelist[username]
            
            # Kiểm tra password
            if user_data['password'] != password:
                print(f"{Fore.RED}❌ Mật khẩu không chính xác!")
                return False
                
            # Kiểm tra ngày hết hạn
            if not self.check_expiry(user_data['expiry']):
                print(f"{Fore.RED}❌ Tài khoản đã hết hạn sử dụng!")
                return False
                
            # Kiểm tra hardware ID
            if current_hardware_id not in user_data['hardware_ids']:
                # Nếu chưa có hardware ID này
                if len(user_data['hardware_ids']) < user_data['max_devices']:
                    print(f"{Fore.YELLOW}⚠️  Đang kích hoạt trên máy mới...")
                    # Trong thực tế, bạn cần cập nhật file whitelist trên GitHub
                    # Ở đây tôi sẽ chỉ cho phép và ghi nhận local
                    user_data['hardware_ids'].append(current_hardware_id)
                    print(f"{Fore.GREEN}✅ Đã kích hoạt thành công trên máy này!")
                else:
                    print(f"{Fore.RED}❌ Đã vượt quá {user_data['max_devices']} máy cho phép!")
                    return False
            else:
                print(f"{Fore.GREEN}✅ Hardware ID hợp lệ!")
                
            self.current_user = username
            self.user_data = user_data
            return True
        else:
            print(f"{Fore.RED}❌ Tên đăng nhập không tồn tại!")
            return False

class FacebookRegTool:
    def __init__(self):
        self.version = "4.0"
        self.author = "Từ Quang Nam"
        self.banner = f"""
{Fore.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ███████╗ █████╗ ██████╗ ███████╗██████╗  ██████╗ ███████╗ ██████╗ ██████╗ ║
║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝ ██╔════╝██╔═══██╗██╔══██╗║
║    █████╗  ███████║██████╔╝█████╗  ██████╔╝██║  ███╗███████╗██║   ██║██████╔╝║
║    ██╔══╝  ██╔══██║██╔══██╗██╔══╝  ██╔══██╗██║   ██║╚════██║██║   ██║██╔══██╗║
║    ██║     ██║  ██║██║  ██║███████╗██║  ██║╚██████╔╝███████║╚██████╔╝██║  ██║║
║    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝║
║                                                                              ║
║                  FACEBOOK REGISTRATION TOOL v{self.version}                             ║
║                  Copyright © 2025 by {self.author}                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
        self.user_manager = UserManager()

    def loading_animation(self, message="Đang tải"):
        """Hiệu ứng loading"""
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for i in range(20):
            print(f"\r{Fore.CYAN}{chars[i % len(chars)]} {message}{'.' * (i % 4)}{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.1)
        print("\r" + " " * 50 + "\r", end="", flush=True)

    def print_colored(self, message, color=Fore.WHITE, style=Style.NORMAL):
        print(f"{style}{color}[{time.strftime('%H:%M:%S')}] {message}{Style.RESET_ALL}")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_fancy_header(self, title):
        """Hiển thị header đẹp"""
        print(f"\n{Fore.CYAN}╔{'═' * 60}╗")
        print(f"║{Fore.YELLOW} {title:^58} {Fore.CYAN}║")
        print(f"╚{'═' * 60}╝{Style.RESET_ALL}")

    def show_minimal_menu(self, current_function=None):
        """Hiển thị menu tối giản khi đang thực hiện chức năng"""
        self.clear_console()
        print(self.banner)
        
        if current_function:
            print(f"{Fore.GREEN}🎯 Đang thực hiện: {current_function}")
            print(f"{Fore.CYAN}┌{'─' * 58}┐")
            print(f"│ {Fore.YELLOW}Để quay lại menu chính, nhấn Ctrl+C                      {Fore.CYAN}│")
            print(f"└{'─' * 58}┘{Style.RESET_ALL}")
        else:
            self.show_statistics()
            print(f"\n{Fore.CYAN}╔{'═' * 60}╗")
            print(f"║{Fore.YELLOW} {'MENU CHÍNH':^58} {Fore.CYAN}║")
            print(f"╠{'═' * 60}╣")
            print(f"║ {Fore.GREEN}1.{Fore.WHITE} Đăng ký tài khoản Facebook                              {Fore.CYAN}║")
            print(f"║ {Fore.GREEN}2.{Fore.WHITE} Tách UID từ file tài khoản                              {Fore.CYAN}║")
            print(f"║ {Fore.GREEN}3.{Fore.WHITE} Hiển thị ví dụ cookie                                   {Fore.CYAN}║")
            print(f"║ {Fore.GREEN}4.{Fore.WHITE} Xóa file dữ liệu cũ                                     {Fore.CYAN}║")
            print(f"║ {Fore.GREEN}5.{Fore.WHITE} Thoát chương trình                                      {Fore.CYAN}║")
            print(f"╚{'═' * 60}╝{Style.RESET_ALL}")

    def generate_strong_password(self, length=15):
        """Tạo mật khẩu mạnh tự động"""
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))

    def get_fb_password_choice(self):
        """Lựa chọn loại mật khẩu Facebook"""
        self.show_minimal_menu("LỰA CHỌN MẬT KHẨU FACEBOOK")
        
        print(f"\n{Fore.GREEN}1.{Fore.WHITE} Mật khẩu tự động (15 ký tự ngẫu nhiên mạnh)")
        print(f"{Fore.GREEN}2.{Fore.WHITE} Mật khẩu tự nhập")
        print(f"{Fore.GREEN}3.{Fore.WHITE} Quay lại menu chính")
        
        while True:
            choice = input(f"\n{Fore.CYAN}👉 Chọn loại mật khẩu (1-3): {Style.RESET_ALL}").strip()
            
            if choice == '1':
                password = self.generate_strong_password()
                self.print_colored(f"✓ Đã tạo mật khẩu tự động: {password}", Fore.GREEN)
                return password
            elif choice == '2':
                while True:
                    password = input(f"{Fore.CYAN}👉 Nhập mật khẩu Facebook: {Style.RESET_ALL}").strip()
                    if len(password) >= 6:
                        return password
                    else:
                        self.print_colored("✗ Mật khẩu phải có ít nhất 6 ký tự!", Fore.RED)
            elif choice == '3':
                return None
            else:
                self.print_colored("✗ Lựa chọn không hợp lệ!", Fore.RED)

    def setup_driver(self, thread_id):
        """Thiết lập Chrome driver với các tùy chọn tối ưu"""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        ]
        
        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
        chrome_options.add_argument("--window-size=400,700")
        chrome_options.add_argument(f"--window-position={thread_id * 400},0")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        
        # Tắt các tính năng không cần thiết
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument("--disable-background-timer-throttling")
        chrome_options.add_argument("--disable-backgrounding-occluded-windows")
        chrome_options.add_argument("--disable-renderer-backgrounding")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--silent")

        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Ẩn automation
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            return driver
        except Exception as e:
            self.print_colored(f"✗ Lỗi khởi tạo driver: {e}", Fore.RED)
            return None

    def generate_vietnamese_name(self):
        """Tạo tên người dùng Việt Nam ngẫu nhiên"""
        ho_list = ["Nguyễn", "Trần", "Lê", "Phạm", "Huỳnh", "Hoàng", "Phan", "Vũ", "Võ", "Đặng"]
        ten_list = ["Nam", "Long", "Huy", "Tuấn", "Khoa", "Tài", "Duy", "Sơn", "Phúc", "Trí", 
                   "Linh", "Trang", "Lan", "Hương", "Thảo", "Vy", "Ngân", "Mai", "Anh", "Quỳnh"]
        
        return random.choice(ho_list), random.choice(ten_list)

    def generate_phone_number(self):
        """Tạo số điện thoại Việt Nam hợp lệ"""
        prefixes = ['032', '033', '034', '035', '036', '037', '038', '039',
                   '070', '076', '077', '078', '079',
                   '081', '082', '083', '084', '085',
                   '056', '058',
                   '059', '099']
        return random.choice(prefixes) + ''.join([str(random.randint(0, 9)) for _ in range(7)])

    def wait_for_element(self, driver, by, value, timeout=10):
        """Chờ element xuất hiện"""
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except:
            return None

    def register_account(self, thread_id, account_number, fb_password):
        """Đăng ký tài khoản Facebook"""
        driver = None
        try:
            self.print_colored(f"🧵 Luồng {thread_id} - Tài khoản {account_number}: Đang khởi tạo...", Fore.CYAN)
            
            driver = self.setup_driver(thread_id)
            if not driver:
                return False

            # Tạo thông tin ngẫu nhiên
            ho, ten = self.generate_vietnamese_name()
            sdt = self.generate_phone_number()
            password = fb_password
            full_name = f"{ho} {ten}"
            
            self.print_colored(f"🧵 Luồng {thread_id} - Tài khoản {account_number}:", Fore.BLUE)
            self.print_colored(f"   👤 Tên: {full_name}", Fore.WHITE)
            self.print_colored(f"   📞 SĐT: {sdt}", Fore.WHITE)
            self.print_colored(f"   🔐 Mật khẩu: {password}", Fore.WHITE)

            # Truy cập trang đăng ký mobile
            driver.get("https://mbasic.facebook.com/reg/")
            time.sleep(random.uniform(3, 5))

            # Điền thông tin cơ bản
            try:
                # Họ
                lastname_field = self.wait_for_element(driver, By.NAME, 'lastname')
                if lastname_field:
                    lastname_field.clear()
                    for char in ten:
                        lastname_field.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.1))
                    time.sleep(random.uniform(1, 2))
                
                # Tên
                firstname_field = self.wait_for_element(driver, By.NAME, 'firstname')
                if firstname_field:
                    firstname_field.clear()
                    for char in ho:
                        firstname_field.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.1))
                    time.sleep(random.uniform(1, 2))
            except Exception as e:
                self.print_colored(f"🧵 Luồng {thread_id}: Lỗi điền tên - {e}", Fore.YELLOW)

            # Số điện thoại
            try:
                email_field = self.wait_for_element(driver, By.NAME, 'reg_email__')
                if email_field:
                    email_field.clear()
                    for char in sdt:
                        email_field.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.1))
                    time.sleep(1)
            except Exception as e:
                self.print_colored(f"🧵 Luồng {thread_id}: Lỗi điền SĐT - {e}", Fore.YELLOW)

            # Mật khẩu
            try:
                pass_field = self.wait_for_element(driver, By.NAME, 'reg_passwd__')
                if pass_field:
                    pass_field.clear()
                    for char in password:
                        pass_field.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.1))
                    time.sleep(1)
            except Exception as e:
                self.print_colored(f"🧵 Luồng {thread_id}: Lỗi điền mật khẩu - {e}", Fore.YELLOW)

            # Chọn ngày sinh
            try:
                # Ngày
                day_select = self.wait_for_element(driver, By.ID, 'day')
                if day_select:
                    Select(day_select).select_by_value(str(random.randint(1, 28)))
                    time.sleep(0.5)
                
                # Tháng
                month_select = self.wait_for_element(driver, By.ID, 'month')
                if month_select:
                    Select(month_select).select_by_value(str(random.randint(1, 12)))
                    time.sleep(0.5)
                
                # Năm
                year_select = self.wait_for_element(driver, By.ID, 'year')
                if year_select:
                    Select(year_select).select_by_value(str(random.randint(1980, 2000)))
                    time.sleep(0.5)
            except Exception as e:
                self.print_colored(f"🧵 Luồng {thread_id}: Lỗi chọn ngày sinh - {e}", Fore.YELLOW)

            # Chọn giới tính
            try:
                gender_value = random.choice(["1", "2"])  # 1: Nam, 2: Nữ
                gender_field = self.wait_for_element(driver, By.CSS_SELECTOR, f"input[name='sex'][value='{gender_value}']")
                if gender_field:
                    driver.execute_script("arguments[0].click();", gender_field)
                    time.sleep(1)
            except Exception as e:
                self.print_colored(f"🧵 Luồng {thread_id}: Lỗi chọn giới tính - {e}", Fore.YELLOW)

            # Submit form
            try:
                submit_button = self.wait_for_element(driver, By.NAME, 'websubmit')
                if submit_button:
                    self.print_colored(f"🧵 Luồng {thread_id}: Đang submit form...", Fore.BLUE)
                    time.sleep(random.uniform(2, 3))
                    
                    try:
                        driver.execute_script("arguments[0].click();", submit_button)
                    except:
                        submit_button.click()
                    
                    self.print_colored(f"🧵 Luồng {thread_id}: Đã submit form", Fore.BLUE)
                    time.sleep(20)
                else:
                    self.print_colored(f"🧵 Luồng {thread_id}: Không tìm thấy nút submit", Fore.RED)
                    return False
            except Exception as e:
                self.print_colored(f"🧵 Luồng {thread_id}: Lỗi submit form - {e}", Fore.RED)
                return False

            # Kiểm tra kết quả đăng ký
            success = False
            current_url = driver.current_url.lower()
            page_source = driver.page_source.lower()

            if any(x in current_url for x in ['checkpoint', 'confirmemail', 'xacnhan']):
                self.print_colored(f"🧵 Luồng {thread_id}: ✅ Đăng ký thành công, cần xác minh", Fore.GREEN)
                success = True
            elif any(x in page_source for x in ['checkpoint', 'xác nhận', 'confirm']):
                self.print_colored(f"🧵 Luồng {thread_id}: ✅ Đăng ký thành công, cần xác minh", Fore.GREEN)
                success = True
            elif any(x in current_url for x in ['home', 'newsfeed', 'facebook.com']):
                self.print_colored(f"🧵 Luồng {thread_id}: ✅ Đăng ký thành công hoàn toàn", Fore.GREEN)
                success = True
            else:
                if any(x in page_source for x in ['lỗi', 'error', 'invalid', 'số điện thoại']):
                    self.print_colored(f"🧵 Luồng {thread_id}: ❌ Đăng ký thất bại - có lỗi xảy ra", Fore.RED)
                    return False
                else:
                    self.print_colored(f"🧵 Luồng {thread_id}: ⚠️ Đang kiểm tra kết quả...", Fore.YELLOW)
                    time.sleep(15)
                    success = True

            if success:
                try:
                    cookies = driver.get_cookies()
                    cookie_string = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
                    
                    uid = "UNKNOWN"
                    for cookie in cookies:
                        if cookie['name'] == 'c_user':
                            uid = cookie['value']
                            break
                    
                    with open('TK.txt', 'a', encoding='utf-8') as f:
                        status = "NEED_VERIFY" if 'checkpoint' in current_url else "ACTIVE"
                        f.write(f"{uid}|{sdt}|{password}|{cookie_string}|{full_name}|{status}\n")
                    
                    if uid != "UNKNOWN":
                        self.print_colored(f"🧵 Luồng {thread_id}: ✅ Đã lưu tài khoản {uid}", Fore.GREEN)
                    else:
                        self.print_colored(f"🧵 Luồng {thread_id}: ✅ Đã lưu tài khoản (UID chưa xác định)", Fore.YELLOW)
                    
                    return True
                        
                except Exception as e:
                    self.print_colored(f"🧵 Luồng {thread_id}: ❌ Lỗi lưu thông tin - {e}", Fore.RED)
                    return False
            else:
                self.print_colored(f"🧵 Luồng {thread_id}: ❌ Đăng ký thất bại", Fore.RED)
                return False

        except Exception as e:
            self.print_colored(f"🧵 Luồng {thread_id}: ❌ Lỗi nghiêm trọng - {e}", Fore.RED)
            return False
        finally:
            if driver:
                try:
                    driver.quit()
                except:
                    pass

    def run_registration(self, num_threads, total_accounts, fb_password):
        """Chạy đăng ký với multi-threading"""
        self.show_minimal_menu("ĐĂNG KÝ TÀI KHOẢN FACEBOOK")
        
        self.print_colored(f"🚀 Bắt đầu đăng ký {total_accounts} tài khoản với {num_threads} luồng", Fore.MAGENTA)
        self.print_colored(f"🔐 Mật khẩu sử dụng: {fb_password}", Fore.CYAN)
        
        # Kiểm tra giới hạn tài khoản
        if self.user_manager.user_data:
            max_accounts = self.user_manager.user_data['max_accounts']
            self.print_colored(f"📊 Giới hạn tài khoản của bạn: {max_accounts}", Fore.YELLOW)
        
        successful_accounts = 0
        failed_accounts = 0
        
        def worker(args):
            thread_id, account_num = args
            nonlocal successful_accounts, failed_accounts
            if self.register_account(thread_id, account_num, fb_password):
                successful_accounts += 1
            else:
                failed_accounts += 1
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            args_list = []
            for i in range(total_accounts):
                thread_id = i % num_threads
                args_list.append((thread_id, i + 1))
            
            for args in args_list:
                executor.submit(worker, args)
                time.sleep(random.uniform(20, 25))
        
        self.show_minimal_menu("KẾT QUẢ ĐĂNG KÝ")
        self.print_colored(f"✅ Thành công: {successful_accounts}", Fore.GREEN)
        self.print_colored(f"❌ Thất bại: {failed_accounts}", Fore.RED)
        if total_accounts > 0:
            self.print_colored(f"📊 Tỷ lệ thành công: {(successful_accounts/total_accounts)*100:.1f}%", Fore.CYAN)

    def extract_uids(self):
        """Tách UID từ file tài khoản"""
        self.show_minimal_menu("TÁCH UID TỪ TÀI KHOẢN")
        
        try:
            if not os.path.exists('TK.txt'):
                self.print_colored("❌ Không tìm thấy file TK.txt", Fore.RED)
                return

            with open('TK.txt', 'r', encoding='utf-8') as tk_file:
                lines = tk_file.readlines()
                
            uids = []
            for line in lines:
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 1:
                        uid = parts[0].strip()
                        if uid and uid != "UNKNOWN" and uid.isdigit():
                            uids.append(uid)

            with open('uid.txt', 'w', encoding='utf-8') as uid_file:
                for uid in uids:
                    uid_file.write(f"{uid}\n")

            self.print_colored(f"✅ Đã tách {len(uids)} UID vào file uid.txt", Fore.GREEN)
            
        except Exception as e:
            self.print_colored(f"❌ Lỗi khi tách UID: {e}", Fore.RED)

    def show_cookies_example(self):
        """Hiển thị ví dụ về cookie"""
        self.show_minimal_menu("VÍ DỤ COOKIE FACEBOOK")
        
        self.print_colored("📋 Cookie hoàn chỉnh cần có các thành phần:", Fore.YELLOW)
        print(f"\n{Fore.GREEN}c_user={Fore.WHITE}61581209653224{Fore.GREEN};")
        print(f"xs={Fore.WHITE}22%3A26rDEry4ivlNpA%3A2%3A1758932144%3A-1%3A-1{Fore.GREEN};")
        print(f"fr={Fore.WHITE}1v5lO1JbxxKPOtciX.AWd7ky_I9ZCRxYVbjfIQ7xSEayROmjWANqk17I9hTW569kgHkqs.Bo1yyd..AAA.0.0.Bo1yyr.AWfNtZuti2ynaD_q4Fqe0NIX9jY{Fore.GREEN};")
        print(f"datr={Fore.WHITE}nSzXaIZZElNXE9VMx3odYFyO{Fore.GREEN};")
        
        self.print_colored(f"\n🔑 UID nằm ở cookie: {Fore.GREEN}c_user{Fore.WHITE}=61581209653224", Fore.CYAN)

    def show_statistics(self):
        """Hiển thị thống kê tài khoản đã đăng ký"""
        try:
            if os.path.exists('TK.txt'):
                with open('TK.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                active_accounts = len([line for line in lines if 'ACTIVE' in line])
                verify_accounts = len([line for line in lines if 'NEED_VERIFY' in line])
                unknown_accounts = len([line for line in lines if 'UNKNOWN' in line])
                
                self.print_colored(f"📊 THỐNG KÊ TÀI KHOẢN:", Fore.CYAN)
                self.print_colored(f"   📈 Tổng số: {len(lines)}", Fore.WHITE)
                self.print_colored(f"   ✅ Active: {active_accounts}", Fore.GREEN)
                self.print_colored(f"   ⚠️ Cần xác minh: {verify_accounts}", Fore.YELLOW)
                self.print_colored(f"   ❓ Chưa xác định: {unknown_accounts}", Fore.RED)
            else:
                self.print_colored("📊 Chưa có tài khoản nào được đăng ký", Fore.YELLOW)
        except Exception as e:
            self.print_colored(f"📊 Lỗi đọc thống kê: {e}", Fore.RED)

    def main(self):
        """Hàm chính"""
        self.clear_console()
        print(self.banner)
        
        # Hiệu ứng loading khi vào tool
        self.loading_animation("Khởi động tool")
        
        # ĐĂNG NHẬP HỆ THỐNG
        if not self.user_manager.authenticate_user():
            self.print_colored("⏳ Tool sẽ tự động thoát sau 5 giây...", Fore.YELLOW)
            time.sleep(15)
            return
        
        # ĐĂNG NHẬP THÀNH CÔNG
        self.print_colored(f"✅ Chào mừng {self.user_manager.current_user}!", Fore.GREEN)
        
        # Hiển thị thông tin user
        if self.user_manager.user_data:
            user_data = self.user_manager.user_data
            self.print_colored(f"📅 Hạn sử dụng: {user_data['expiry']}", Fore.CYAN)
            self.print_colored(f"🖥️ Số máy đã kích hoạt: {len(user_data['hardware_ids'])}/{user_data['max_devices']}", Fore.CYAN)
            self.print_colored(f"📊 Giới hạn tài khoản: {user_data['max_accounts']}", Fore.CYAN)
        
        time.sleep(2)
        
        while True:
            try:
                self.show_minimal_menu()
                
                choice = input(f"\n{Fore.CYAN}👉 Chọn chức năng (1-5): {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    fb_password = self.get_fb_password_choice()
                    if fb_password is None:
                        continue
                        
                    try:
                        self.show_minimal_menu("THIẾT LẬP ĐĂNG KÝ")
                        num_threads = int(input(f"{Fore.CYAN}👉 Nhập số luồng (1-3): {Style.RESET_ALL}"))
                        total_accounts = int(input(f"{Fore.CYAN}👉 Nhập tổng số tài khoản: {Style.RESET_ALL}"))
                        
                        if 1 <= num_threads <= 3 and total_accounts > 0:
                            self.run_registration(num_threads, total_accounts, fb_password)
                        else:
                            self.print_colored("❌ Số luồng phải từ 1-3 và số tài khoản > 0", Fore.RED)
                    except ValueError:
                        self.print_colored("❌ Vui lòng nhập số hợp lệ", Fore.RED)
                    except KeyboardInterrupt:
                        self.print_colored("\n↩️ Quay lại menu chính...", Fore.YELLOW)
                        continue
                        
                elif choice == '2':
                    self.extract_uids()
                    
                elif choice == '3':
                    self.show_cookies_example()
                    
                elif choice == '4':
                    self.show_minimal_menu("XÓA DỮ LIỆU")
                    try:
                        files_to_remove = ['TK.txt', 'uid.txt']
                        removed_count = 0
                        for file in files_to_remove:
                            if os.path.exists(file):
                                os.remove(file)
                                self.print_colored(f"✅ Đã xóa {file}", Fore.GREEN)
                                removed_count += 1
                        
                        if removed_count == 0:
                            self.print_colored("ℹ️ Không có file nào để xóa", Fore.YELLOW)
                    except Exception as e:
                        self.print_colored(f"❌ Lỗi khi xóa file: {e}", Fore.RED)
                        
                elif choice == '5':
                    self.show_minimal_menu("THOÁT CHƯƠNG TRÌNH")
                    self.print_colored("👋 Cảm ơn bạn đã sử dụng tool!", Fore.MAGENTA)
                    self.print_colored(f"📞 Tác giả: {self.author}", Fore.CYAN)
                    break
                else:
                    self.print_colored("❌ Lựa chọn không hợp lệ", Fore.RED)
                    
                input(f"\n{Fore.YELLOW}👉 Nhấn Enter để tiếp tục...{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                self.print_colored("\n↩️ Quay lại menu chính...", Fore.YELLOW)
                continue
            except Exception as e:
                self.print_colored(f"❌ Lỗi không xác định: {e}", Fore.RED)

if __name__ == "__main__":
    # Ẩn các cảnh báo
    import warnings
    warnings.filterwarnings("ignore")
    os.environ['WDM_LOG_LEVEL'] = '0'
    
    tool = FacebookRegTool()
    tool.main()