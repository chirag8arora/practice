import re

m = r'(0?[1-9]|1[0-2])'
d = r'(0?[1-9]|[1-2]\d|30)'
y = r'((18|19|20|)\d{2})'
p = r'\b(' + m + '(-|/)' + d + r'\3' + y + r')\b'
# p = r'\b((0?[1-9]|1[0-2])([-/])(0?[1-9]|[1-2]\d|30)\3((18|19|20)\d{2}|[1-9]\d|0?[1-9]))\b'
print p

l = [
    ('05/09/2013', True),
    ('12/09/2013', True),
    ('5/09/2013', True),
    ('5/12/2013', True),
    ('5/10/2013', True),
    ('05/9/2013', True),
    ('5/9/2013', True),
    ('05/09/13', True),
    ('5/09/13', True),
    ('05/9/13', True),
    ('5/9/13', True),
    ('05-09-2013', True),
    ('05-09-00', True),
    ('5-09-2013', True),
    ('05-9-2013', True),
    ('5-9-2013', True),
    ('05-09-13', True),
    ('5-09-13', True),
    ('05-9-13', True),
    ('5-9-13', True),
    ('12/26-1987', False),
    ('12/26/1987', True),
    ('5-9-1713', False),
    ('5/31/2011', False),
    ('0-0-00', False),
    ('0/0/00', False),
    ('1/30/01', True),
    ('1/10/10', True),
    ('119/10/10', False),
    ('ajax11/10/10', False),
    ('11/11/2222', False),
    ('13/13/13', False),
    ('13/13/0', False),
    ('12/13/220', False),
    ('12/13/99', True),
]

for i in l:
    m = re.match(p, i[0])
    # print m.groupdict()
    if (m is not None) != i[1]:
        print i
