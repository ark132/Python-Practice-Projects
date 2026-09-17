import numpy as np
import matplotlib.pyplot as plt
# Generation of my first image using numpy creating my childhood painting in paint software 
image_gen=np.ones((600,1200,3),dtype=np.uint8)*[135, 206, 235]
x=np.arange(0,1200)
y=np.arange(0,600)
X,Y=np.meshgrid(x,y)
cx,cy=700,90 # Column 700, Row 90
R=np.sqrt((X-cx)**2 + (Y-cy)**2)
# Sun
sun_radius=60
sun_mask=R<=sun_radius
np.arctan2(Y-cy,X-cx)
image_gen[sun_mask,:]=[255,127,39]
# Mountains
mountain=np.array(
    [
        [[200, 20], [0, 300], [400, 300]],  # Mountain 1
        [[480, 50], [300, 300], [650, 300]],  # Mountain 2
        [[950, 40], [800, 300], [1100, 300]],  # Mountain 3
        [[1100, 70], [1000, 300], [1200, 300]],  # Mountain 4
    ]
)
# 2. Compute boundary slopes with np.polyfit and fill pixels
for pts in mountain:
    peak,left,right=pts[0],pts[1],pts[2]
    # Get slopes (m) and intercepts (b)
    m_left,b_left=np.polyfit([left[0], peak[0]], [left[1], peak[1]], 1)
    m_right,b_right=np.polyfit([peak[0], right[0]], [peak[1], right[1]], 1)
    left_mask=Y>=(m_left*X+b_left)
    right_mask=Y>=(m_right*X+b_right)
    base_mask=Y<=left[1]
    # Combine and color green
    mountain_mask=left_mask & right_mask & base_mask
    image_gen[mountain_mask, :] = [34, 177, 76]
# House
house_body_mask=(X>=120)&(X<=280)&(Y>=420)&(Y<=520) #House structure
# Paint wall
image_gen[house_body_mask,:]=[240,215,140]
# House Roof
roof_peak=[200,330]
roof_left=[100,420]
roof_right=[300,420]
m_l,b_l=np.polyfit([roof_left[0], roof_peak[0]], [roof_left[1], roof_peak[1]], 1)
m_r,b_r=np.polyfit([roof_right[0], roof_peak[0]], [roof_right[1], roof_peak[1]], 1)
# Triangle Mask
roof_mask = (Y >= (m_l * X + b_l)) & (Y >= (m_r * X + b_r)) & (Y <= 420)
image_gen[roof_mask,:]=[180, 40, 40]

door_mask = (X >= 180) & (X <= 220) & (Y >= 460) & (Y <= 520)
# Paint Door (e.g., Dark Brown)
image_gen[door_mask, :] = [110, 60, 30]
# Window Rectangles
left_win = (X >= 140) & (X <= 165) & (Y >= 440) & (Y <= 465)
right_win = (X >= 235) & (X <= 260) & (Y >= 440) & (Y <= 465)

# Paint Glass (Cyan / Sky Blue)
image_gen[left_win | right_win, :] = [170, 225, 250]

# Window Frames (1-pixel cross lines)
left_cross = left_win & ((X == 152) | (Y == 452))
right_cross = right_win & ((X == 247) | (Y == 452))

# Paint Crosses (Dark Grey/Black)
image_gen[left_cross | right_cross, :] = [50, 50, 50]
plt.axis("off")
plt.grid(False)
plt.imshow(image_gen)
plt.show()