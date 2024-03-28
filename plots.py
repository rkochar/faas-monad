import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def user_survey():
    data = {
        'Q3': [4, 8, 3, 1, 2, 1, 2, 1, 2, 2, 3, 1, 3, 2, 2],
        'Q4': [1, 6, 3, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
        'Q5': [8, 9, 7, 9, 7, 9, 7, 7, 8, 5, 8, 9, 9, 8, 10],
        'Q6': [8, 8, 8, 9, 8, 9, 8, 8, 8, 8, 8, 9, 8, 7, 9],
        'Q7': [8, 9, 6, 8, 7, 9, 6, 7, 9, 9, 8, 8, 8, 7, 7],
        'Q8': [7, 8, 7, 9, 9, 9, 8, 5, 7, 9, 8, 9, 9, 8, 10],
        'Q9': [8, 7, 6, 7, 8, 9, 6, 4, 7, 9, 8, 8, 9, 6, 9],
        'Q10': [9, 8, 6, 8, 7, 8, 7, 7, 9, 9, 8, 9, 8, 7, 10],
        'Q11': [7, 8, 6, 8, 7, 9, 7, 6, 8, 7, 8, 8, 7, 7, 6]
    }
    df_survey = pd.DataFrame(data)
    print(df_survey.describe())
    df_survey.boxplot(column=list(df_survey.columns))
    plt.show()
    sns.boxplot(data=df_survey)
    plt.show()


def make_vertical_box_plots(df1, df2, title, title1, title2, xlabel=None, ylabel=None, fontsize=12):
    sns.set(font_scale=1.5)

    fig, axs = plt.subplots(1, 2, figsize=(10, 8))
    sns.boxplot(data=df1, ax=axs[0])
    sns.boxplot(data=df2, ax=axs[1])
    fig.suptitle(title)
    axs[0].set_title(title1)
    axs[1].set_title(title2)
    if xlabel is not None:
        axs[0].set_xlabel(xlabel)
        axs[1].set_xlabel(xlabel)
    if type(ylabel) is tuple:
        axs[0].set_ylabel(ylabel[0])
        axs[1].set_ylabel(ylabel[1])
    elif ylabel is not None:
        axs[0].set_ylabel(ylabel)
        axs[1].set_ylabel(ylabel)
        axs[0].fontsize = fontsize
    plt.tight_layout()
    plt.show()


def boxplotaws(df1, title, xlabel=None, ylabel=None):
    sns.set(font_scale=1.5)
    sns.boxplot(data=df1)
    plt.title(title)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def aws_box_plot(df1, df2, df_aws, title, title1, title2, title_aws, xlabel=None, ylabel=None, figsize=(12, 8)):
    sns.set(font_scale=1.5)
    fig, axs = plt.subplots(1, 3, figsize=figsize)
    sns.boxplot(data=df1, ax=axs[0])
    sns.boxplot(data=df2, ax=axs[1])
    sns.boxplot(data=df_aws, ax=axs[2])
    fig.suptitle(title)
    axs[0].set_title(title1)
    axs[1].set_title(title2)
    axs[2].set_title(title_aws)
    if xlabel is not None:
        axs[0].set_xlabel(xlabel)
        axs[1].set_xlabel(xlabel)
        axs[2].set_xlabel(xlabel)
    if ylabel is not None:
        axs[0].set_ylabel(ylabel)
        axs[1].set_ylabel(ylabel)
        axs[2].set_ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def latency_plots(xs, title, xlabel, ylabel, dashes=True, figsize=(10, 5)):
    sns.set(font_scale=1.5)
    # Seaborn lineplot
    plt.figure(figsize=figsize)
    sns.lineplot(data=xs, dashes=dashes)
    if dashes:
        for line in plt.gca().lines:
            line.set_linestyle("--")
        #ax.lines[0].set_linestyle("--")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.tight_layout()
    plt.show()


def compare_latencies(df1, df2, title, xlabel, ylabel, figsize=(10, 5)):
    plt.subplots(figsize=figsize)
    sns.set(font_scale=1.5)
    sns.lineplot(data=df2, dashes=True)
    for line in plt.gca().lines:
        line.set_linestyle("--")
    sns.lineplot(data=df1, dashes=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.tight_layout()
    plt.show()



def add_list(xs, ys):
    return [sum(x) for x in zip(xs, ys)]


def mvcc():
    kubernetes_v1_control_time = [0.793475, 1.013997, 0.516335, 0.396327, 0.725422, 0.206179, 1.021480, 1.019803, 0.997738, 1.018675]
    kubernetes_v1_control_ram = [37520, 37520, 37520, 37520, 37520, 37520, 37520, 37520, 37520, 37520]
    kubernetes_v1_worker_time = [0.378776, 1.024018, 0.020771, 0.027789, 1.004755, 0.023494, 0.504497, 1.017287, 1.014095, 1.003820]
    kubernetes_v1_worker_ram = [37312, 37312, 37440, 37312, 37312, 37312, 37312, 37312, 37312, 37312]

    aws_native_v1_control_time = [0.136501, 0.145205, 0.109854, 0.137513, 0.128829, 0.145179, 0.135313, 0.133055, 0.145302, 0.140627]
    aws_native_v1_control_ram = [37632, 37632, 37368, 37368, 37368, 37368, 37368, 37368, 37632, 37632]
    aws_native_v1_worker_time = [0.109614, 0.118489, 0.112408, 0.110375, 0.118503, 0.115700, 0.124081, 0.105847, 0.122305, 0.126024]
    aws_native_v1_worker_ram = [47088, 47088, 47088, 47088, 47088, 47088, 47352, 47352, 47352, 47352]

    gcp_native_v1_control_time = [1.491859, 1.867794, 1.772979, 1.227144, 1.165873, 1.001101, 0.981884, 1.105514, 1.513661, 0.861779]
    gcp_native_v1_control_ram = [160448, 122304, 126456, 130636, 134804, 139640, 143804, 147976, 152120, 156296]
    gcp_native_v1_worker_time = [1.899105, 1.037837, 0.892350, 1.026456, 1.862277, 1.025851, 0.823755, 1.209156, 1.268427, 1.209156]
    gcp_native_v1_worker_ram = [149624, 149568, 149512, 149136, 149076, 148940, 148764, 148764, 148448, 147044]

    gcp_msa_v1_control_time = [1.649685, 1.610865, 0.996971, 1.939060, 1.931674, 1.589383, 1.327237, 1.458381, 1.909028, 1.282464]
    gcp_msa_v1_control_ram = [142972, 151352, 159688, 168060, 177444, 186012, 194600, 203536, 212292, 220952]
    gcp_msa_v1_worker_time = [1.274210, 1.167855, 0.778846, 1.016076, 0.815231, 0.790300, 0.996067, 0.918585, 2.160582, 0.868658]
    gcp_msa_v1_worker_ram = [125500, 125720, 125720, 130460, 133648, 135908, 138128, 138640, 138852, 138908]

    aws_msa_v1_control_time = [0.132978, 0.141185, 0.132538, 0.142153, 0.139308, 0.129953, 0.130069, 0.128658, 0.125790, 0.142757]
    aws_msa_v1_control_ram = [37364, 37364, 37364, 37364, 37364, 37364, 37364, 37628, 37628, 37628]
    aws_msa_v1_worker_time = [0.108650, 0.105267, 0.091029, 0.093328, 0.104633, 0.118187, 0.105994, 0.099929, 0.101294, 0.118012]
    aws_msa_v1_worker_ram = [46964, 46964, 46964, 46964, 46964, 46964, 47228, 47228, 47228, 47228]

    kubernetes_v2_control_time = [1.009957, 0.024368, 0.042323, 0.0314412, 0.048122, 0.993633, 0.066280, 0.078494, 0.032028, 0.146135]
    kubernetes_v2_control_ram = [37556, 37592, 37592, 37592, 37592, 37592, 37556, 37592, 37592, 37592]
    kubernetes_v2_worker_time = [0.033896, 0.039033, 0.030928, 0.034017, 0.032511, 1.011317, 1.007928, 0.040851, 0.030660, 1.028882]
    kubernetes_v2_worker_ram = [37584, 37584, 37584, 37584, 37584, 37584, 37584, 37584, 37584, 37584]

    aws_native_v2_control_time = [0.219537, 0.217846, 0.216031, 0.244741, 0.241034, 0.225464, 0.216542, 0.218291, 0.219074, 0.221688]
    aws_native_v2_control_ram = [37892, 37892, 37892, 37892, 37892, 37892, 37892, 37628, 37628, 37628]
    aws_native_v2_worker_time = [0.195900, 0.224261, 0.208464, 0.243186, 0.237011, 0.228803, 0.215098, 0.212448, 0.227427, 0.239786]
    aws_native_v2_worker_ram = [47616, 47616, 47616, 47616, 47352, 47352, 47352, 47352, 47352, 47352]

    aws_msa_v2_control_time = [0.260230, 0.250721, 0.247342, 0.252537, 0.244680, 0.413190, 0.245428, 0.256091, 0.265146, 0.260541]
    aws_msa_v2_control_ram = [38152, 38152, 38152, 38152, 38152, 38152, 38152, 37888, 37888, 37888]
    aws_msa_v2_worker_time = [0.147283, 0.137341, 0.142359, 0.143085, 0.146324, 0.180492, 0.148517, 0.150734, 0.009314, 0.148677]
    aws_msa_v2_worker_ram = [47804, 47804, 47804, 47540, 47540, 47540, 47540, 47540, 47540, 47540]

    gcp_native_v2_control_time = [0.830406, 1.313704, 0.712170, 1.214612, 0.954179, 0.777318, 1.289387, 0.863902, 0.839105, 0.933404]
    gcp_native_v2_control_ram = [123920, 123976, 126780, 129556, 130192, 130436, 137720, 133512, 133376, 130832]
    gcp_native_v2_worker_time = [1.074226, 1.337669, 1.106108, 0.733345, 1.608533, 1.123138, 1.246236, 1.189588, 0.895781, 0.818517]
    gcp_native_v2_worker_ram = [139660, 139724, 139924, 141436, 141436, 141644, 141692, 144064, 144064, 144064]

    gcp_msa_v2_control_time = [0.522187, 0.640480, 1.046779, 0.809641, 0.650032, 1.795502, 1.547599, 1.302985, 0.657659, 0.986754]
    gcp_msa_v2_control_ram = [125224, 125828, 126200, 126256, 126584, 126936, 127524, 127884, 128500, 114800]
    gcp_msa_v2_worker_time = [0.979372, 0.472925, 0.856171, 0.631772, 0.764715, 1.530403, 0.952578, 0.896151, 0.764199, 1.195980]
    gcp_msa_v2_worker_ram = [152768, 148336, 148336, 147888, 147732, 147256, 147200, 147144, 146824, 146240]

    # Add control and worker times
    kubernetes_v1_latency = add_list(kubernetes_v1_control_time, kubernetes_v1_worker_time)
    aws_native_v1_latency = add_list(aws_native_v1_control_time, aws_native_v1_worker_time)
    gcp_native_v1_latency = add_list(gcp_native_v1_control_time, gcp_native_v1_worker_time)
    gcp_msa_v1_latency = add_list(gcp_msa_v1_control_time, gcp_msa_v1_worker_time)
    aws_msa_v1_latency = add_list(aws_msa_v1_control_time, aws_msa_v1_worker_time)
    df_v1_latency = pd.DataFrame({
        "Kubernetes": kubernetes_v1_latency,
        "AWS Native": aws_native_v1_latency,
        "AWS MSA": aws_msa_v1_latency,
        "GCP Native": gcp_native_v1_latency,
        "GCP MSA": gcp_msa_v1_latency
    })
    #print("df_v1_latency")
    #print(df_v1_latency.describe())
    #print('\n')
    latency_plots(df_v1_latency, "Latency of MVCC (v1)", "Invocation", "Time (s)", dashes=False)

    kubernetes_v2_latency = add_list(kubernetes_v2_control_time, kubernetes_v2_worker_time)
    aws_native_v2_latency = add_list(aws_native_v2_control_time, aws_native_v2_worker_time)
    aws_msa_v2_latency = add_list(aws_msa_v2_control_time, aws_msa_v2_worker_time)
    gcp_native_v2_latency = add_list(gcp_native_v2_control_time, gcp_native_v2_worker_time)
    gcp_msa_v2_latency = add_list(gcp_msa_v2_control_time, gcp_msa_v2_worker_time)
    df_v2_latency = pd.DataFrame({
        "Kubernetes": kubernetes_v2_latency,
        "AWS Native": aws_native_v2_latency,
        "AWS MSA": aws_msa_v2_latency,
        "GCP Native": gcp_native_v2_latency,
        "GCP MSA": gcp_msa_v2_latency
    })
    #print("df_v2_latency")
    #print(df_v2_latency.describe())
    #print('\n')
    latency_plots(df_v2_latency, "Latency of MVCC (latency optimized)", "Invocation", "Time (s)", dashes=True)

    # Compare latencies
    df_aws_latency_v1 = pd.DataFrame({
        "AWS Native v1": aws_native_v1_latency,
        "AWS MSA v1": aws_msa_v1_latency,
    })
    df_aws_latency_v2 = pd.DataFrame({
        "AWS Native lo": aws_native_v2_latency,
        "AWS MSA lo": aws_msa_v2_latency,
    })
    compare_latencies(df_aws_latency_v1, df_aws_latency_v2, "Latency of MVCC (v1 vs latency optimized)", "Invocation", "Time (s)")

    df_aws_latency_v1 = pd.DataFrame({
        "AWS Native v1": aws_native_v1_latency,
        "AWS MSA v1": aws_msa_v1_latency,
        "Kubernetes v1": kubernetes_v1_latency
    })
    df_aws_latency_v2 = pd.DataFrame({
        "AWS Native lo": aws_native_v2_latency,
        "AWS MSA lo": aws_msa_v2_latency,
        "Kubernetes lo": kubernetes_v2_latency
    })
    compare_latencies(df_aws_latency_v1, df_aws_latency_v2, "Latency of MVCC (v1 vs latency optimized)", "Invocation", "Time (s)")

    df_gcp_latency_v1 = pd.DataFrame({
        "GCP Native v1": gcp_native_v1_latency,
        "GCP MSA v1": gcp_msa_v1_latency,
    })
    df_gcp_latency_v2 = pd.DataFrame({
        "GCP Native lo": gcp_native_v2_latency,
        "GCP MSA lo": gcp_msa_v2_latency,
    })
    compare_latencies(df_gcp_latency_v1, df_gcp_latency_v2, "Latency of MVCC (v1 vs latency optimized)", "Invocation", "Time (s)")


    df_gcp_latency_v1 = pd.DataFrame({
        "GCP Native v1": gcp_native_v1_latency,
        "GCP MSA v1": gcp_msa_v1_latency,
        "Kubernetes v1": kubernetes_v1_latency
    })
    df_gcp_latency_v2 = pd.DataFrame({
        "GCP Native lo": gcp_native_v2_latency,
        "GCP MSA lo": gcp_msa_v2_latency,
        "Kubernetes lo": kubernetes_v2_latency
    })
    compare_latencies(df_gcp_latency_v1, df_gcp_latency_v2, "Latency of MVCC (v1 vs latency optimized)", "Invocation", "Time (s)")

    #df_control_v1_time = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v1_control_time,
    #    "AWS\nNative": aws_native_v1_control_time,
    #    "AWS\nMSA": aws_msa_v1_control_time,
    #    "GCP\nNative": gcp_native_v1_control_time,
    #    "GCP\nMSA": gcp_msa_v1_control_time
    #})
    #print("df_control_v1_time")
    #print(df_control_v1_time.describe())
    #print('\n')

    #df_worker_v1_time = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v1_worker_time,
    #    "AWS\nNative": aws_native_v1_worker_time,
    #    "AWS\nMSA": aws_msa_v1_worker_time,
    #    "GCP\nNative": gcp_native_v1_worker_time,
    #    "GCP\nMSA": gcp_msa_v1_worker_time
    #})
    #print("df_worker_v1_time")
    #print(df_worker_v1_time.describe())
    #print('\n')

    #df_aws_v1_time = pd.DataFrame({
    #    "Worker\nNative": aws_native_v1_worker_time,
    #    "Worker\nMSA": aws_msa_v1_worker_time,
    #    "Control\nNative": aws_native_v1_control_time,
    #    "Control\nMSA": aws_msa_v1_control_time,
    #})

    #make_vertical_box_plots(df_worker_v1_time, df_control_v1_time, "MVCC execution time (v1)", "Worker", "Control", None, "Time (s)", fontsize=20)
    #boxplotaws(df_aws_v1_time, "MVCC execution time (Zoom in on AWS)", "AWS", "Time (s)")
    ##aws_box_plot(df_worker_v1_time, df_control_v1_time, df_aws_v1_time, "MVCC execution time (v1)", "Worker", "Control", "AWS", None, "Time (s)")

    #df_control_v1_ram = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v1_control_ram,
    #    "AWS\nNative": aws_native_v1_control_ram,
    #    "AWS\nMSA": aws_msa_v1_control_ram,
    #    "GCP\nNative": gcp_native_v1_control_ram,
    #    "GCP\nMSA": gcp_msa_v1_control_ram
    #})
    #print("df_control_v1_ram")
    #print(df_control_v1_ram.describe())
    #print('\n')

    #df_worker_v1_ram = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v1_worker_ram,
    #    "AWS\nNative": aws_native_v1_worker_ram,
    #    "AWS\nMSA": aws_msa_v1_worker_ram,
    #    "GCP\nNative": gcp_native_v1_worker_ram,
    #    "GCP\nMSA": gcp_msa_v1_worker_ram
    #})
    #print("df_worker_v1_ram")
    #print(df_worker_v1_ram.describe())
    #print('\n')

    #df_aws_v1_ram = pd.DataFrame({
    #    "Worker\nKuber-\nnetes": kubernetes_v1_worker_ram,
    #    "Worker\nNative": aws_native_v1_worker_ram,
    #    "Worker\nMSA": aws_msa_v1_worker_ram,
    #    "Control\nKuber-\nnetes": kubernetes_v1_control_ram,
    #    "Control\nNative": aws_native_v1_control_ram,
    #    "Control\nMSA": aws_msa_v1_control_ram,
    #})

    #make_vertical_box_plots(df_worker_v1_ram, df_control_v1_ram, "MVCC RAM usage (v1)", "Worker", "Control", None, "RAM (KB)", fontsize=10)
    #boxplotaws(df_aws_v1_ram, "MVCC RAM usage v1 (Zoom in on AWS & Kubernetes)", "Kubernetes and AWS", "RAM (KB)")
    ##aws_box_plot(df_worker_v1_ram, df_control_v1_ram, df_aws_v1_ram, "MVCC RAM usage (v1)", "Worker", "Control", "Kubernetes and AWS", None, "RAM (KB)", figsize=(14, 8))

    #df_worker_v2_time = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v2_worker_time,
    #    "AWS\nNative": aws_native_v2_worker_time,
    #    "AWS\nMSA": aws_msa_v2_worker_time,
    #    "GCP\nNative": gcp_native_v2_worker_time,
    #    "GCP\nMSA": gcp_msa_v2_worker_time
    #})
    #print("df_worker_v2_time")
    #print(df_worker_v2_time.describe())
    #print('\n')

    #df_control_v2_time = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v2_control_time,
    #    "AWS\nNative": aws_native_v2_control_time,
    #    "AWS\nMSA": aws_msa_v2_control_time,
    #    "GCP\nNative": gcp_native_v2_control_time,
    #    "GCP\nMSA": gcp_msa_v2_control_time
    #})

    #df_aws_v2_time = pd.DataFrame({
    #    "Worker\nKuber-\nnetes": kubernetes_v2_worker_time,
    #    "Worker\nNative": aws_native_v2_worker_time,
    #    "Worker\nMSA": aws_msa_v2_worker_time,
    #    "Control\nKuber-\nnetes": kubernetes_v2_control_time,
    #    "Control\nNative": aws_native_v2_control_time,
    #    "Control\nMSA": aws_msa_v2_control_time,
    #})
    #make_vertical_box_plots(df_worker_v2_time, df_control_v2_time, "MVCC (latency optimized) execution time", "Worker", "Control", None, "Time (s)")
    #boxplotaws(df_aws_v2_time, "MVCC (latency optimized) execution time (Zoom in an AWS & Kubernetes)", "AWS", "Time (s)")
    ##aws_box_plot(df_worker_v2_time, df_control_v2_time, df_aws_v2_time, "MVCC (latency optimized) execution time", "Worker", "Control", "AWS", None, "Time (s)", figsize=(12, 8))

    #print("df_control_v2_time")
    #print(df_control_v2_time.describe())
    #print('\n')

    #df_control_v2_ram = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v2_control_ram,
    #    "AWS\nNative": aws_native_v2_control_ram,
    #    "AWS\nMSA": aws_msa_v2_control_ram,
    #    "GCP\nNative": gcp_native_v2_control_ram,
    #    "GCP\nMSA": gcp_msa_v2_control_ram
    #})
    #print("df_control_v2_ram")
    #print(df_control_v2_ram.describe())
    #print('\n')

    #df_worker_v2_ram = pd.DataFrame({
    #    "Kuber-\nnetes": kubernetes_v2_worker_ram,
    #    "AWS\nNative": aws_native_v2_worker_ram,
    #    "AWS\nMSA": aws_msa_v2_worker_ram,
    #    "GCP\nNative": gcp_native_v2_worker_ram,
    #    "GCP\nMSA": gcp_msa_v2_worker_ram
    #})
    #print("df_worker_v2_ram")
    #print(df_worker_v2_ram.describe())
    #print('\n')

    #df_aws_v2_ram = pd.DataFrame({
    #    "Worker\nKuber-\nnetes": kubernetes_v2_worker_ram,
    #    "Worker\nAWS\nNative": aws_native_v2_worker_ram,
    #    "Worker\nAWS\nMSA": aws_msa_v2_worker_ram,
    #    "Control\nKuber-\nnetes": kubernetes_v2_control_ram,
    #    "Control\nAWS\nNative": aws_native_v2_control_ram,
    #    "Control\nAWS\nMSA": aws_msa_v2_control_ram,
    #})
    #make_vertical_box_plots(df_worker_v2_ram, df_control_v2_ram, "MVCC (latency optimized) RAM usage", "Worker", "Control", None, "RAM (KB)")
    #boxplotaws(df_aws_v2_ram, "MVCC (latency optimized) RAM usage (Zoom in on AWS & Kubernetes)", "AWS", "RAM (KB)")
    ##aws_box_plot(df_worker_v2_ram, df_control_v2_ram, df_aws_v2_ram, "MVCC (latency optimized) RAM usage", "Worker", "Control", "Kubernetes and AWS", None, "RAM (KB)", figsize=(14, 8))


def zookeeper():
    native_writer_time = [0.037113, 0.036892, 0.046870, 0.038474, 0.060027, 0.038963, 0.038126, 0.038587, 0.039149, 0.040490]
    native_writer_ram = [47976, 47976, 47976, 47976, 47976, 47976, 47976, 47976, 47976, 47976]
    native_distributor_time = [0.085641, 0.106650, 0.212175, 0.125171, 0.113983, 0.121254, 0.122602, 0.114562, 0.101404, 0.108597]
    native_distributor_ram = [51552, 51552, 51552, 51552, 51552, 51552, 51552, 51552, 51552, 51552]

    msa_writer_time = [0.215296, 0.047078, 0.053788, 0.062924, 0.220363, 0.044693, 0.038598, 0.050149, 0.044993, 0.055103]
    msa_writer_ram = [48776, 48776, 48776, 48776, 48776, 49564, 49564, 49564, 49564, 49564]
    msa_distributor_time = [0.418039, 0.169950, 0.240719, 0.134873, 0.440069, 0.235175, 0.060217, 0.149766, 0.216456, 0.219520]
    msa_distributor_ram = [52376, 52376, 52376, 52376, 52376, 52376, 52376, 52376, 52376, 52376]

    zookeeper_time = pd.DataFrame({
        "FaaS-\nKeeper\nWriter": native_writer_time,
        "MSA\nWriter": msa_writer_time,
        "FaaS-\nKeeper\nDistri-\nbutor": native_distributor_time,
        "MSA\nDistri-\nbutor": msa_distributor_time
    })
    print("zookeeper_time")
    print(zookeeper_time.describe())
    print('\n')

    zookeeper_ram = pd.DataFrame({
        "FaaS-\nKeeper\nWriter": native_writer_ram,
        "MSA\nWriter": msa_writer_ram,
        "FaaS-\nKeeper\nDistri-\nbutor": native_distributor_ram,
        "MSA\nDistri-\nbutor": msa_distributor_ram
    })
    print("zookeeper_ram")
    print(zookeeper_ram.describe())
    print('\n')
    make_vertical_box_plots(zookeeper_time, zookeeper_ram, "Zookeeper in AWS", "Execution Time", "RAM", None, ("Time (s)", "RAM (KB)"))

    zookeeper_latency = pd.DataFrame({
        "FaaSKeeper": add_list(native_writer_time, native_distributor_time),
        "MSA": add_list(msa_writer_time, msa_distributor_time)
    })
    print("zookeeper_latency")
    print(zookeeper_latency.describe())
    print('\n')
    latency_plots(zookeeper_latency, "Latency in Zookeeper", "Invocation", "Time (s)")

def mapreduce():
    d1_refarch_mapper_time = [0.121655, 0.122471, 0.121669, 0.118316, 0.092190, 0.058335, 0.113302, 0.085759, 0.086814, 0.120649]
    d1_refarch_mapper_ram = [45880, 45880, 45880, 45880, 45880, 45088, 45088, 45088, 46144, 46144]

    d1_aws_mapper_time = [0.374481, 0.306901, 0.345849, 0.155812, 0.323350, 0.316980, 0.322199, 0.320986, 0.339833, 0.299038]
    d1_aws_mapper_ram = [47636, 47636, 47636, 47636, 47636, 47372, 47372, 47372, 47372, 47372]
    d1_aws_reducer_time = [0.103112, 0.135336, 0.093015, 0.197104, 0.191298, 0.178675, 0.148307, 0.118185, 0.115601, 0.138269]
    d1_aws_reducer_ram = [47180, 47180, 47180, 47180, 47180, 47180, 46916, 46916, 46916, 46916]

    d1_gcp_mapper_time = [0.229457, 0.203519, 0.251336, 0.286550, 0.273870, 0.218811, 0.199010, 0.200595, 0.198554, 0.270467]
    d1_gcp_mapper_ram = [57472, 57472, 57472, 57472, 57472, 57472, 57472, 57472, 57472, 57472]
    d1_gcp_reducer_time = [0.121239, 0.127765, 0.128168, 0.234405, 0.160193, 0.147104, 0.130153, 0.223740, 0.133132, 0.169556]
    d1_gcp_reducer_ram = [57388, 57388, 57388, 57388, 57388, 57260, 57260, 57388, 57388, 57388]

    d2_refarch_mapper_time = [0.115704, 0.108881, 0.127877, 0.079823, 0.099283, 0.079823, 0.127877, 0.091940, 0.100953, 0.110815]
    d2_refarch_mapper_ram = [46144, 46144, 46144, 46144, 45876, 45876, 45876, 45876, 45876, 45876]

    d2_aws_mapper_time = [0.343974, 0.209806, 0.348801, 0.377183, 0.392374, 0.357081, 0.390687, 0.354244, 0.364568, 0.216755]
    d2_aws_mapper_ram = [47604, 47340, 47340, 47340, 47340, 47340, 47076, 47076, 47076, 47076]
    d2_aws_reducer_time = [0.278712, 0.161795, 0.274752, 0.322493, 0.320085, 0.337038, 0.275484, 0.286035, 0.283580, 0.160220]
    d2_aws_reducer_ram = [47188, 47188, 47188, 47188, 47188, 47452, 47452, 47452, 47452, 47452]

    d2_gcp_mapper_time = [0.457935, 0.388853, 0.415447, 0.598263, 0.434647, 0.437866, 0.475297, 0.515363, 0.368016, 0.359398]
    d2_gcp_mapper_ram = [55812, 55812, 55812, 55812, 55800, 55800, 55800, 55796, 55796, 55796]
    d2_gcp_reducer_time = [0.356580, 0.286534, 0.203414, 0.181540, 0.291301, 0.135925, 0.174785, 0.211402, 0.217848, 0.270040]
    d2_gcp_reducer_ram = [57920, 57920, 57920, 57920, 57920, 57556, 57556, 57556, 57920, 57920]

    d3_refarch_mapper_time = [0.259188, 0.164671, 0.229451, 0.250591, 0.149541, 0.265715, 0.171741, 0.239006, 0.158177, 0.161975]
    d3_refarch_mapper_ram = [44092, 45676, 44164, 44136, 44044, 45628, 43920, 43980, 44044, 44028]

    d3_aws_mapper_time = [0.306391, 0.459464, 0.444042, 0.431296, 0.443612, 0.445281, 0.476763, 0.448426, 0.536684, 0.420338]
    d3_aws_mapper_ram = [47480, 47216, 47216, 47216, 47216, 47216, 47216, 46952, 46952, 46952]
    d3_aws_reducer_time = [0.168889, 0.285866, 0.279483, 0.285159, 0.297057, 0.282081, 0.284532, 0.278014, 0.300545, 0.290419]
    d3_aws_reducer_ram = [46856, 46856, 46856, 46856, 47120, 47120, 47120, 47120, 47120, 47120]

    d3_gcp_mapper_time = [0.656728, 0.601116, 0.615589, 0.581839, 0.580846, 0.669007, 0.677443, 0.681872, 0.695932, 0.665682]
    d3_gcp_mapper_ram = [56648, 56652, 56660, 56660, 56660, 56664, 56664, 56664, 56664, 56664]
    d3_gcp_reducer_time = [0.134706, 0.172939, 0.174369, 0.203405, 0.2429747, 0.190187, 0.133671, 0.226952, 0.181092, 0.204350]
    d3_gcp_reducer_ram = [57992, 57992, 57992, 57992, 58324, 58324, 57992, 58324, 57992, 58324]

    d1_mapper_time = pd.DataFrame({
        "Refarch": d1_refarch_mapper_time,
        "AWS": d1_aws_mapper_time,
        "GCP": d1_gcp_mapper_time,
    })
    print("d1_mapper_time")
    print(d1_mapper_time.describe())
    print('\n')

    d2_mapper_time = pd.DataFrame({
        "Refarch": d2_refarch_mapper_time,
        "AWS": d2_aws_mapper_time,
        "GCP": d2_gcp_mapper_time,
    })
    print("d2_mapper_time")
    print(d2_mapper_time.describe())
    print('\n')

    d3_mapper_time = pd.DataFrame({
        "Refarch": d3_refarch_mapper_time,
        "AWS": d3_aws_mapper_time,
        "GCP": d3_gcp_mapper_time,
    })
    print('d3_mapper_time')
    print(d3_mapper_time.describe())
    print('\n')

    d1_reducer_time = pd.DataFrame({
        "AWS": d1_aws_reducer_time,
        "GCP": d1_gcp_reducer_time,
    })
    print("d1_reducer_time")
    print(d1_reducer_time.describe())
    print('\n')

    d2_reducer_time = pd.DataFrame({
        "AWS": d2_aws_reducer_time,
        "GCP": d2_gcp_reducer_time,
    })
    print("d2_reducer_time")
    print(d2_reducer_time.describe())
    print('\n')

    d3_reducer_time = pd.DataFrame({
        "AWS": d3_aws_reducer_time,
        "GCP": d3_gcp_reducer_time,
    })
    print("d3_reducer_time")
    print(d3_reducer_time.describe())
    print('\n')

    d1_mapper_ram = pd.DataFrame({
        "Refarch": d1_refarch_mapper_ram,
        "AWS": d1_aws_mapper_ram,
        "GCP": d1_gcp_mapper_ram,
    })
    print("d1_mapper_ram")
    print(d1_mapper_ram.describe())
    print('\n')

    d2_mapper_ram = pd.DataFrame({
        "Refarch": d2_refarch_mapper_ram,
        "AWS": d2_aws_mapper_ram,
        "GCP": d2_gcp_mapper_ram,
    })
    print("d2_mapper_ram")
    print(d2_mapper_ram.describe())
    print('\n')

    d3_mapper_ram = pd.DataFrame({
        "Refarch": d3_refarch_mapper_ram,
        "AWS": d3_aws_mapper_ram,
        "GCP": d3_gcp_mapper_ram,
    })
    print("d3_mapper_ram")
    print(d3_mapper_ram.describe())
    print('\n')

    d1_reducer_ram = pd.DataFrame({
        "AWS": d1_aws_reducer_ram,
        "GCP": d1_gcp_reducer_ram,
    })
    print("d1_reducer_ram")
    print(d1_reducer_ram.describe())
    print('\n')

    d2_reducer_ram = pd.DataFrame({
        "AWS": d2_aws_reducer_ram,
        "GCP": d2_gcp_reducer_ram,
    })
    print("d2_reducer_ram")
    print(d2_reducer_ram.describe())
    print('\n')

    d3_reducer_ram = pd.DataFrame({
        "AWS": d3_aws_reducer_ram,
        "GCP": d3_gcp_reducer_ram,
    })
    print("d3_reducer_ram")
    print(d3_reducer_ram.describe())
    print('\n')

    sns.set(font_scale=1.5)
    mapreduce_mapper_time = pd.DataFrame({
        "Refarch": d1_refarch_mapper_time + d2_refarch_mapper_time + d3_refarch_mapper_time,
        "AWS\nMSA": d1_aws_mapper_time + d2_aws_mapper_time + d3_aws_mapper_time,
        "GCP\nMSA": d1_gcp_mapper_time + d2_gcp_mapper_time + d3_gcp_mapper_time,
        "Dataset": (['d1'] * 10) + (['d2'] * 10) + (['d3'] * 10)
    })
    dflong_mapper_time = pd.melt(mapreduce_mapper_time, "Dataset", var_name='Variant', value_name='Time (s)')
    #fig, ax = plt.subplots(figsize=(5, 5))
    #sns.catplot(x="Variant", hue="Dataset", y="Time (s)", data=dflong_mapper_time, kind='box', legend=True)
    seaborn_bug(dflong_mapper_time, "Variant", "Dataset", "Time (s)", title="MapReduce Mapper Execution Time")
    #plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    #plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    #sns.move_legend(ax, "upper left", frameon=False)
    #plt.title("MapReduce Mapper Execution Time")
    #plt.tight_layout()
    #plt.show()

    mapreduce_reduce_time = pd.DataFrame({
        "AWS\nMSA": d1_aws_reducer_time + d2_aws_reducer_time + d3_aws_reducer_time,
        "GCP\nMSA": d1_gcp_reducer_time + d2_gcp_reducer_time + d3_gcp_reducer_time,
        "Dataset": (['d1'] * 10) + (['d2'] * 10) + (['d3'] * 10)
    })
    dflong_reduce_time = pd.melt(mapreduce_reduce_time, "Dataset", var_name='Variant', value_name='Time (s)')
    seaborn_bug(dflong_reduce_time, "Variant", "Dataset", "Time (s)", title="MapReduce Reducer Execution Time")
    #sns.catplot(x="Variant", hue="Dataset", y="Time (s)", data=dflong_reduce_time, kind='box')
    #plt.title("MapReduce Reducer Execution Time")
    #plt.tight_layout()
    #plt.show()

    mapreduce_mapper_ram = pd.DataFrame({
        "Refarch": d1_refarch_mapper_ram + d2_refarch_mapper_ram + d3_refarch_mapper_ram,
        "AWS\nMSA": d1_aws_mapper_ram + d2_aws_mapper_ram + d3_aws_mapper_ram,
        "GCP\nMSA": d1_gcp_mapper_ram + d2_gcp_mapper_ram + d3_gcp_mapper_ram,
        "Dataset": (['d1'] * 10) + (['d2'] * 10) + (['d3'] * 10)
    })
    dflong_mapper_ram = pd.melt(mapreduce_mapper_ram, "Dataset", var_name='Variant', value_name='RAM (KB)')
    seaborn_bug(dflong_mapper_ram, "Variant", "Dataset", "RAM (KB)", title="MapReduce Mapper RAM Usage")
    #sns.catplot(x="Variant", hue="Dataset", y="RAM (KB)", data=dflong_mapper_ram, kind='box')
    #plt.title("MapReduce Mapper RAM Usage")
    #plt.tight_layout()
    #plt.show()

    mapreduce_reduce_ram = pd.DataFrame({
        "AWS\nMSA": d1_aws_reducer_ram + d2_aws_reducer_ram + d3_aws_reducer_ram,
        "GCP\nMSA": d1_gcp_reducer_ram + d2_gcp_reducer_ram + d3_gcp_reducer_ram,
        "Dataset": (['d1'] * 10) + (['d2'] * 10) + (['d3'] * 10)
    })
    dflong_reduce_ram = pd.melt(mapreduce_reduce_ram, "Dataset", var_name='Variant', value_name='RAM (KB)')
    seaborn_bug(dflong_reduce_ram, "Variant", "Dataset", "RAM (KB)", title="MapReduce Reducer RAM Usage")
    #sns.catplot(x="Variant", hue="Dataset", y="RAM (KB)", data=dflong_reduce_ram, kind='box')
    #plt.title("MapReduce Reducer RAM Usage")
    #plt.tight_layout()
    #plt.show()


def seaborn_bug(df_long, x, hue, y, title):
    #df = pd.DataFrame([[2, 4, 5, 6, 1], [4, 5, 6, 7, 2], [5, 4, 5, 5, 1],
    #               [10, 4, 7, 8, 2], [9, 3, 4, 6, 2], [3, 3, 4, 4, 1]],
    #              columns=['a1', 'a2', 'a3', 'a4', 'b'])
    #df_long = pd.melt(df, "b", var_name="a", value_name="c")
    fig, ax = plt.subplots(figsize=(7, 5))
    #sns.boxplot(x="a", hue="b", y="c", data=df_long, ax=ax)
    sns.boxplot(x=x, hue=hue, y=y, data=df_long, ax=ax)
    ax.spines[['top', 'right']].set_visible(False)
    sns.move_legend(ax, bbox_to_anchor=(1.02, 0.55), loc='lower left', frameon=False)
    plt.title(title)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    #user_survey()
    mvcc()
    #zookeeper()
    #mapreduce()
    #seaborn_bug()

