# 원본 파일 경로와 저장할 파일 경로
input_path = 'y_2025\python.txt'
output_path = 'y_2025\python2.txt'

# 파일 읽고 ' '를 '\n'으로 대체
with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read().replace(' ', '\n')

# 새 파일로 저장
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)
