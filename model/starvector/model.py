def process_images(self, images):
    """
    Process images for the model with device awareness.
    
    Args:
        images: List of PIL images or tensors
        
    Returns:
        Processed images on the appropriate device
    """
    processed_images = []
    for image in images:
        if isinstance(image, torch.Tensor):
            # If already a tensor, just process it further
            processed = self.processor(images=image, return_tensors="pt")["pixel_values"]
        else:
            # Process from PIL image
            processed = self.processor(images=image, return_tensors="pt")["pixel_values"]
        
        processed_images.append(processed)
    
    return processed_images
