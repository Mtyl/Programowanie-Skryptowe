python3 -c 'import sys,re,functools;from collections import Counter;print(re.sub(r":\s",":",str(dict(Counter((map(lambda i:len(i), (re.findall(r"\S+", sys.stdin.read())))))))))'