def Uni_Replacer(string):
    replacements = {
        '\\xc4\\x84': 'Ą',
        '\\xc4\\x86': 'Ć',
        '\\xc4\\x98': 'Ę',
        '\\xc5\\x81': 'Ł',
        '\\xc5\\x83': 'Ń',
        '\\xc3\\x93': 'Ó',
        '\\xc5\\x9a': 'Ś',
        '\\xc5\\xb9': 'Ź',
        '\\xc5\\xbb': 'Ż',
        '\\xc4\\x85': 'ą',
        '\\xc4\\x87': 'ć',
        '\\xc4\\x99': 'ę',
        '\\xc5\\x82': 'ł',
        '\\xc5\\x84': 'ń',
        '\\xc3\\xb3': 'ó',
        '\\xc5\\x9b': 'ś',
        '\\xc5\\xba': 'ź',
        '\\xc5\\xbc': 'ż'
    }

    work_text = string

    for k, v in replacements.items():
        work_text = work_text.replace(k, v)

    return work_text


def Pl_Replacer(string):
    replacements = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z',
        'Ą': 'a',
        'Ć': 'c',
        'Ę': 'e',
        'Ł': 'l',
        'Ń': 'n',
        'Ó': 'o',
        'Ś': 's',
        'Ź': 'z',
        'Ż': 'z'
    }

    work_text = string

    for k, v in replacements.items():
        work_text = work_text.replace(k, v)

    return work_text