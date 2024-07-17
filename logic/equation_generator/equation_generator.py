from logic.equation.linear_equation import LinearEquation, Difficult
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Inches


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

    @staticmethod
    def __create_equation_image(
        equation: str, filename: str = "equation_image.png"
    ) -> None:
        fig, ax = plt.subplots(figsize=(2, 1))
        ax.text(0.5, 0.5, f"{equation}", fontsize=20, ha="center", va="center")
        ax.axis("off")
        plt.savefig(filename, bbox_inches="tight")
        plt.close()

    @staticmethod
    def __convert_python_string_to_latex(equation: str) -> str:
        latex_equation = equation.replace("*", r"\cdot ")
        latex_equation = f"${latex_equation}$"
        return latex_equation

    def generate_equations_to_docx_file(
        self, equations: list[LinearEquation], filename: str = "equation.doc"
    ) -> None:
        doc = Document()
        doc.add_heading(
            f"Уравнения с уровнем сложности {self.difficult.value}", level=1
        )

        for equation in equations:
            latex_equation = self.__convert_python_string_to_latex(equation.equation)
            image_filename = "equation.png"
            self.__create_equation_image(latex_equation, image_filename)
            doc.add_picture(image_filename, width=Inches(2))

        doc.save(filename)


if __name__ == "__main__":
    generator = EquationGenerator(difficult=Difficult.EASY, quantity_of_equations=5)
    equations = generator.generate_equations()
    generator.generate_equations_word(equations)
