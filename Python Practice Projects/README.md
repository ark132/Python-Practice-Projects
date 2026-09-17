# 🎨 Childhood Landscape Recreation with Pure NumPy

A programmatic recreation of a classic childhood landscape painting built entirely using 
**pure NumPy matrix math and Matplotlib visualization**. 

This project bypasses traditional computer vision libraries (such as OpenCV) and drawing APIs to construct every geometric shape directly through 2D coordinate grids, vectorized boolean masks, and linear algebra.

---

## 🛠️ Implementation Details

* **Canvas Architecture:** 8-bit RGB 3D NumPy array (`600x1200x3`, `dtype=np.uint8`) updated via vector-based matrix indexing.
* **Coordinate Meshgrids:** Generated spatial coordinate matrices $X$ and $Y$ using `np.meshgrid()` for hardware-accelerated grid operations.
* **Sun Geometry:** Rendered using spatial Euclidean distance matrices:
  $$R = \sqrt{(X - c_x)^2 + (Y - c_y)^2} \le \text{radius}$$
* **Triangular Slopes (Mountains & Roof):** Defined vertex coordinates and dynamically solved linear slope equations ($y = mx + b$) using `np.polyfit()` to create triangular boundary masks.
* **House & Window Framing:** Bounded rectangular coordinate inequalities combined with bitwise boolean operations (`&`, `|`) and 1-pixel grid slices for crosshatched window frames.

---

## 🚀 Quickstart

### Prerequisites
```bash
pip install numpy matplotlib