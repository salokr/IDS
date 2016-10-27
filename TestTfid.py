import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
def readFile(input):

    col_name=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]
    df=pd.read_csv('Example.txt',header=None,names=col_name)
    df
    tfv=TfidfVectorizer(min_df=1,             max_features=None,strip_accents='unicode',analyzer='word',token_pattern=r'\w{1,}',ngram_range=(1,2),use_idf=1,sublinear_tf=1,stop_words='english')
    text_Data=list(df.apply(lambda x: '%s' %(x['service']),axis=1))
    text_Data
    text=tfv.fit_transform(text_Data)
    text.todense()