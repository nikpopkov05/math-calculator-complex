class ComplexNumber:

    def __init__(self, real, imaginary):
        """
        Инициализирует объект комплексного числа

        :param real: Действительная часть комплексного числа
        :param imaginary: Мнимая часть комплексного числа
        """
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        """
        Перегружает оператор сложения для сложения двух комплексных чисел
        :param other: Другой объект комплексного числа, который нужно сложить с текущим
        :return: Новый объект комплексного числа, представляющий сумму двух комплексных чисел
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        """
        Перегружает оператор вычитания для вычитания двух комплексных чисел
        :param other: Другой объект комплексного числа, который нужно вычесть с текущим
        :return: Новый объект комплексного числа, представляющий разность двух комплексных чисел
        """
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        """
        Перегружает оператор умножения для умножения двух комплексных чисел
        :param other: Другой объект комплексного числа, который нужно умножить на текущее
        :return: Новый объект комплексного числа, представляющий произведение двух комплексных чисел
        """
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        """
        Перегружает оператор деления для деления двух комплексных чисел
        :param other: Другой объект комплексного числа, который нужно делить на текущее
        :return: Новый объект комплексного числа, представляющий частное двух комплексных чисел
        """
        denominator = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / denominator,
                             (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def __str__(self):
        """
        Возвращает строковое представление комплексного числа в формате 'a + bi'
        :return: Строка, представляющая комплексное число
        """
        return f"{self.real} + {self.imaginary}i"


def input_complex_number(prompt):
    """
    Запрашивает у пользователя ввод комплексного числа в виде 'a + bi'
    :param prompt: Сообщение, которое будет отображаться пользователю при запросе ввода
    :return: Объект комплексного числа, созданный на основе введенных данных
    """
    while True:
        try:
            value = input(prompt)
            real, imaginary = map(float, value.replace('i', '').split('+'))
            return ComplexNumber(real, imaginary)
        except ValueError:
            print("Неверный формат. Пожалуйста, введите в формате 'a + bi'.")


def determinant(matrix):
    """
    Вычисляет определитель квадратной матрицы
    :param matrix: Квадратная матрица, представленная в виде списков
    :return: Определитель матрицы, который мы задали
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = ComplexNumber(0, 0)
    for c in range(n):
        minor = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += matrix[0][c] * determinant(minor) * (-1 if c % 2 else 1)
    return det


def cramer_method(A, B):
    """
    Решает систему линейных уравнений с помощью метода Крамера
    :param A: Квадратная матрица коэффициентов(n x n)
    :param B: Вектор свободных членов (длина n)
    :return: Вектор решений (длина n), если система имеет единственное решение
    """
    det_A = determinant(A)
    if det_A.real == 0 and det_A.imaginary == 0:
        raise ValueError("Определитель матрицы A равен нулю. Система не имеет единственного решения.")

    n = len(B)
    X = []
    for i in range(n):
        # Создаем матрицу Ai, заменяя i-ый столбец на B
        Ai = [row[:] for row in A]
        for j in range(n):
            Ai[j][i] = B[j]
        det_Ai = determinant(Ai)
        X.append(det_Ai / det_A)

    return X


def main():
    """
    Главная функция программы, которая инициализирует выполнение.

    Эта функция выполняет следующие действия:
    - Запрашивает у пользователя ввод данных для решения системы линейных уравнений.
    - Вызывает метод Крамера для вычисления решений.
    - Выводит результаты на экран.

    :return: Вывод результатов всех вычислений
    """
    n = int(input("Введите размерность системы (n): "))

    A = [[ComplexNumber(0, 0) for _ in range(n)] for _ in range(n)]
    B = [ComplexNumber(0, 0) for _ in range(n)]

    # Ввод коэффициентов матрицы A
    print("Введите коэффициенты матрицы A (в формате 'a + bi'):")
    for i in range(n):
        for j in range(n):
            A[i][j] = input_complex_number(f"A[{i + 1}][{j + 1}]: ")

    # Ввод свободных членов B
    print("Введите свободные члены B (в формате 'a + bi')" )

if __name__ == "__main__":
    main()

