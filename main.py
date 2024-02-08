import mavlink_mat_file_loader

filename = 'filename.mat'
params = ['AHR2','ATT','BARO_0','BAT_0','GPS_0','XKF1_0','RATE','RCOU']

dt = mavlink_mat_file_loader.data(filename,params)
labels = mavlink_mat_file_loader.label(filename,params)

print(labels)
#----------------------------EXPECTED OUTCOME----------------------------
#       AHR2       ATT   BARO_0     BAT_0   GPS_0  XKF1_0    RATE    RCOU
# 0   LineNo    LineNo   LineNo    LineNo  LineNo  LineNo  LineNo  LineNo
# 1   TimeUS    TimeUS   TimeUS    TimeUS  TimeUS  TimeUS  TimeUS  TimeUS
# 2     Roll   DesRoll        I  Instance       I       C    RDes      C1
# 3    Pitch      Roll      Alt      Volt  Status    Roll       R      C2
# 4      Yaw  DesPitch    Press     VoltR     GMS   Pitch    ROut      C3
# 5      Alt     Pitch     Temp      Curr     GWk     Yaw    PDes      C4
# 6      Lat    DesYaw      CRt   CurrTot   NSats      VN       P      C5
# 7      Lng       Yaw      SMS   EnrgTot    HDop      VE    POut      C6
# 8       Q1     ErrRP   Offset      Temp     Lat      VD    YDes      C7
# 9       Q2    ErrYaw  GndTemp       Res     Lng     dPD       Y      C8
# 10      Q3      AEKF   Health    RemPct     Alt      PN    YOut      C9
# 11      Q4                                  Spd      PE    ADes     C10
# 12                                         GCrs      PD       A     C11
# 13                                           VZ      GX    AOut     C12
# 14                                          Yaw      GY             C13
# 15                                            U      GZ             C14
# 16                                                   OH

# parameters.txt is attached in the repository explaining each datasets

# consider one want to look at roll data
roll_1 = dt['AHR2']['Roll']
roll_2 = dt['ATT']['Roll']
roll_3 = dt['XKF1_0']['Roll']

# consider one want to look at alt data
alt_1 = dt['AHR2']['Alt']
alt_2 = dt['BARO_0']['Alt']
alt_3 = dt['GPS_0']['Alt']

# ALTHOUGH TIME DATA IS AVAILABLE IN EACH DATA-SET BUT IN CASE ONE WANTS IT IN SIMPLER FORM THEN BELOW IS USEFUL
# TO RUN THIS WITHOUT ANY ERROR MAKE SURE YOU DONT CHANGE FILENAME AFTER DOWNLOADING IT FROM THE VEHICLE

typical_filename = '2022-06-28 10-49-39.bin-644548.mat'
time = mavlink_mat_file_loader.timedata(filename,params)



















