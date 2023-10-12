import requests

if __name__ == "__main__":
    # Example loan application
    application = {
        " Destination Port": -0.37317513441427996,
        " Flow Duration": -0.5661854195805945,
        " Total Fwd Packets": -0.009021207040715472,
        "Total Length of Fwd Packets": -0.05684448078767351,
        " Fwd Packet Length Max": -0.28889736015641687,
        " Fwd Packet Length Min": -0.24532450577684167,
        " Fwd Packet Length Mean": -0.26469567858814613,
        "Bwd Packet Length Max": 1.3272162985826161,
        " Bwd Packet Length Min": -0.4497195128724976,
        "Flow Bytes/s": -0.0414942269636252,
        " Flow Packets/s": -0.21604372098769803,
        " Flow IAT Mean": -0.36437003995260475,
        " Flow IAT Std": -0.4955904132454165,
        " Flow IAT Min": -0.0733433702601763,
        " Fwd IAT Mean": -0.4082606796525462,
        " Fwd IAT Std": -0.5187690076370991,
        " Fwd IAT Min": -0.12376001768515836,
        "Bwd IAT Total": -0.319415337815444,
        " Bwd IAT Mean": -0.20978942717681234,
        " Bwd IAT Std": -0.2209049746399047,
        " Bwd IAT Max": -0.2548669532052559,
        " Bwd IAT Min": -0.11262558409383355,
        "Fwd PSH Flags": -0.19121248283137302,
        " Fwd URG Flags": -0.00648889099737826,
        " Fwd Header Length": 0.0024793347052920437,
        " Bwd Packets/s": -0.18804439409469392,
        " Min Packet Length": -0.46169789037682046,
        " Packet Length Variance": 1.270929132205581,
        "FIN Flag Count": -0.26816736959461834,
        " RST Flag Count": -0.01123956215190286,
        " PSH Flag Count": 1.2821151368473633,
        " ACK Flag Count": -0.7167641150935132,
        " URG Flag Count": -0.25626028053337635,
        " Down/Up Ratio": 2.065801905131256,
        "Init_Win_bytes_forward": 0.029672579613428507,
        " Init_Win_bytes_backward": -0.1730173925094681,
        " act_data_pkt_fwd": -0.004426387101004908,
        "Active Mean": -0.1560887034727364,
        " Active Std": -0.09822171846417006,
        " Active Max": -0.1678713817295027,
        " Active Min": -0.1333685844671758,
        " Idle Std": -0.1588634648709423
    }

    # Location of my server
    url = "http://0.0.0.0:8989/predict"

    # request
    resp = requests.post(url, json=application)

    # Print result
    print(resp.json())
