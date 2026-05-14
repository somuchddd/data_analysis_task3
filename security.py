blocked_prompts = [
    'забудь предыдущие инструкции',
    'игнорируй предыдущие инструкции',
    'отключи ограничения',
    'обойди ограничения',
    'выполни код',
    'удали файл',
    'удали папку',
    'скачай файл',
    'отправь данные',
    'отправь файл',
    'твоя роль',
    'os.system',
    'subprocess',
    'eval(',
    'exec('
]

def is_prompt_safe(prompt):
    prompt = prompt.lower()
    for pattern in blocked_prompts:
        if pattern.lower() in prompt:
            return False
        
    return True