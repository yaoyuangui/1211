import subprocess
import sys


def deploy_web_app():
    try:
        # 从Git拉取最新代码
        print("Pulling the latest code from Git...")
        subprocess.run(["git", "pull"], check=True)
        print("Code pulled successfully.")

        # 安装依赖
        print("Installing dependencies...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed successfully.")

        # 运行测试套件
        print("Running test suite...")
        subprocess.run(["pytest"], check=True)
        print("Test suite passed successfully.")

        # 重启Web服务器
        print("Restarting the web server...")
        subprocess.run(["systemctl", "restart", "https://github.com/yaoyuangui/1211.git"
                                                ""], check=True)
        print("Web server restarted successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    deploy_web_app()