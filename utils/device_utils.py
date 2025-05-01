import torch

def get_device():
    """
    Determine the appropriate device (CUDA or CPU) based on availability.
    
    Returns:
        torch.device: The available device (cuda or cpu)
    """
    if torch.cuda.is_available():
        try:
            # Test CUDA availability with a small operation
            torch.tensor([1.0], device="cuda")
            return torch.device("cuda")
        except RuntimeError:
            return torch.device("cpu")
    else:
        return torch.device("cpu")
    
def to_device(model, device=None):
    """
    Move a model to the specified device or determine the best device.
    
    Args:
        model: PyTorch model to move
        device: Target device (if None, will be determined automatically)
        
    Returns:
        The model on the appropriate device
    """
    if device is None:
        device = get_device()
    
    if device.type == "cuda":
        try:
            return model.cuda()
        except RuntimeError:
            print("Warning: CUDA error detected. Falling back to CPU.")
            return model.cpu()
    else:
        return model.cpu()
