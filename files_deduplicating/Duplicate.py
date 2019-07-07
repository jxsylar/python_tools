#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 20:04:33
# @Author  : jxsylar


'''
功能：文件查重
'''

import os 
import sys
from hashlib import md5
import json
import time


def _get_files(*path):
    '''输入路径，输出该目录下所有文件列表'''
    file_list = list()
    path = set(path)    # 避免传入重复路径
    for p in path:
        g = os.walk(p)  
        for path, dir_list, files_list in g:
            for file_name in files_list:  
                temp = os.path.join(path, file_name)
                file_list.append(temp)
    return file_list


def _cal_md5(*path):
    file_md5_dict = dict()
    file_list = _get_files(*path)

    for file in file_list:
        with open(file, 'rb') as f:
            _hash = md5()
            for line in f:
                _hash.update(line)
        file_md5_dict.setdefault(_hash.hexdigest(), list()).append(file)
    return file_md5_dict


def get_dup_files(*path):
    dup_files = dict()
    file_md5_dict = _cal_md5(*path)
    for k, v in file_md5_dict.items():
        if len(v) > 1:
            dup_files[k] = v
    return dup_files


def write_then_open_file(filename, content):
    """将重复文件记录"""
    begin_time = '{}'.format(time.strftime('%Y/%M/%d/ %H:%M:%S'))
    with open(filename,'w', encoding='utf-8') as f:
        f.write('\n{:-^60}\n'.format('Begin '+begin_time))
        f.write(json.dumps(content, ensure_ascii=False, indent=2))
        end_time = time.strftime('%Y/%M/%d/ %H:%M:%S')
        f.write('\n{:-^60}\n'.format('End '+end_time))
    if sys.platform != 'linux':
        os.system('start {}'.format(filename))
    else:
        os.system('more {}'.format(filename))


if __name__ == '__main__':
    args = input('请输入需要查重的路径，若有多个路径，以空格分开：\n')
    path = args.split(' ')
    if len(path) <= 0:
        raise Exception('Please input PATH.')
    files = _get_files(*path)
    dup_files = get_dup_files(*path)
    unique_file = list(set(files) - set(dup_files))
    write_then_open_file('unique_file_result.txt', unique_file)
    write_then_open_file('duplicate_result.txt', dup_files)

