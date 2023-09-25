#!/bin/bash

input_file="input.txt"  # 输入的txt文件名
output_dir="output"     # 输出文件夹名
split_ratio=0.7         # 拆分比例，这里是70%

# 创建输出文件夹
mkdir -p "$output_dir"

# 统计文本行数
total_lines=$(wc -l < "$input_file")
split_lines=$(echo "$total_lines * $split_ratio" | bc)
split_lines=${split_lines%.*}  # 去除小数部分

# 随机打乱文本行顺序
shuffled_lines=($(shuf -i 1-"$total_lines"))

# 分割成两个部分
split1_lines=("${shuffled_lines[@]:0:$split_lines}")
split2_lines=("${shuffled_lines[@]:$split_lines}")

# 创建并写入拆分后的文本文件
split1_file="$output_dir/split1.txt"
split2_file="$output_dir/split2.txt"

for line_num in "${split1_lines[@]}"; do
    sed -n "${line_num}p" "$input_file" >> "$split1_file"
done

for line_num in "${split2_lines[@]}"; do
    sed -n "${line_num}p" "$input_file" >> "$split2_file"
done

echo "拆分完成，拆分后的文本已保存在 $output_dir 目录下。"
