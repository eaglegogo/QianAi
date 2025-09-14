import re
from transformers import pipeline

# 假设日志为文本文件，每行一条
LOG_PATH = 'logs/devops.log'

# 加载大语言模型（可用小型模型或API，示例用huggingface pipeline）
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')


def extract_errors(log_text):
    """简单提取日志中的错误和异常行"""
    error_lines = [line for line in log_text.split('\n') if 'error' in line.lower() or 'exception' in line.lower()]
    return error_lines


def analyze_log():
    try:
        with open(LOG_PATH, 'r', encoding='utf-8') as f:
            log_text = f.read()
    except FileNotFoundError:
        return {'summary': '未找到日志文件', 'errors': []}

    errors = extract_errors(log_text)
    error_text = '\n'.join(errors) if errors else '无明显错误'
    # AI 总结（可根据实际模型和API调整）
    summary = summarizer(error_text, max_length=60, min_length=10, do_sample=False)[0]['summary_text'] if errors else '日志无明显异常。'
    return {
        'summary': summary,
        'errors': errors
    }

if __name__ == '__main__':
    result = analyze_log()
    print('AI日志摘要：', result['summary'])
    if result['errors']:
        print('错误详情:')
        for err in result['errors']:
            print(err)
