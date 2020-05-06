# -*- coding: utf-8 -*-

# Author: Cynthia

"""
    利用pandas读写excel
"""
"""
    pandas基础知识:
    1. Python Data Analysis Library, 基于numpy的更高一级的库
    2. Series([data, index, dtype, name, copy, …]), 类似于一维数组, 但是额外开辟了一个数组
    存储索引, 所以其索引可以不仅仅是数字; 有点像是拆开的字典; 可以通过两个数组构建(不指定index默认数
    组下标, 也可以通过字典构建
    3. DataFrame([data, index, columns, dtype, copy]), DataFrame是一个表格型数据结构，可
    以看做是由Series组成的字典
    
    
    补充一下numpy的数据类型:
    
"""
import os
import pandas as pd


def main():
    url_excel = "data/seed.xlsx"
    xls = pd.read_excel(url_excel)
    print(xls.size)
    print(xls.shape)
    print(len(xls))
    xls.iloc[3:5, 5] = 1000
    for index, row in xls.iterrows():
        xls.iloc[index, 5] = "333\n455666666666666666666666665"

    for index, col in xls.iteritems():
        print(max([len(str(x)) for x in col.values]))
    # loc和iloc的区别, loc按名字索引, iloc按数字index索引

    style = {

        'text_wrap': True,
        'align': 'left',
        'valign': 'vcenter',
        'bold': True,
        'bg_color': '#00CD66'

    }
    url_desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
    with pd.ExcelWriter("data/data1.xlsx") as writer:
        # 这里要先写到writer里, 否则writer无法进行获取sheet等操作
        xls.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
        workbook, worksheet = writer.book, writer.sheets['Sheet1']
        worksheet.set_column('F:F', None, workbook.add_format(style))
        writer.save()

    # excel解析不了na等, 需要先替换了, 不然后面要自己处理会很麻烦
    xls.fillna("", inplace=True)

    # 官方文档给的ExcelWriter支持追加, 但试了下好像不行, 关闭后再打开写入新的sheet会覆盖
    with pd.ExcelWriter("data/data2.xlsx") as writer:

        workbook = writer.book
        format = workbook.add_format(style)

        # 按行写
        xls.to_excel(writer, index=False, header=False, sheet_name='Sheet1')
        worksheet = writer.sheets['Sheet1']
        worksheet.write_row(0, 0, ['字段中文名', '字段英文名', '类型', '长度', '必输', '说明'], format)
        for index, row in xls.iterrows():
            # 用write_row等直接去写就不用单独调set_column等设置格式了, 可以直接参数指定
            worksheet.write_row(index + 1, 0, row, workbook.add_format({"text_wrap": True}))

        # 按列写
        xls.to_excel(writer, index=False, header=False, sheet_name='Sheet2')
        worksheet = writer.sheets['Sheet2']
        worksheet.write_row(0, 0, ['字段中文名', '字段英文名', '类型', '长度', '必输', '说明'], format)
        # 列枚举xls.iteritems()出来的index是列名而不是数字索引, 这里不能那么写
        for col in range(xls.shape[1]):
            worksheet.write_column(1, col, xls.iloc[:, col], workbook.add_format({"text_wrap": True}))


        # 按单元格写
        xls.to_excel(writer, index=False, header=False, sheet_name='Sheet3')
        worksheet = writer.sheets['Sheet3']

        # 整体格式设置而不是写的时候再设置
        # 注意, 整体格式设置完了, write的时候就不要设置了, 会全覆盖
        # set_row(row, height, cell_format, options)
        # set_column(first_col, last_col, width, cell_format, options)
        # pandas不支持设置自适应宽度, 只能自己算; 注意set_column索引参数是俩, row是一个
        # 列格式will be applied to any cells in the column that don’t have a format
        # 行格式takes precedence over a default column format
        f_len = lambda x: (len(x.encode("utf-8"))-len(x))/2+len(x)
        worksheet.set_row(0, None, workbook.add_format({"border":1, 'bold': True, 'bg_color': '#00CD66'}))
        for col in range(xls.shape[1]):

            max_len = max([f_len(x) for y in xls.iloc[:, col] for x in str(y).split("\n")])
            # 这里max_len没直接用, 而是加了个数字, 也是奇怪, 不加生成的excel单元格长度总是差一点
            worksheet.set_column(col, col, max_len+3, workbook.add_format({"border": 1, "text_wrap": True}))

        worksheet.write_row(0, 0, ['字段中文名', '字段英文名', '类型', '长度', '必输', '说明'])
        for i in range(xls.shape[0]):
            for j in range(xls.shape[1]):
                worksheet.write(i + 1, j, xls.iloc[i, j])


if __name__ == '__main__':
    main()
