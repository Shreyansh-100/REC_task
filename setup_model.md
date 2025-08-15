# Setup the Model
A lot of files/scripts are useful only when runnig evaluation on the refcoco dataset, the link to the repository for that has been provided in Step 5.

Note:- If setting up GPU, run the following command in CMD locally to check the CUDA version and GPU functionality. (This is for a nvidia based GPU)
   ```
      nvidia-smi    
   ``` 
---
### Follow the steps given below:

1. **Clone the repository (xyz)**:
   ```bash
   git clone https://github.com/Shreyansh-100/REC_task
   ```

2. **Setup a conda environment** in your terminal:
   ```bash
   conda create -n mdetr_env
   conda activate mdetr env
   ```

3. **Enter the local repository**:
   ```bash
   cd mdetr
   ```

4. **Run the command to install the necessary requisites**:
   ```bash
   pip install -r requirements.txt
   ```

5. **If you want to run the evaluation scripts** as instructed in the research paper and the original GitHub repository, follow the steps mentioned here:  
   [Evaluation Steps](https://github.com/ashkamath/mdetr/blob/main/.github/refexp.md) it will be prefferable if you did that, setupt the json's as mentioned in the above steps (link has been attached).

6. **Pre-trained model checkpoint**:  
   After cloning the repository, you will find the pre-trained model checkpoint available in the directory,once you download it from the link attached: [Checkpoint](https://zenodo.org/record/4721981/files/refcoco_resnet101_checkpoint.pth?download=1)
   
   Ensure the the directory looks like
   ```bash

   /Checkpoint/<checkpoint-name>.pth
   ```

   Ensure to change the checkpoint path in the inference.py script to run locally.
   

7. **Run the command to perform inference on your own image and query**:
   ```bash
   python inference.py
   ```

---

## ADDITIONAL

Since running inference with image path and query in the terminal might be a bit exhausting, follow these steps to run inference using a web interface.

1. **Ensure you have the `stream.py` script**.

2. **To run this script, first install the required dependencies**:
   ```bash
   pip install -r optional_requirements.txt
   ```

3. **Run the command on your existing conda-activated terminal**:
   ```bash
   streamlit run stream.py
   ```
