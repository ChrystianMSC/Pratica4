import tkinter as tk
import math

class TriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle do Triângulo")

        # Canvas para desenhar o triângulo
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Coordenadas iniciais do triângulo
        self.triangle = [200, 100, 150, 300, 250, 300]
        self.draw_triangle()

        # Botões de controle
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="↑ Cima", command=self.rotate_up).grid(row=0, column=1)
        tk.Button(btn_frame, text="↓ Baixo", command=self.rotate_down).grid(row=1, column=1)
        tk.Button(btn_frame, text="← Esquerda", command=self.rotate_left).grid(row=1, column=0)
        tk.Button(btn_frame, text="→ Direita", command=self.rotate_right).grid(row=1, column=2)

    def draw_triangle(self):
        self.canvas.delete("all")  # Limpa o canvas
        self.canvas.create_polygon(self.triangle, fill="blue")

    @staticmethod
    def rotate_triangle(coords, angle):
        # Centro do triângulo
        cx = sum(coords[::2]) / 3
        cy = sum(coords[1::2]) / 3

        # Aplica a rotação nas coordenadas
        rotated = []
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i + 1]
            x -= cx
            y -= cy
            x_rot = x * math.cos(angle) - y * math.sin(angle)
            y_rot = x * math.sin(angle) + y * math.cos(angle)
            rotated.append(x_rot + cx)
            rotated.append(y_rot + cy)
        return rotated

    def rotate(self, angle):
        self.triangle = self.rotate_triangle(self.triangle, angle)
        self.draw_triangle()

    def rotate_up(self):
        self.rotate(math.radians(-15))

    def rotate_down(self):
        self.rotate(math.radians(15))

    def rotate_left(self):
        self.rotate(math.radians(15))

    def rotate_right(self):
        self.rotate(math.radians(-15))


# Inicializa o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleApp(root)
    root.mainloop()
