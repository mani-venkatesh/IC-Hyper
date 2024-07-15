import wfdb

def load_data(records_path):
    sample_length = 60*60 # seconds
    sample_frequency = 50 # hz
    with open(records_path, 'r') as records:
        raw_contents = records.read()
        record_list = raw_contents.split('\n')
        
        patient_dict = {}
        for record in record_list:
            path = 'database/' + record
            signals, fields = wfdb.rdsamp(path, sampto=sample_length * sample_frequency)
            temp_dict = {}
            temp_dict['s'] = signals
            temp_dict['f'] = fields
            patient_dict[record] = temp_dict
        return patient_dict
