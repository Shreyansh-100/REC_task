# Setup the Model

### Follow the steps given below:

1. **Clone the repository (xyz)**:
   ```bash
   git clone https://github.com/yourusername/xyz.git
   ```

2. **Setup a conda environment** in your terminal:
   ```bash
   conda create -n env_name
   conda activate env_name
   ```

3. **Enter the local repository**:
   ```bash
   cd xyz
   ```

4. **Run the command to install the necessary requisites**:
   ```bash
   pip install -r requirements.txt
   ```

5. **If you want to run the evaluation scripts** as instructed in the research paper and the original GitHub repository, follow the steps mentioned here:  
   [Evaluation Steps](https://github.com/ashkamath/mdetr/blob/main/.github/refexp.md) it will be prefferable if you did that, setupt the json's as mentioned in the above steps (link has been attached).

6. **Pre-trained model checkpoint**:  
   After cloning the repository, you will find the pre-trained model checkpoint available in the directory:  
   ```bash
   /Checkpoint/
   ```

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
