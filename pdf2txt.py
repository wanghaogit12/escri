#!/home/wh/Desktop/envir/py/bin/python3
"""
PDF 文本提取工具
自动在PDF同目录生成同名.txt文件
"""
import pdfplumber
import sys
import os

def extract_pdf(pdf_path, output_path):
    """提取PDF文本"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n\n'  # 不加页号信息
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text.strip())
            return True
    except Exception as e:
        print(f'错误: {e}')
        return False

def get_unique_filename(file_path):
    """获取唯一文件名，避免覆盖"""
    if not os.path.exists(file_path):
        return file_path
    
    base, ext = os.path.splitext(file_path)
    counter = 1
    while True:
        new_path = f"{base}_{counter}{ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1

def main():
    # 获取PDF文件路径
    if len(sys.argv) == 2:
        pdf_file = sys.argv[1]
    else:
        print("PDF文本提取工具")
        pdf_file = input("请输入PDF文件路径: ").strip()
        pdf_file = pdf_file.strip("'\"")
    
    # 检查文件是否存在
    if not os.path.exists(pdf_file):
        print(f"文件不存在: {pdf_file}")
        sys.exit(1)
    
    # 生成输出文件路径
    pdf_dir = os.path.dirname(pdf_file)
    pdf_name = os.path.basename(pdf_file)
    pdf_base = os.path.splitext(pdf_name)[0]
    output_file = os.path.join(pdf_dir, f"{pdf_base}.txt")
    
    # 确保文件名唯一
    output_file = get_unique_filename(output_file)
    
    # 提取文本
    success = extract_pdf(pdf_file, output_file)
    
    if success:
        print(f"已保存到: {output_file}")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
