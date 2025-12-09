import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    ### Replace with your own code (begin) ###
    signal = np.array(signal)
    diffs = [signal[i+1] - signal[i] for i in range(len(signal) - 1)]
    
    turn_indices = []
    for i in range(len(diffs)):
        prev_diff = diffs[i-1]
        cur_diff = diffs[i]
        if prev_diff * cur_diff < 0:
            turn_indices.append(i)
            
    turn_indices = np.array(turn_indices, dtype=int)
    
    x = np.arange(len(signal))
    
    plt.figure()
    plt.plot(x, signal, marker="o", label="Signal", zorder=1)
    
    if len(turn_indices) > 0:
        plt.scatter(
            turn_indices,
            signal[turn_indices],
            color="orange",
            s=60,
            label="Turning points",
            zorder=2)
        
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Signal with turning points")
    
    plt.grid(axis="y", linestyle="--", alpha=0.7) # transparency of lines
    
    plt.legend()
    
    plt.tight_layout()
    
    plt.savefig(filename)
    
    plt.show()
    
    plt.close()
    
    return turn_indices
    ### Replace with your own code (end)   ###
signal = [1,4,2,5,3,6]
detect_turning_points(signal)
