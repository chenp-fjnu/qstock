class Codes(object):
    @staticmethod
    def get_code(s):
        if len(s)==6:
            return (s+'SH') if s.startswith('6') else (s+'SZ')
        else:
            return '股票代码必须为6位数字！'