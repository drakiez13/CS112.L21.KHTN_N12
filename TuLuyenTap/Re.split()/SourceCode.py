regex_pattern = r"[.,]\s*"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))