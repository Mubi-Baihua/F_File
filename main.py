from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys
import os
import requests

def download_file(url, local_filename):
    try:
        resp = requests.get(url, stream=True)          # 使用流模式避免一次性读取大文件
        resp.raise_for_status()                        # 如果请求失败会抛出异常

        with open(local_filename, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:                             # 忽略保持活动的空块
                    f.write(chunk)

        return True

    except requests.exceptions.RequestException as e:
        print(f"下载失败：{e}")
        return False
def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("f_file.png"))
    if  os.path.exists('.f_file/easytier-core.downloadexe'):
        os.remove('.f_file/easytier-core.downloadexe')
    if not os.path.isdir('.f_file'):
        os.makedirs('.f_file')
    if  not os.path.exists('.f_file/easytier-core.exe'):
        window_install = QMainWindow()
        window_install.setWindowTitle("F File 1")
        window_install.resize(400, 200)
        central_widget = QWidget()
        window_install.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        log_text_edit = QTextEdit()
        log_text_edit.setReadOnly(True)  # 设置为只读模式，防止用户编辑
        layout.addWidget(log_text_edit)

        log_text_edit.append("EasyTier版本 : v2.4.5")
        log_text_edit.append("正在下载EasyTier内核...")

        window_install.show() 

        url = "https://gitee.com//mu-bi-bai-hua/EasyTier/releases/download/v2.4.5/easytier-core.exe"

        if download_file(url, ".f_file/easytier-core.downloadexe"):
            os.rename(".f_file/easytier-core.downloadexe", ".f_file/easytier-core.exe")
            log_text_edit.append("下载成功！")
            window_install.close()  # 下载完成后关闭安装窗口
            main_page(app)
        else:
            log_text_edit.append("下载失败！")
            app.exec()
    else:
        main_page(app)

def send_file(log_text_edit):
    pass
        
def main_page(app):    
    window = QMainWindow()
    window.setWindowTitle("F File 1")
    window.resize(450, 300)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout()
    central_widget.setLayout(layout)

    label = QLabel("F File 1 - 文件传输")
    label.setAlignment(Qt.AlignCenter)
    
    # 设置标签字体为标题大小
    font = label.font()
    font.setPointSize(12)  # 增大字体大小
    font.setBold(True)     # 设置为粗体
    label.setFont(font)
    
    layout.addWidget(label)

    button_send = QPushButton("发送文件")
    #button_send.setFixedSize(450, 25)
    button_send.clicked.connect(lambda: send_file(log_text_edit))
    layout.addWidget(button_send)
    
    button_receive = QPushButton("接收文件")
    #button_receive.setFixedSize(450, 25)  # 设置按钮大小
    layout.addWidget(button_receive)

    log_text_edit = QTextEdit()
    log_text_edit.setReadOnly(True)  # 设置为只读模式，防止用户编辑
    layout.addWidget(log_text_edit)

    window.show()

    log_text_edit.append("F File 1 - 文件传输")
    log_text_edit.append("Coded by MubiBaihua")

    app.exec()

if __name__ == "__main__":
    main()