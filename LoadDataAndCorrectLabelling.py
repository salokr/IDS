import pandas as pd
import csv
from sklearn import preprocessing
from time import time


#with open("testdata.txt","r") as inp, open("SeparatedTest.txt","w") as out:
#    w=csv.writer(out)
#    w.writerows(x for x in csv.reader(inp, delimiter=","))




col_name=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]


kdd_dataset=pd.read_csv("fulldataset.txt",header=None,names=col_name)
#kdd_dataset.describe()



kdd_dataset['label'].replace(['smurf.','neptune.' , 'normal.' , 'satan.',  'ipsweep.' , 'portsweep.'  , 'nmap.' ,   'back.'  , 'warezclient.'   , 'teardrop.' ,  'pod.'  ,'guess_passwd.' ,    'buffer_overflow.'  ,'land.', 'warezmaster.', 'imap.', 'rootkit.', 'loadmodule.',  'ftp_write.', 'multihop.' ,  'phf.'  ,  'perl.',    'spy.'],['dos','dos' , 'normal' , 'probe',  'probe' , 'probe'  , 'probe' ,   'dos'  , 'r2l'   , 'dos' ,  'dos'  ,'r2l' ,    'u2r'  ,'dos', 'r2l', 'r2l', 'u2r', 'u2r',  'r2l', 'r2l' ,  'r2l'  ,  'u2r',    'r2l'],inplace=True)





#for test-set
kdd_dataset['label'].replace(['snmpgetattack.','mailbomb.','snmpguess.','mscan.','apache2.','processtable.','saint.','httptunnel.','named.','sendmail.','ps.','xterm.','xlock.','xsnoop.','sqlattack.','worm.','udpstorm.'],['r2l','dos','r2l','probe','dos','dos','probe','r2l','r2l','r2l','u2r','u2r','r2l','r2l','u2r','r2l','dos'],inplace=True)



#kdd_dataset.to_csv('TempTest.txt',sep='\t',header=False,index=False)
kdd_dataset.to_csv('LabelledTrain.txt',header=False,index=False)

#insert following in a new file

#le_ptype=preprocessing.LabelEncoder()#Texts Needs to be handelled differently
#le_service=preprocessing.LabelEncoder()#Texts Needs to be handelled differently
#le_flag=preprocessing.LabelEncoder()#Texts Needs to be handelled differently
#le_land=preprocessing.LabelEncoder()#
#le_loggedin=preprocessing.LabelEncoder()#
#le_ishostlogin=preprocessing.LabelEncoder()
#le_isguestlogin=preprocessing.LabelEncoder()
#le_root_shell=preprocessing.LabelEncoder()
#le_su_attempted=preprocessing.LabelEncoder()
#Convert to Labels
#data.protocol_type=le_ptype.fit_transform(data.protocol_type)#Texts Needs to be handelled differently
#data.service=le_service.fit_transform(data.service)#Texts Needs to be handelled differently
#data.flag=le_flag.fit_transform(data.flag)#Texts Needs to be handelled differently
#data.land=le_land.fit_transform(data.land)#
#data.logged_in=le_loggedin.fit_transform(data.logged_in)#
#data.is_host_login=le_ishostlogin.fit_transform(data.is_host_login)
#data.is_guest_login=le_isguestlogin.fit_transform(data.is_guest_login)
#data.root_shell=le_root_shell.fit_transform(data.root_shell)
#data.su_attempted=le_su_attempted.fit_transform(data.su_attempted)

