# 文件拆分

```
.
├── out_files (拆分后文件目录)
│   ├── test1_1.txt
│   ├── test1_2.txt
│   ├── test1_3.txt
│   ├── test1_4.txt
│   ├── test1_5.txt
│   ├── test2_1.txt
│   ├── test2_2.txt
│   ├── test2_3.txt
│   ├── test2_4.txt
│   └── test2_5.txt
├── src_files (待拆分文件目录)
│   ├── test1.txt
│   └── test2.txt
├── main.py
└── README.md
```

# 原理  

将文件**按行**拆分为若干个文件  

# 使用  

1. 将需要拆分的文件放在 `src_files` 目录下    
2. 确定拆分数: 修改 `main.py` 第59行的 `group` 参数, 当前设置为5  
3. 运行 `main.py`, 分组完毕, 结果保存在 `out_files` 目录里 

# 说明  

1. 拆分后的文件命名规则: 在原来待拆分文件名基础上, 加上 `_{序号}`. 比如将 `test.txt`, 拆分为5个文件, 则拆分后的文件名为: `test_1.txt`, `test_2.txt`, `test_3.txt`, `test_4.txt`, `test_5.txt`  
2. `src_files` 目录可以放多个需要拆分文件. 比如上面目录树里所示, 将 `test1.txt` 和 `test2.txt` 分别拆分为5个文件  
