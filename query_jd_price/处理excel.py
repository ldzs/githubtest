from openpyxl import load_workbook


def 读取excel():
    文件=load_workbook("商品目录及价格.xlsx")
    页=文件.active
    print(页.title)

def main():
    读取excel()

main()