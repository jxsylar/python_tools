#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 20:04:33
# @Author  : jxsylar

import os


def get_files(*path):
    """输入路径，输出该目录下所有文件列表
    """
    file_list = list()
    path = set(path)  # 避免传入重复路径
    for p in path:
        g = os.walk(p)
        for path, dir_list, files_list in g:
            for file_name in files_list:
                temp = os.path.join(path, file_name)
                file_list.append(temp)
    return file_list


def group_file(outfile_folder, file_name, *, group=1):
    """将文件按行数拆分为 group 个小文件
    file_name: 支持路径输入
        1      ~ 6764
        6764+1 ~ 6764+1+6764
        6764*2+2  ~6764*3+2
        6764*3+3  ~ 6764*4+3
        6764*4+4  ~ 6764*5+4
        ...
        6764*(group_n-1)+(group_n-1) ~ 6764*group_n+(group_n-1)
    sub_file_n: max_line_per_group*(group_n-1)+(group_n-1) ~ max_line_per_group*group_n+(group_n-1)
    写入当前文件的判断条件: real_line_n <= max_line_per_group*group_n+(group_n-1)
    其中: group_n : range(1, group+1)
    """
    if group < 1 or not isinstance(group, int):
        raise TypeError('The arg group must be positive integer.')
    dir_path, file = os.path.split(file_name)
    file_basename, file_ext = os.path.splitext(file)
    # 子文件名
    sub_files_list = ['{}_{}{}'.format(file_basename, i, file_ext) for i in range(1, group+1)]
    max_line = len(['' for line in open(file_name, 'rb')])
    max_line_per_group = max_line//group
    group_n = 1
    f_src = open(file_name, 'rb')
    f_out = open('{}/{}'.format(outfile_folder, sub_files_list[group_n-1]), 'wb')
    for real_line_num, content in enumerate(f_src):
        if real_line_num <= max_line_per_group*group_n+(group_n-1):
            f_out.write(content)
        else:
            group_n += 1
            f_out = open('{}/{}'.format(outfile_folder, sub_files_list[group_n-1]), 'wb')
            f_out.write(content)
    f_src.close()


if __name__ == '__main__':
    src = 'src_files'
    out = 'out_files'
    group = 5

    file_list = get_files(src)
    for file in file_list:
        if os.path.isfile(file):
            group_file(out, file, group=group)
