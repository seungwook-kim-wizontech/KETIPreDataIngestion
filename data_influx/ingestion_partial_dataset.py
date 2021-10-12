import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from requests.api import head
from KETIPreDataIngestion.data_influx import ingestion_basic_dataset as ibd
from KETIPreDataIngestion.KETI_setting import influx_setting_KETI as ins

def partial_dataSet_ingestion(intDataInfo, influx_parameter):
    
    result={}
    for i, dbinfo in enumerate(intDataInfo['db_info']):
        db_name = dbinfo['db_name']
        measurement = dbinfo['measurement']

        influx_c = ibd.BasicDatasetRead(influx_parameter, db_name, measurement)
        bind_params = {'end_time': dbinfo['end'], 'start_time': dbinfo['start']}
        result[i] = influx_c.get_data_by_time(bind_params)        

        result[i].index.name ='datetime'
        
    return result

