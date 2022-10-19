import torch
print("hello pytorch {}".format(torch.__version__))
print(torch.cuda.is_available())
print(torch.cuda.device_count() )# gpu数量
print(torch.cuda.current_device())# 当前设备索引, 从0开始
print(torch.cuda.get_device_name(0))# 返回gpu名字