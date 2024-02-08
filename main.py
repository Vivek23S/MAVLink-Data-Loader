import mavlink_mat_file_loader

filename = 'Test1.bin-350233.mat'
params = ['AHR2','ATT','BARO_0','BAT_0','GPS_0','XKF1_0','RATE','RCOU']

dt = mavlink_mat_file_loader.data(filename,params)

