from zk import ZK, const

def get_users(device_ip) :
    conn = None
    zk = ZK(device_ip, port=4370, timeout=5)

    try:
        print('Connecting to device ...')
        conn = zk.connect()
        print('Disabling device ...')
        conn.disable_device()
        print('Firmware Version: {}'.format(conn.get_firmware_version()))
        users = conn.get_users()
        print('Enabling device ...')
        conn.enable_device()
        user_dicts = []
        for user in users :
            user_dicts.append({
                        'name': user.name,
                        'user_id': user.user_id,
                    })
        return user_dicts
    except Exception as e:
        print("Process terminated: {}".format(e))
    finally:
        if conn:
            conn.disconnect()