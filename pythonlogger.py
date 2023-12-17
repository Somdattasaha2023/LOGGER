import sys, os
import datetime
import logging

values_list = ""


def get_env_variable(p_var_name, p_fail_if_none=True):
  if p_var_name == "LOG_DIR":
    p_var_variable = ''
  if p_var_name == "LOGFILE_4ENV":
    p_var_variable = ''

  if p_var_name == None and p_fail_if_none:
    print("Env variable", p_var_name, "is not set")
    raise EnvironmentError("Variable", p_var_name, "is not set")
  else:
    print("Env variable", p_var_variable, "is  set")

  return p_var_variable


SCRIPT_NAME = '/app/bas/script/aaa.py'
# get substring between last slash and last dot - like text aaa out of /app/bas/script/aaa.py
#print('os sep :' + os.sep)
SCRIPT_NAME = ".".join(SCRIPT_NAME.split(os.sep)[-1].split(".")[0:-1])
#print(SCRIPT_NAME)

p_var_variable = os.getenv("LOG_DIR")
print(p_var_variable)

feed_sql_par_id = 0
try:
  run_signature = '231205'
  if run_signature.isdigit():  # may be converted to number
    feed_sql_par_id = int(run_signature)
    print("one of parameters is digit:", run_signature)

  elif run_signature.isalnum():
    print("one of parameters is alphanumeric:", run_signature)
  #    exit(0)

  else:
    feed_sql_par_id = 0

  if len(run_signature) != 6 or feed_sql_par_id == 0:
    print("one of parameters is invalid:", run_signature, feed_sql_par_id)
    exit(1)
#except Exception as e:
#  print("At least two arguments must be provided to the script", SCRIPT_NAME,e)
# exit(1)

except Exception:
  print("Arguments are provided correctly")
  #exit(1)

# assume we need to compare counts of retrieve and insert. If not we set this boolean to False later
b_match_retrieve_insert_required = True
#print(b_match_retrieve_insert_required)
# initiate logger
log_dir = get_env_variable("LOG_DIR")

log_file = get_env_variable("LOGFILE_4ENV", False)
if log_file == None:
  log_file = log_dir + "/" + SCRIPT_NAME + "_" + run_signature + "_" + str(
      feed_sql_par_id) + "_" + datetime.datetime.now().strftime(
          "%Y%m%d%H%M%S") + ".log"
else:
  log_file = log_dir + "/" + log_file

log_file = log_dir + SCRIPT_NAME + "_" + run_signature + "_" + str(
    feed_sql_par_id) + "_" + datetime.datetime.now().strftime(
        "%Y%m%d%H%M%S") + ".log"
#print(log_file)

logging.basicConfig(
    filename=log_file,
    filemode='w',
    format=
    '%(asctime)s %(filename)s %(lineno)d %(module)s %(levelname)s:\n%(message)s\n'
)

logger = logging.getLogger(__name__)

#print('logger' , logger)

logger.setLevel(logging.DEBUG)

#print('logger' , logger)
logger.info("Script execution started by Somdatta: " + " ".join(SCRIPT_NAME) +
            " ".join(run_signature) + "\nlog file is " + log_file)
#print(logging)

logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

logging.error("high alert")

print(logging)

meta_col_list = '<COB>'
from_where_clause = 'whed'

data_fully_refreshed = meta_col_list.find('<COB>')

print("data_fully_refreshed", data_fully_refreshed)

#== -1 and
data_from_where_clause = from_where_clause.upper().find('WHERE')
print("from_where_clause", data_from_where_clause)

destination_col_list = "(1,3,5,6,877)"

#pos_start=destination_col_list.upper().find("TRIM(")

pos_start = destination_col_list.lower().find("(")
print("pos_start", pos_start)

pos_end = destination_col_list.lower().find(")")
print("pos_end", pos_end)
print(destination_col_list.count(","))

values_list += "( :1"
for i in range(destination_col_list.count(",")):
  values_list += "," + ":" + str(i + 2)

print("the final values_list:", values_list)
values_list += ")"

print("the final values list:", values_list)
