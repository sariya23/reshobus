from logic.equation.linear_equation import LinearEquation, Difficult


class EquationGenerator:
    def __init__(self, difficult: Difficult, quantity_of_equations: int = 10):
        self.quantity_of_equations = quantity_of_equations
        self.difficult = difficult

    def generate_equations(self) -> list[LinearEquation]:
        equations = [
            LinearEquation.from_template_with_concrete_difficult(self.difficult)
            for _ in range(self.quantity_of_equations)
        ]
        return equations

    def generate_equations_pdf(self, equation: LinearEquation) -> None:
        pass


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from docx import Document
    from docx.shared import Inches

    def create_equation_image(latex, filename):
        fig, ax = plt.subplots(figsize=(2, 1))
        ax.text(0.5, 0.5, f"${latex}$", fontsize=20, ha="center", va="center")
        ax.axis("off")
        plt.savefig(filename, bbox_inches="tight")
        plt.close()

    def create_word_with_equations(doc_filename):
        doc = Document()
        doc.add_heading("Equation Example", level=1)

        # Добавление уравнения как изображения
        latex_equation = r"\alpha = 0.5"
        image_filename = "equation.png"
        create_equation_image(latex_equation, image_filename)

        doc.add_paragraph("Here is an equation:")
        doc.add_picture(image_filename, width=Inches(2))

        doc.save(doc_filename)

    create_word_with_equations("example.docx")
