import pytest
import subprocess
if __name__ == '__main__':

    pytest.main(["--alluredir", "./report/reportallure/"])
    cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/', './report/reporthtml/')
    print("开始生成报告！")
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print("报告生成完毕！")


