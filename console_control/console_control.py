from typing import List
import sys

path_parts: List[str] = ["C:", "Users", "michael.brunner", "PycharmProjects", "InnoSuisse", "Lib", "site-packages"]

path = '/'.join(path_parts)
print(path)
sys.path.append(path)

from ptpython.repl import embed

embed(globals(), locals())
