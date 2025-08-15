#This script is used to run inference on images using the MDETR model for referring expression detection on CLI
import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
from hubconf import mdetr_resnet101_refcoco
def run_inference(image_path, query, checkpoint_path, conf_threshold=0.9):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu") #Loading the GPU if available, otherwise CPU
    model, postprocessor = mdetr_resnet101_refcoco(pretrained=False, return_postprocessor=True)
    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint["model"])
    model.to(device).eval()

    transform = transforms.Compose([
        transforms.Resize(800),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0).to(device)  # (1,3,H,W)

    captions = [query]

    with torch.no_grad():
        mem_cache = model(img_tensor, captions, encode_and_save=True)
        outputs = model(img_tensor, captions, encode_and_save=False, memory_cache=mem_cache)

    target_sizes = torch.tensor([[image.height, image.width]], device=device)
    results = postprocessor(outputs, target_sizes)

    scores = results[0]["scores"].cpu()
    boxes = results[0]["boxes"].cpu()

    keep = scores > conf_threshold
    boxes = boxes[keep]
    scores = scores[keep]

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.imshow(image)

    for (xmin, ymin, xmax, ymax), score in zip(boxes, scores):
        ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                   fill=False, color='red', linewidth=3))
        ax.text(xmin, ymin, f"{score:.2f}", fontsize=12, color='white',
                bbox=dict(facecolor='red', alpha=0.5))

    plt.axis('off')
    plt.show()

def run_inference_streamlit(image_path, query, checkpoint_path, conf_threshold=0.9):
    run_inference(image_path, query, checkpoint_path, conf_threshold)
    
def input_query():
    input_query = input("Enter your query: ")
    return input_query

def input_image_path():
    print("If running in WSL and the image is in Windows, use the path like: /mnt/path/to/image.jpg", end="")
    print("ensure the use of forward slashes (/) in the path.")
    input_image_path = input("Enter the image path: ")
    return input_image_path


if __name__ == "__main__":
    
    run_inference(
        image_path=input_image_path(),
        query=input_query(),
        checkpoint_path="/home/shreyansh/mdetr/Checkpoint/refcoco_resnet101_checkpoint.pth"
    )