import torch
import subprocess

def check_nvidia_smi():
    try:
        result = subprocess.run(["nvidia-smi"], capture_output=True, text=True, check=True)
        print("===== nvidia-smi =====")
        print(result.stdout)
    except Exception as e:
        print("⚠️ 无法运行 nvidia-smi，请确认容器启动时加了 --gpus all，或者驱动是否正确安装。")
        print(e)

def check_pytorch():
    print("\n===== PyTorch 检测 =====")
    try:
        print("PyTorch 版本:", torch.__version__)
        print("编译时的 CUDA 版本:", torch.version.cuda)
        print("CUDA 是否可用:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("GPU 数量:", torch.cuda.device_count())
            for i in range(torch.cuda.device_count()):
                print(f" - GPU {i}: {torch.cuda.get_device_name(i)}")
            print("当前设备 ID:", torch.cuda.current_device())
        else:
            print("⚠️ 没有检测到 GPU")
    except Exception as e:
        print("⚠️ PyTorch 检测失败:", e)

def check_mmcv():
    import mmcv
    print(f"mmcv version: {mmcv.__version__}")

if __name__ == "__main__":
    check_nvidia_smi()
    check_pytorch()
    check_mmcv()

