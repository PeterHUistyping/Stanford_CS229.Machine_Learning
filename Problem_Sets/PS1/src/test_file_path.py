# Hope you don't be imprisoned by legacy Python code :)
from pathlib import Path    # add path
# `cwd`: current directory is straightforward
cwd = Path.cwd()    # add path

# `mod_path`: According to the accepted answer and combine with future power
# if we are in the `helper_script.py`
mod_path = Path(__file__).parent    # add path
# OR if we are `import helper_script`
#mod_path = Path(helper_script.__file__).parent

# `src_path`: with the future power, it's just so straightforward
relative_path_1 = '../data'

#relative_path_1 = 'same/parent/with/helper/script/'
#relative_path_2 = '../../or/any/level/up/'
src_path_1 = (mod_path / '../data').resolve()   # add path
#src_path_2 = (mod_path / relative_path_2).resolve()
print(src_path_1)
