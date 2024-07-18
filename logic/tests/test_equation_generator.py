import os

from logic.equation.linear_equation import Difficult
from logic.equation_generator.equation_generator import EquationGenerator


def test_file_with_equation_created_after_generate(remove_tmp_dir_after_test):
    generator = EquationGenerator(difficult=Difficult.EASY, quantity_of_equations=10)
    equations = generator.generate_equations()

    generator.generate_equations_to_doc_file(equations, filename="test.doc")
    generator.generate_answers_to_doc_file(equations, filename="test_answer.doc")

    assert os.path.exists(os.path.join(generator.PATH_TO_SAVE_DIR, "test.doc"))
    assert os.path.exists(os.path.join(generator.PATH_TO_SAVE_DIR, "test_answer.doc"))
