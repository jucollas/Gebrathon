import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def generate_linalg_logo(
    title="LineaPy",
    A=np.array([[1.0, 0.6],
                [-0.3, 1.1]]),
    fname_base="linalg_logo"
):
    # Crear figura
    fig, ax = plt.subplots(figsize=(4, 4), dpi=300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Cuadrado unidad antes de la transformación
    square = np.array([[0,0],[1,0],[1,1],[0,1]])
    # Aplicar transformación lineal
    square_t = (A @ square.T).T
    
    # Dibujar cuadrado original (línea punteada)
    poly1 = Polygon(
      square, 
      fill = False, 
      linewidth = 1.2, 
      linestyle = '--', 
      edgecolor ='#a9a9a9')
    ax.add_patch(poly1)
    
    # Dibujar paralelogramo transformado (relleno transparente)
    poly2 = Polygon(
      square_t, 
      alpha = 0.2, 
      linewidth = 2.0
    )
    ax.add_patch(poly2)
    
    # Dibujar ejes guía
    ax.plot([-0.2, 1.6], [0, 0], linewidth=0.8, alpha=0.4)
    ax.plot([0, 0], [-0.6, 1.6], linewidth=0.8, alpha=0.4)
    
    # Vectores base
    e1, e2 = np.array([1,0]), np.array([0,1])
    Ae1, Ae2 = A @ e1, A @ e2
    
    # Dibujar vectores base originales
    ax.arrow(0,0,e1[0],e1[1], head_width=0.03, length_includes_head=True, linewidth=1.2, alpha=0.8)
    ax.arrow(0,0,e2[0],e2[1], head_width=0.03, length_includes_head=True, linewidth=1.2, alpha=0.8)
    
    # Dibujar vectores transformados
    ax.arrow(0,0,Ae1[0],Ae1[1], head_width=0.04, length_includes_head=True, linewidth=2.0, alpha=0.9)
    ax.arrow(0,0,Ae2[0],Ae2[1], head_width=0.04, length_includes_head=True, linewidth=2.0, alpha=0.9)
    
    # Eigenvector real (si existe)
    """vals, vecs = np.linalg.eig(A)
    real_indices = [i for i, v in enumerate(vals) if np.isreal(v)]
    if real_indices:
        i = real_indices[0]
        v = np.real(vecs[:, i])
        v = v / np.linalg.norm(v)  # Normalizar
        ax.arrow(0,0, v[0]*1.2, v[1]*1.2, head_width=0.05, length_includes_head=True, linewidth=2.4)"""
    
    # Título del logo
    #ax.text(0.02, 1.55, title, fontsize=16, fontweight='bold', ha='left', va='center')
    
    # Mostrar matriz usada
    #matrix_text = f"A = [[{A[0,0]:.1f}, {A[0,1]:.1f}], [{A[1,0]:.1f}, {A[1,1]:.1f}]]"
    #ax.text(0.02, -0.5, matrix_text, fontsize=8, ha='left', va='center', alpha=0.8)
    
    # Ajustar límites de la vista
    all_pts = np.vstack([square, square_t, [[0,0], Ae1, Ae2]])
    xmin, ymin = all_pts.min(axis=0) - 0.25
    xmax, ymax = all_pts.max(axis=0) + 0.25
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    # Guardar imágenes (PNG + SVG)
    plt.savefig(f"{fname_base}.png", bbox_inches='tight', pad_inches=0.1)
    plt.savefig(f"{fname_base}.svg", bbox_inches='tight', pad_inches=0.1)
    plt.show()
    

# Ejemplo de uso:
generate_linalg_logo(title="Gebrathon")
