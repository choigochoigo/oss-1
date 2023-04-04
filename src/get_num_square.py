import os

num = os.environ.get("INPUT_NUM")
if num:
  try:
    num = int(num)
  except Exception:
    exit('ERROR: the INPUT_NUM provide ("{}") is not an integer'.format((num))
else:
  num=1
        
print(f"::set-output name=num_sqaured::{num**2}")
                     
