# 3DKeyAD: Keypoint-Guided Prototype-Aligned Anomaly Detection in 3D Point Clouds
> [📄 Paper](https://arxiv.org/abs/2507.13110)  
---

## 📌 Overview

**3DKeyAD** is a 3D anomaly detection method in high-resolution point clouds.

---

## ✨ Highlights

- ✅ Multi-prototype rigid registration ensures consistent spatial alignment
- ✅ Keypoint-guided clustering focuses on geometrically informative regions
- ✅ Cluster-wise feature comparison supports raw, FPFH, and PointMAE features
- ✅ SOTA results on [Real3D-AD](https://github.com/M-3LAB/Real3D-AD) dataset

---
## 🔄 Quick Reproduction (No Environment Setup Needed)

We provide precomputed anomaly scores for every point and object in the dataset, allowing for immediate evaluation without configuring the environment.

### 📥 Step 1: Download Score Files
Please download the evaluation score files from the following link:

**[📦 Download Precomputed Scores](#)** <!-- TODO: Replace with actual download URL -->

### 🧪 Step 2: Run Evaluation Scripts
You can run the following evaluation scripts to reproduce the results of each variant. No training or inference is required.

```bash
# Evaluate 3DKeyAD (Raw+FS)
python EvalRawFs.py

# Evaluate 3DKeyAD (Raw+ISS+FS)
python EvalRawIssFs.py

# Evaluate 3DKeyAD (FPFH+ISS+FS)
python EvalFpfhLssFs.py

# Evaluate 3DKeyAD (Raw+FPFH+ISS+FS)
python EvalRawFpfhLssFs.py
```

Each script will output O-AUROC and P-AUROC scores as reported in the paper.

> 📝 **Note:** Make sure the downloaded score files are placed in the correct directory as expected by each script.

---
## 📊 Results
<img width="1062" height="555" alt="image" src="https://github.com/user-attachments/assets/eb5cf97c-1d1e-46ff-931b-1d2546443947" />
<img width="1068" height="506" alt="image" src="https://github.com/user-attachments/assets/11479ded-5b68-4c3a-b239-66e194a9c82f" />

---
## 📖 Citation
```bibtex
@misc{wang20253dkeyad,
  title={3DKeyAD: High-Resolution 3D Point Cloud Anomaly Detection via Keypoint-Guided Point Clustering}, 
  author={Zi Wang and Katsuya Hotta and Koichiro Kamide and Yawen Zou and Chao Zhang and Jun Yu},
  year={2025},
  eprint={2507.13110},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2507.13110}, 
}

