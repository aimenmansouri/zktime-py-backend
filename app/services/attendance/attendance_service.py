from zk import ZK, const
from datetime import datetime , timedelta

def get_attendance(device_ip , start_date , end_date) :
    conn = None
    zk = ZK(device_ip, port=4370, timeout=10)

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)

    try:
        print('Connecting to device ...')
        conn = zk.connect()
        print('Disabling device ...')
        conn.disable_device()
        print('Firmware Version: {}'.format(conn.get_firmware_version()))
        atts = conn.get_attendance()
        print('Enabling device ...')
        filtred_atts = [i for i in atts if (i.timestamp >= start_date and i.timestamp <= end_date)]
        conn.enable_device()
        atts_dicts = []
        for att in filtred_atts :
            atts_dicts.append({
                        'user_id': att.user_id,
                        'timestamp': att.timestamp,
                        'att_uid' : f"{att.uid}-{device_ip}",
                    })
        return atts_dicts
    except Exception as e:
        print("Process terminated: {}".format(e))
    finally:
        if conn:
            conn.disconnect()