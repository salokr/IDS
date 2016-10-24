import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import StratifiedKFold
import numpy
def createFile(inputfile,testfile):

    #eval_size=0.10
    
    col_name=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]
    
    data=pd.read_csv(inputfile,header=None,names=col_name)
    
    testdata=pd.read_csv(testfile,header=None,names=col_name)
    
    
    
    #THE LABEL ENCODER FOR SERVICES COLUMN
    
    le=preprocessing.LabelEncoder()
    data.service=le.fit_transform(data.service)
    

    #THROWS EXCEPTION
    
    testdata.service=le.fit_transform(testdata.service)
    
    #ohservice=pd.get_dummies(data['service'])
    #data=data.join(ohservice,lsuffix='service')
    #data=data.drop('service',axis=1)
    
    #
    #TODO : SERVICE WILL HAVE TO BE HANDELLED DIFFERENTLY
    #
    
    
    
    
    
    
    ohptype=pd.get_dummies(data['protocol_type'])
    data=data.join(ohptype,lsuffix='ptype')
    data=data.drop('protocol_type',axis=1)
    
    
    
    
    ohflag=pd.get_dummies(data['flag'])
    data=data.join(ohflag,lsuffix='flag')
    data=data.drop('flag',axis=1)
    
    
    #ohland=pd.get_dummies(data['land'])
    #data=data.join(ohland,lsuffix='land')
    #data=data.drop('land',axis=1)
    
    
    
    #ohlogged_in=pd.get_dummies(data['logged_in'])
    #data=data.join(ohlogged_in,lsuffix='li')
    #data=data.drop('logged_in',axis=1)
    
    
    
    #ohis_host_login=pd.get_dummies(data['is_host_login'])
    #data=data.join(ohis_host_login,lsuffix='ihl')
    #data=data.drop('is_host_login',axis=1)
    
    
    #ohis_guest_login=pd.get_dummies(data['is_guest_login'])
    #data=data.join(ohis_guest_login,lsuffix='ihl')
    #data=data.drop('is_guest_login',axis=1)
    
    
    
    #ohroot_shell=pd.get_dummies(data['root_shell'])
    #data=data.join(ohroot_shell,lsuffix='rs')
    #data=data.drop('root_shell',axis=1)
    
    
    ohsu_attempted=pd.get_dummies(data['su_attempted'])
    data=data.join(ohsu_attempted,lsuffix='sa')
    data=data.drop('su_attempted',axis=1)
    
   
    labels=data['label']
    data=data.drop('label',axis=1)
    data=data.join(labels,lsuffix='labels')
    
    
    temp=data.values
    cols=data.shape[1]
    y=temp[:,cols-1]
    #kf=StratifiedKFold(y,round(1./eval_size))
    
    
    #train_indices,valid_indices=next(iter(kf))
    
    #X_train=temp[train_indices]
    #X_valid=temp[valid_indices]
    
    #numpy.savetxt("TrainFile.txt",X_train,delimiter=",",fmt='%s')
    #numpy.savetxt("ValidFile.txt",X_valid,delimiter=",",fmt='%s')
    
    #X_train.shape
    #X_valid.shape
    
    #return X_valid;
    #checkdata.apply(pd.Series.nunique)