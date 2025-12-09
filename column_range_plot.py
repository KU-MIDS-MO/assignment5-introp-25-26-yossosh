import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    ### Replace with your own code (begin) ###
    A = np.array(A)
    
    n_rows = A.shape[0]
    n_cols = A.shape[1]
    
    ranges = np.zeros(n_cols)
    
    for j in range(n_cols):
        col_min = A[0, j]
        col_max = A[0, j]
        
        for i in range(1, n_rows):
            value = A[i, j]
            if value < col_min:
                col_min = value  
            if value > col_max:
                col_max = value
                
        ranges[j] = col_max - col_min


    x_positions = np.arange(n_cols)

    plt.figure()
    bars = plt.bar(x_positions, ranges,
            label="Column ranges",
            color="skyblue")
    
    plt.xlabel("Column index")
    plt.ylabel("Range")
    plt.title("Column ranges")
    
    labels = []
    for j in range(n_cols):
        labels.append("Col" + str(j))
    plt.xticks(x_positions, labels)
    
    plt.grid(axis="y", linestyle="--", alpha=0.7) # alpha - transparency of lines
    
    plt.legend()
    
    for bar in bars:
        x = bar.get_x() + bar.get_width() / 2.0
        
        height = bar.get_height()
        
        plt.text(x, height + 1,
                 str(round(height, 1)),
                 ha="center", 
                 va="bottom", 
                 fontsize=8) # alignment
        
    plt.tight_layout()

    plt.savefig(filename)
    
    plt.show()
    
    plt.close()

    return ranges    
    ### Replace with your own code (end)   ###
array = np.array([
    [5,6,9,10],
    [27,32,11,65],
    [2,90,45,13],
    [12,76,9,11]
    ])

column_range_plot(array)

